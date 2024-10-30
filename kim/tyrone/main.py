from crypt import methods

from flask import Flask
from log.route import *
from user.route import *

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(log)


@app.route('/hello')
def hello_word():
    return 'Hello, World'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=10000, debug=True)