from flask import Blueprint, request

user = Blueprint('login', __name__)

@user.route('/user/login', methods=['POST'])
def login():
    json = request.json
    return json.get('user')