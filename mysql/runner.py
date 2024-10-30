import tables

# 配置数据库连接
config = {
    'user': 'tyrone',       # 数据库用户名
    'password': 'Kiban410.',   # 数据库密码
    'host': '172.16.150.128',           # 数据库主机
    'database': 'py-dev',   # 数据库名称
}


def str_format(f_str, **param):
    return f_str.format(**param)
    pass


if __name__ == '__main__':
    tables.name_print(**config)
    pass