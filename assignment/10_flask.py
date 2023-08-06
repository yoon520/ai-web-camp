from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    db_conn = pymysql.connect(host='localhost', user='root',
            password='1234', database='myweb',
            autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    with db_conn:
        db_cursor = db_conn.cursor()
        db_cursor.execute("SELECT genre, title, star, poster, creator FROM post WHERE userId=1")
        postAll = db_cursor.fetchall()

        db_cursor = db_conn.cursor()
        db_cursor.execute("SELECT hashtag FROM post WHERE userId=1")
        hashtag = db_cursor.fetchall()
        hashtag_li = {}
        for i in hashtag:
            if i['hashtag'] not in hashtag_li:
                hashtag_li[i['hashtag']] = 1
            else:
                hashtag_li[i['hashtag']] += 1
        hashtag_li = sorted(hashtag_li, key = lambda x: hashtag_li[x], reverse=True)

    return render_template('myWeb.html', postAll = postAll, hashtag = hashtag_li[:10])

if __name__ == "__main__":
    app.run(port=5001, debug=True)