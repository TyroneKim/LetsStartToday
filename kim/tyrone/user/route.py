from array import array

from flask import Blueprint, request, jsonify
from sqlalchemy.sql.functions import random
from sqlalchemy.util import md5_hex

from kim.tyrone.bean.User import User
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


@user.route('/user/save', methods=['POST'])
def user_save():
    json = request.json
    new_user = User()
    new_user.set_attrs(json)
    db.session.add(new_user)
    db.session.commit()
    return ""