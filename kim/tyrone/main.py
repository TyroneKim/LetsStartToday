from flask import Flask

from kim.tyrone import config

app = Flask(__name__)

if __name__ == '__main__':
    config.init(app)
    app.run(host="127.0.0.1", port=10000, debug=True)
