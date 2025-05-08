import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/add_url', methods=['GET'])
def add_url():
    url = request.args.get('url')
    with psycopg2.connect(
            dbname="myapp_db",
            user="myapp_user",
            password="mypassword",
            host="database",
            port="5432"
    ) as connect:
        with connect.cursor() as cursor:
            cursor.execute("INSERT INTO urls (url) VALUES (%s)", (url,))
            connect.commit()
    return jsonify({"message": "URL added successfully!"}), 201


@app.route('/get_urls', methods=['GET'])
def get_urls():
    with psycopg2.connect(
            dbname="myapp_db",
            user="myapp_user",
            password="mypassword",
            host="database",
            port="5432"
    ) as connect:
        with connect.cursor() as cursor:
            cursor.execute("SELECT * FROM urls")
            urls = cursor.fetchall()
    return jsonify(urls)

@app.route('/')
def blocked():
    return "oops.."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)

# http://10.157.35.132:5100/parser?url=https://habr.com/ru/feed/
# https://ya.ru/
# https://translate.google.com/?sl=en&tl=ru&op=translate
# https://www.google.com/