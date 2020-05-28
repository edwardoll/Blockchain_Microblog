# 定时执行
# Postgresql的mastodon_production数据库的表
# statuses【id text account_id created_at】
# accounts【username id】
# status_stats【status_id favourites_count reblogs_count】

# blog_list【text_id account_name created_time text】
# blog_old【text_id account_name created_time text】
# blog_update【text_id account_name created_time text number】

# MySQL的mysql数据库的表
# blog_pre【text_id account_name created_time text number】
# blog_result【block_id text_id account_name created_time text number state
# favourite reblog】
# blog_block【block_id block_time block_high block_hash block_text】

import psycopg2
import pymysql
import time

# 创建连接对象
conn = psycopg2.connect(database = "mastodon_production", user = "postgres", password = "", host = "localhost", port = "5432")
db = pymysql.connect(host = "localhost", user = "root", password = "123456", database = "mysql", charset = "utf8mb4")

# 创建指针对象
cur_pg = conn.cursor()
cur_my = db.cursor()

# 在mastodon_production数据库中
# 根据表statuses与表accounts更新表blog_list
cur_pg.execute("INSERT INTO blog_list(text_id, account_name, created_time, text) \
    SELECT statuses.id AS text_id, accounts.username AS account_name, statuses.created_at AS created_time, statuses.text AS text \
    FROM statuses INNER JOIN accounts ON (statuses.account_id = accounts.id);")
# 将表blog_list与表blog_old对比，相差内容编号后放入表blog_update
cur_pg.execute("INSERT INTO blog_update(text_id, account_name, created_time, text) \
    SELECT text_id, account_name, created_time, text FROM blog_list \
    WHERE blog_list.text_id IN (SELECT text_id FROM blog_list LEFT JOIN \
    (SELECT text_id AS id FROM blog_old) AS tra \
    ON blog_list.text_id = tra.id where tra.id IS NULL);")
cur_pg.execute('SELECT * FROM blog_update ORDER BY text_id ASC;')
results_num = cur_pg.fetchall()
for i in range(len(results_num)):
    cur_pg.execute("UPDATE blog_update SET number = %s WHERE blog_update.text_id = %s;", (i + 1, results_num[i][0]))
# 将表blog_old与表blog_list同步
cur_pg.execute("TRUNCATE TABLE blog_old RESTART IDENTITY;")
cur_pg.execute("INSERT INTO blog_old SELECT * FROM blog_list;")
# 清空表blog_list
cur_pg.execute("TRUNCATE TABLE blog_list RESTART IDENTITY;")

# 将mastodon_production数据库中的表blog_update传入mysql数据库中的表blog_pre
cur_pg.execute('SELECT * FROM blog_update ORDER BY text_id ASC;')
results_tra = cur_pg.fetchall()
for result in results_tra:
    cur_my.execute("INSERT INTO blog_pre(text_id, account_name, created_time, text, number)VALUES(%s, %s, %s, %s, %s)", \
        (result[0], result[1], result[2], result[3], result[4]))

# 清空mastodon_production数据库中的表blog_update
cur_pg.execute("TRUNCATE TABLE blog_update RESTART IDENTITY;")

# 在mysql数据库中
# 将表blog_pre添加至表blog_result
cur_my.execute("ALTER TABLE blog_result AUTO_INCREMENT = 1;")
cur_my.execute("INSERT INTO blog_result(text_id, account_name, created_time, text, number) \
    SELECT text_id, account_name, created_time, text, number FROM blog_pre \
    WHERE blog_pre.text_id IN (SELECT text_id FROM blog_pre LEFT JOIN \
    (SELECT text_id AS id FROM blog_result) AS tra \
    ON blog_pre.text_id = tra.id where tra.id IS NULL);")
# 清空表blog_pre
cur_my.execute("truncate table blog_pre;")

# 将表blog_result的点赞数和转发数与表status_stats同步
cur_pg.execute('SELECT status_id, favourites_count, reblogs_count FROM status_stats;')
results_con = cur_pg.fetchall()
for con in results_con:
    cur_my.execute("UPDATE blog_result SET favourite = %s, reblog = %s WHERE blog_result.text_id = %s AND blog_result.state = 0;", (con[1], con[2], con[0]))

# 关闭连接
conn.commit()
db.commit()
cur_pg.close()
cur_my.close()
conn.close()
db.close()

t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 28800))
print('执行时间：' + t + '    新增数据：' + str(len(results_num)) + '条' + "    ALL DONE!")
