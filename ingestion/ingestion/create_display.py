from .get_eternal_engine import engine
from sqlalchemy import select
from .create_tables import book_details, book_results, book_display, author_details, author_results, author_display


def create_book_display():
    engine.execute(book_display.delete())
    display_df = book_results.join(book_details, book_results.c.book_id == book_details.c.book_id, isouter=True)
    # Drop duplicate book_id col after join
    required_cols = [book_results] + [x for x in book_details.columns if x.key != 'book_id']
    display_sql = select(required_cols).select_from(display_df)
    display_results = engine.execute(display_sql)
    engine.execute(book_display.insert(), list(display_results))


def create_author_display():
    engine.execute(author_display.delete())
    display_df = author_results.join(author_details, author_results.c.author_id == author_details.c.author_id, isouter=True)
    # Drop duplicate author_id col after join
    required_cols = [author_results] + [x for x in author_details.columns if x.key != 'author_id']
    display_sql = select(required_cols).select_from(display_df)
    display_results = engine.execute(display_sql)
    engine.execute(author_display.insert(), list(display_results))
