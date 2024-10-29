import mysql.connector

# 配置数据库连接
config = {
    'user': 'root',       # 数据库用户名
    'password': 'asx12!.y',   # 数据库密码
    'host': 'localhost',           # 数据库主机
    'database': 'script',   # 数据库名称
}

if __name__ == '__main__':
    try:
        # 连接到数据库
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # 查询包含 application_status 字段的所有表
        query = """
        SELECT table_name 
        FROM information_schema.columns 
        WHERE table_schema = %s AND column_name = 'application_status';
        """
        cursor.execute(query, (config['database'],))

        tables_with_field = [row[0] for row in cursor.fetchall()]

        # 循环查询每个表中 application_status 字段不为空的记录数量
        print("Tables with 'application_status' and non-null count:")
        for table in tables_with_field:
            count_query = f"SELECT COUNT(*) FROM `{table}` WHERE application_status IS NOT NULL;"
            cursor.execute(count_query)
            count = cursor.fetchone()[0]
            if 0 < count:
                print(f"Table: {table}, Non-NULL application_status count: {count}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # 关闭数据库连接
        if conn.is_connected():
            cursor.close()
            conn.close()
