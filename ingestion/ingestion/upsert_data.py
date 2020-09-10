import os
from sqlalchemy.dialects.mysql import insert

from .create_tables import book_ratings, author_ratings, book_details, author_details
from .get_eternal_engine import engine
from .xml_parser import get_book_ratings_from_xml, \
    get_author_ratings_from_xml, get_book_details_from_xml, get_author_details_from_xml

data_dir = os.environ['DATA_DIR']
xml_folder = os.path.join(data_dir, 'xml')


def upsert_book_ratings(xml_path):
    books_to_insert = get_book_ratings_from_xml(xml_path)
    review_insert_statement = insert(book_ratings).values(books_to_insert)
    review_on_duplicate_statement = review_insert_statement.on_duplicate_key_update(
        rating=review_insert_statement.inserted.rating
    )
    engine.execute(review_on_duplicate_statement)


def upsert_author_ratings(xml_path):
    authors_to_insert = get_author_ratings_from_xml(xml_path)
    review_insert_statement = insert(author_ratings).values(authors_to_insert)
    review_on_duplicate_statement = review_insert_statement.on_duplicate_key_update(
        rating=review_insert_statement.inserted.rating
    )
    engine.execute(review_on_duplicate_statement)


def upsert_book_details(xml_path):
    book_details_to_upsert = get_book_details_from_xml(xml_path)
    book_insert_statement = insert(book_details).values(book_details_to_upsert)
    book_on_duplicate_statement = book_insert_statement.on_duplicate_key_update(
        reviews_count=book_insert_statement.inserted.reviews_count,
        ratings_count=book_insert_statement.inserted.ratings_count,
        average_rating=book_insert_statement.inserted.average_rating,
        image_url=book_insert_statement.inserted.image_url
    )
    engine.execute(book_on_duplicate_statement)


def upsert_author_details(xml_path):
    author_details_to_upsert = get_author_details_from_xml(xml_path)
    author_insert_statement = insert(author_details).values(author_details_to_upsert)
    author_on_duplicate_statement = author_insert_statement.on_duplicate_key_update(
        reviews_count=author_insert_statement.inserted.reviews_count,
        ratings_count=author_insert_statement.inserted.ratings_count,
        average_rating=author_insert_statement.inserted.average_rating,
        image_url=author_insert_statement.inserted.image_url
    )
    engine.execute(author_on_duplicate_statement)