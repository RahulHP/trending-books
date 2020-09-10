import os
from ingestion.create_tables import create_tables
from ingestion.xml_downloader import download_xml
from ingestion.upsert_data import upsert_book_ratings, upsert_author_ratings, upsert_book_details, upsert_author_details
from ingestion.calculate_rankings import calculate_rankings
from ingestion.create_display import create_book_display, create_author_display

data_dir = os.environ['DATA_DIR']
if __name__ == '__main__':
    create_tables()
    xml_dir = os.path.join(data_dir, 'xml')
    if not os.path.isdir(xml_dir):
        os.makedirs(xml_dir)
    xml_path = download_xml()
    upsert_book_ratings(xml_path)
    upsert_author_ratings(xml_path)
    upsert_book_details(xml_path)
    upsert_author_details(xml_path)

    xml_file = xml_path.split('/')[-1]
    renamed_file_path = os.path.join(data_dir, 'xml', xml_file[:-4] + '_processed.xml')
    os.rename(xml_path, renamed_file_path)

    calculate_rankings()
    create_book_display()
    create_author_display()
    print('DONE')



