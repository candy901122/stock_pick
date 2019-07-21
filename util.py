import pymysql

db_url = 'mysql://root:root@127.0.0.1/StockPick?charset=utf8'
conn = pymysql.connect(user='root', password='root', database='StockPick')


def get_data_by_table(cur, table_name):
    sql = "SELECT * FROM %s;" % table_name
    cur.execute(sql)
    return cur.fetchall()


def get_data_by_table_query(cur, table_name, query):
    sql = "SELECT * FROM %s where %s;" % (table_name, query)
    cur.execute(sql)
    return cur.fetchall()


def get_data_field_by_table_query(cur, table_name, field, query):
    sql = "SELECT %s FROM %s where %s;" % (field, table_name, query)
    cur.execute(sql)
    return cur.fetchall()

