import mysql.connector

def name_print(**config):
    try:
        # 连接到数据库
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # 查询所有表
        query = """
        SELECT table_name, column_name
        FROM information_schema.columns 
        WHERE table_schema = %s;
        """
        cursor.execute(query, (config['database'],))

        for row in cursor.fetchall():
            print(f"Table: {row[0]}, Column: {row[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # 关闭数据库连接
        if conn.is_connected():
            cursor.close()
            conn.close()
