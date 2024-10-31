from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def mysql(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://tyrone:Kiban410.@172.16.150.128/py-dev'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


def view(app):
    from log.route import log
    from user.route import user
    app.register_blueprint(user)
    app.register_blueprint(log)

def login(app):
    login_manager.init_app(app)

def init(app):
    mysql(app)
    view(app)
    login(app)