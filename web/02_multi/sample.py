from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/ping')
def pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
