FROM python:3.7.9

RUN pip install --no-cache-dir sqlalchemy pymysql requests python-dateutil

COPY ingestion .

CMD python main.py