from flask import jsonify


class R(object):
    code = '0'
    msg = '处理完成'
    data = None

    def __init__(self):
        pass

    def dict(self):
        return {k.lower(): v for k, v in self.__dict__.items() if not k.startswith('_sa')}

def ok(data):
    r = R()
    r.data = data
    return r

def fail(code, data):
    r = R()
    r.code = code
    r.data = data
    return r
