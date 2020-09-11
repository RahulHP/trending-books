from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData, Float, ForeignKey
meta = MetaData()
recent_books = Table(
    'recent_books', meta,
    Column('review_id', String(length=32), primary_key=True),
    Column('book_id', String(length=32)),
    Column('rating', Integer),
    Column('review_time', DateTime),
    Column('ingestion_time', DateTime)
)

recent_authors = Table(
    'recent_authors', meta,
    Column('review_id', String(length=32), primary_key=True),
    Column('author_id', String(length=32)),
    Column('rating', Integer),
    Column('review_time', DateTime),
    Column('ingestion_time', DateTime)
)

all_books = Table(
    'all_books', meta,
    Column('review_id', String(length=32), primary_key=True),
    Column('book_id', String(length=32)),
    Column('rating', Integer),
    Column('review_time', DateTime),
    Column('ingestion_time', DateTime)
)

all_authors = Table(
    'all_authors', meta,
    Column('review_id', String(length=32), primary_key=True),
    Column('author_id', String(length=32)),
    Column('rating', Integer),
    Column('review_time', DateTime),
    Column('ingestion_time', DateTime)
)

book_results = Table(
    'book_results', meta,
    Column('result_duration', String(length=32)),
    Column('result_date', DateTime),
    Column('stat_type', String(length=32)),
    Column('book_id', String(length=32), ForeignKey("book_details.book_id")),
    Column('stat_value', Float)
)

book_display = Table(
    'book_display', meta,
    Column('result_duration', String(length=32)),
    Column('result_date', DateTime),
    Column('stat_type', String(length=32)),
    Column('book_id', String(length=32)),
    Column('stat_value', Float),
    Column('title', String(length=255)),
    Column('title_without_series', String(length=255)),
    Column('reviews_count', Integer),
    Column('ratings_count', Integer),
    Column('average_rating', Float),
    Column('image_url', String(length=256))
)

author_display = Table(
    'author_display', meta,
    Column('result_duration', String(length=32)),
    Column('result_date', DateTime),
    Column('stat_type', String(length=32)),
    Column('author_id', String(length=32)),
    Column('stat_value', Float),
    Column('name', String(length=255)),
    Column('reviews_count', Integer),
    Column('ratings_count', Integer),
    Column('average_rating', Float),
    Column('image_url', String(length=256))
)

author_results = Table(
    'author_results', meta,
    Column('result_duration', String(length=32)),
    Column('result_date', DateTime),
    Column('stat_type', String(length=32)),
    Column('author_id', String(length=32), ForeignKey("author_details.author_id")),
    Column('stat_value', Float)
)

book_details = Table(
    'book_details', meta,
    Column('book_id', String(length=32), primary_key=True),
    Column('title', String(length=255)),
    Column('title_without_series', String(length=255)),
    Column('reviews_count', Integer),
    Column('ratings_count', Integer),
    Column('average_rating', Float),
    Column('image_url', String(length=256))
)

author_details = Table(
    'author_details', meta,
    Column('author_id', String(length=32), primary_key=True),
    Column('name', String(length=255)),
    Column('reviews_count', Integer),
    Column('ratings_count', Integer),
    Column('average_rating', Float),
    Column('image_url', String(length=256))
)
