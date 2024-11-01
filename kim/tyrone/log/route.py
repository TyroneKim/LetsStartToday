from flask import Blueprint, request

from kim.tyrone.log import server

log = Blueprint('log', __name__)


@log.route('/log/dir/<server>', methods=['POST'])
def get_log_dir():
    json = request.json
    server_conf = server.config[json['name']]
    return json.get('user')
