import requests
from datetime import datetime
import os
data_dir = os.environ['DATA_DIR']
SECRET_KEY = os.environ['GOODREADS_API']
RECENT_REVIEWS_API = "https://www.goodreads.com/review/recent_reviews.xml"


def download_xml():
    r = requests.get(RECENT_REVIEWS_API, params={'key': SECRET_KEY})
    file_format = 'recent_reviews_{time}.xml'.format(time=datetime.now().strftime("%Y_%m_%d_%H_%M"))
    xml_path = os.path.join(data_dir, 'xml', file_format)
    with open(xml_path, 'wb') as fp:
        fp.write(r.content)
    return xml_path


if __name__ == '__main__':
    _ = download_xml()
