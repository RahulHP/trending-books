from .get_eternal_engine import engine
from sqlalchemy import func
from sqlalchemy.sql import select
from sqlalchemy.sql.expression import literal
from .create_tables import book_ratings, book_results, author_ratings, author_results
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
from itertools import product


def get_historical_date(current_date: date, duration: str):
    if duration == 'day':
        delta = relativedelta(days=-1)
    elif duration == 'week':
        delta = relativedelta(weeks=-1)
    elif duration == 'month':
        delta = relativedelta(months=-1)
    elif duration == 'year':
        delta = relativedelta(years=-1)
    else:
        raise NotImplementedError(duration)
    return current_date + delta


def get_stats(duration, stat_type, object_type):
    if object_type == 'book':
        rating_table = book_ratings
        primary_key = 'book_id'
    elif object_type == 'author':
        rating_table = author_ratings
        primary_key = 'author_id'
    else:
        raise ValueError("Unsupported object_type:", object_type)

    table_columns = getattr(rating_table, 'c')

    primary_key_col = getattr(table_columns, primary_key)
    current_datetime = datetime.today().date()
    filter_datetime = get_historical_date(current_datetime, duration)
    if stat_type == 'popularity':
        stat = func.count(getattr(table_columns, 'review_id'))
    elif stat_type == 'rating':
        stat = func.avg(getattr(table_columns, 'rating'))
    else:
        raise NotImplementedError()
    data = engine.execute(
        select([literal(duration).label('result_duration'),
                literal(current_datetime).label('result_date'),
                literal(stat_type).label('stat_type'),
                primary_key_col,
                stat.label('stat_value')])
            .where(getattr(table_columns, 'review_time') >= filter_datetime)
            .where(getattr(table_columns, 'review_time') <= current_datetime)
            .group_by(primary_key_col)
            .order_by(stat.desc())
            .limit(10))
    return [dict(x) for x in data]


def calculate_rankings():
    engine.execute(book_results.delete())
    engine.execute(author_results.delete())
    stats = ['popularity', 'rating']
    durations = ['day', 'week', 'month', 'year']
    object_type = ['book', 'author']
    for object_type, stat, duration in product(object_type, stats, durations):
        data = get_stats(duration, stat, object_type)
        if object_type == 'book':
            engine.execute(book_results.insert(), data)
        elif object_type == 'author':
            engine.execute(author_results.insert(), data)
