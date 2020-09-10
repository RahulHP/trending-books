from datetime import datetime
from typing import List
from xml.etree import ElementTree as ET

REVIEW_TIMEZONE_FORMAT = '%a %b %d %H:%M:%S %z %Y'


def parse_books(element: ET.Element) -> List[dict]:
    book_id = element.find('book').findtext('id')
    rating = element.findtext('rating')
    review_id = element.findtext('id')
    review_time = datetime.strptime(element.findtext('date_updated'), REVIEW_TIMEZONE_FORMAT)
    return [{'book_id': book_id, 'review_id': review_id, 'rating': int(rating), 'review_time': review_time,
            'ingestion_time': datetime.now()}]


def parse_authors(element: ET.Element) -> List[dict]:
    rating = element.findtext('rating')
    review_id = element.findtext('id')
    review_time = datetime.strptime(element.findtext('date_updated'), REVIEW_TIMEZONE_FORMAT)
    results = list()
    authors = element.findall('.book/authors/author')
    for author in authors:
        results.append({'author_id': author.findtext('id'), 'review_id': review_id, 'rating': int(rating),
                        'review_time': review_time, 'ingestion_time': datetime.now()})
    return results


def get_book_details(element: ET.Element) -> List[dict]:
    child_element = element.find('book')
    return [{'book_id': child_element.findtext('id'),
             'title': child_element.findtext('title'),
             'title_without_series': child_element.findtext('title_without_series'),
             'reviews_count': int(child_element.findtext('text_reviews_count')),
             'ratings_count': int(child_element.findtext('ratings_count')),
             'average_rating': float(child_element.findtext('average_rating')),
             'image_url': child_element.findtext('image_url')}]


def get_author_details(element: ET.Element) -> List[dict]:
    results = list()
    authors = element.findall('.book/authors/author')
    for child_element in authors:
        results.append({'author_id': child_element.findtext('id'),
                        'name': child_element.findtext('name'),
                        'reviews_count': int(child_element.findtext('text_reviews_count')),
                        'ratings_count': int(child_element.findtext('ratings_count')),
                        'average_rating': float(child_element.findtext('average_rating')),
                        'image_url': child_element.findtext('image_url')})
    return results


def get_book_ratings_from_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    books_to_insert = list()
    for review in root.findall('./reviews/review'):
        books = parse_books(review)
        books_to_insert.extend(books)
    return books_to_insert


def get_author_ratings_from_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    authors_to_insert = list()
    for review in root.findall('./reviews/review'):
        authors = parse_authors(review)
        authors_to_insert.extend(authors)
    return authors_to_insert


def get_book_details_from_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    book_details_to_upsert = list()
    for review in root.findall('./reviews/review'):
        books = get_book_details(review)
        book_details_to_upsert.extend(books)
    return book_details_to_upsert


def get_author_details_from_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    author_details_to_upsert = list()
    for review in root.findall('./reviews/review'):
        authors = get_author_details(review)
        author_details_to_upsert.extend(authors)
    return author_details_to_upsert