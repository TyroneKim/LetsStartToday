from flask import Flask

from kim.tyrone import config

app = Flask(__name__)

if __name__ == '__main__':
    config.init(app)
    # 大吉大利 大吉大利
    app.run(host="127.0.0.1", port=16666, debug=True)
