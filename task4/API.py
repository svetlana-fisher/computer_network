from parser import fetch_data, init_driver
from time import sleep

from flask import Flask, jsonify, request

from data import read_data, write_data

app = Flask(__name__)

@app.route('/parser', methods=['GET'])
def parser():
    url = request.args.get('url')
    driver = init_driver()
    driver.get(url)
    sleep(5)  # Ждем загрузки страницы
    data = fetch_data(driver)
    sleep(5)
    driver.quit()
    write_data(data)
    habr_data = read_data()
    return jsonify(habr_data)

if __name__ == '__main__':
    app.run(debug=True)

