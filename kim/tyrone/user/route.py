from flask import Blueprint, request

from kim.tyrone.user.bean.User import User
from kim.tyrone.config import db

user = Blueprint('user', __name__)


@user.route('/user/login', methods=['POST'])
def login():
    json = request.json
    return json.get('user')


@user.route('/user/list', methods=['POST'])
def user_list():
    users = User.query.all()
    user_dicts = []
    for a in users:
        user_dicts.append(a.to_dict())
    return user_dicts


@user.route('/user/register', methods=['POST'])
def user_save():
    json = request.json
    if User.query.filter(User.username==json.get("username")).count() > 0:
        return '用户名已存在'
    new_user = User()
    new_user.set_attrs(json)
    db.session.add(new_user)
    db.session.commit()
    return ""
