from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from tables import book_display, author_display
import os

db_user = os.environ['MYSQL_USER']
db_password = os.environ['MYSQL_ROOT_PASSWORD']
db_host = os.environ['MYSQL_HOST']
db_port = os.environ['MYSQL_PORT']
db_name = os.environ['MYSQL_DATABASE']
db_url = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # https://stackoverflow.com/q/33738467
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return redirect(url_for('display', object_type='books', duration='day', sort='popularity'))


@app.route('/<object_type>/<duration>/<sort>')
def display(object_type, duration, sort):
    # TODO: Error checking for type,duration and sort
    if object_type == 'books':
        display_table = book_display
        table_columns = getattr(display_table, 'c')
        display_html = 'book_display.html'
    else:
        display_table = author_display
        table_columns = getattr(display_table, 'c')
        display_html = 'author_display.html'

    filter_condition = and_(getattr(table_columns, 'result_duration') == duration,
                            getattr(table_columns, 'stat_type') == sort)
    select_statement = getattr(display_table, 'select')(filter_condition)
    query_results = db.engine.execute(select_statement)
    results = [dict(i) for i in query_results]

    return render_template(display_html, display=results, object_type=object_type, duration=duration, sort=sort)


@app.route('/authors')
def display_authors():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
