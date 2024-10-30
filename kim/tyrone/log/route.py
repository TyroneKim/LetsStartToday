from flask import Blueprint, request
import server

log = Blueprint('login', __name__)

@log.route('/log/dir/<str:server>', methods=['POST'])
def get_log_dir():
    json = request.json
    server_conf = server.config[json['name']]
    return json.get('user')
