# 定时执行
# MySQL的mysql数据库的表
# blog_block【block_id block_time block_high block_hash block_text】
# block_txt【block_id block_ipfs】

# 定时执行
# MySQL的mysql数据库的表
# blog_mail【block_id text_id text_hash text】
# blog_block【block_id block_time block_high block_hash block_text】

import pymysql
import time
import os

def copy_table():
    # 创建连接对象
    db_ser = pymysql.connect(host = "34.203.191.78", user = "root", password = "123456", database = "mysql", charset = "utf8mb4")
    db_show = pymysql.connect(host = "localhost", user = "root", password = "123456", database = "mysql", charset = "utf8mb4")

    # 创建指针对象
    cur_ser = db_ser.cursor()
    cur_show = db_show.cursor()

    # 清空表blog_mail和表blog_block
    cur_show.execute("TRUNCATE TABLE blog_mail;")
    cur_show.execute("TRUNCATE TABLE blog_block;")

    num = 0
    # 更新表blog_mail和表blog_block
    cur_ser.execute('SELECT * FROM blog_mail ORDER BY block_id ASC;')
    results_mail = cur_ser.fetchall()
    for result in results_mail:
        num = num + 1
        cur_show.execute("INSERT INTO blog_mail(block_id, text_id, text_hash, text)VALUES(%s, %s, %s, %s)", \
            (result[0], result[1], result[2], result[3]))

    cur_ser.execute('SELECT * FROM blog_block ORDER BY block_id ASC;')
    results_block = cur_ser.fetchall()
    for result in results_block:
        cur_show.execute("INSERT INTO blog_block(block_id, block_time, block_high, block_hash, block_text)VALUES(%s, %s, %s, %s, %s)", \
            (result[0], result[1], result[2], result[3], result[4]))

    # 关闭连接
    db_ser.commit()
    db_show.commit()
    cur_ser.close()
    cur_show.close()
    db_ser.close()
    db_show.close()

    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 28800))
    print('执行时间：' + t + '    现有数据：' + str(num) + '条' + "    ALL DONE!")
    return 0

def up_block(text = "/home/tra_sql/save/test.txt"):
    # 上传到IPFS服务器
    file_up = os.popen('ipfs add ' + text).read()
    up_list = file_up.split(' ')
    if len(up_list) >= 2:
        return up_list[1]
    else:
        print(file_up)
        return 'Sorry,Failed!'

def add_table():
    # 创建连接对象
    db_show = pymysql.connect(host = "localhost", user = "root", password = "123456", database = "mysql", charset = "utf8mb4")

    # 创建指针对象
    cur_show = db_show.cursor()

    # 取出表blog_block与表block_txt相差内容
    cur_show.execute("SELECT block_id, block_time, block_high, block_hash, block_text FROM blog_block \
        WHERE blog_block.block_id IN (SELECT block_id FROM blog_block LEFT JOIN \
        (SELECT block_id AS id FROM block_txt) AS tra \
        ON blog_block.block_id = tra.id where tra.id IS NULL);")

    results_block = cur_show.fetchall()
    for result in results_block:
        with open('/home/tra_sql/save/' + str(result[3]) + '.txt', 'w') as f:
            f.write('block_id:' + str(result[0]) + '\n')
            f.write('block_time:' + str(result[1]) + '\n')
            f.write('block_high:' + str(result[2]) + '\n')
            f.write('block_hash:' + str(result[3]) + '\n')
            f.write('block_text:' + str(result[4]) + '\n')
        file_hash = up_block('/home/tra_sql/save/' + str(result[3]) + '.txt')
        cur_show.execute("INSERT INTO block_txt(block_id, block_ipfs)VALUES(%s, %s)", (result[0], file_hash))

    db_show.commit()
    cur_show.close()
    db_show.close()

    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 28800))
    print('执行时间：' + t + '    新增数据：' + str(len(results_block)) + '条' + "    ALL DONE!")
    return 0

if __name__ == '__main__':
    copy_table()
    time.sleep(5)
    add_table()
