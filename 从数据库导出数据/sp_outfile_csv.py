import os

import pymysql
import csv


# 数据处理好，看如何塞入execl中


def csv_dict_write(path, head, data):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writeheader()
        writer.writerows(data)
        return True


if __name__ == '__main__':
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    count_sql = "select count(*) from SP500_FinData_sina; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    big_list = []
    for num in range(1, long_count):
        sql = 'select name,d1,d2,d3,d4,d5  from SP500_FinData_sina where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)

    # #执行sql语句
# name,d1,d2,d3,d4,d5
    head = ['name', 'd1', "d2", "d3","d4","d5"]
    l_path = os.getcwd()
    csv_dict_write('{0}/SP500_FinData_sina.csv'.format(l_path), head, big_list)
    print("数据导出完成～")