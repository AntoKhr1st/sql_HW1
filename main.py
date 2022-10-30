import sqlite3
import flask

from utils import search_by_tite, search_by_release_year, search_by_rating, search_by_genre

app = flask.Flask(__name__)


@app.route("/movie/<title>")
def view_title(title):
    result = search_by_tite(title)
    return result


@app.route("/movie/<int:year_1>/to/<int:year_2>")
def view_release_year(year_1, year_2):
    result = search_by_release_year(year_1, year_2)
    return result


@app.route("/rating/<rating>")
def view_rating(rating):
    result = search_by_rating(rating)
    return result


@app.route("/genre/<genre>")
def view_genre(genre):
    result = search_by_genre(genre)
    return result

if __name__ == '__main__':
    app.run()
