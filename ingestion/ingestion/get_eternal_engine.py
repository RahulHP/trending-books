from sqlalchemy import create_engine
import os
db_user = os.environ['MYSQL_USER']
db_password = os.environ['MYSQL_ROOT_PASSWORD']
db_host = os.environ['MYSQL_HOST']
db_port = os.environ['MYSQL_PORT']
db_name = os.environ['MYSQL_DATABASE']
db_url = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'
engine = create_engine(db_url)
