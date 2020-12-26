from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/movie')
def movie():
    data = []
    db = sqlite3.connect("movie.db")
    cur = db.cursor()
    sql = "select * from movie250"
    data_ = cur.execute(sql)
    for item in data_:
        data.append(item)
    cur.close()
    db.close()
    return render_template("movie.html", movies=data)


@app.route('/rate')
def rate():
    rate = []
    freq = []
    db = sqlite3.connect("movie.db")
    cur = db.cursor()
    sql = "select rate, count(rate) from movie250 group by rate"
    data_ = cur.execute(sql)
    data = []
    for item in data_:
        rate.append(item[0])
        freq.append(item[1])
    cur.close()
    db.close()

    return render_template("rate.html", rate=rate, freq=freq)


@app.route('/word')
def word():
    return render_template("word.html")


if __name__ == '__main__':
    app.run()
