# 定时执行
# MySQL的mysql数据库的表
# blog_result【block_id text_id account_name created_time text number state
# favourite reblog】
# blog_mail【block_id text_id text_hash text】
# blog_block【block_id block_time block_high block_hash block_text】

import pymysql
import time
import hashlib
import os
import requests
import json

def clear_str(text):
    text = text.replace('─', '').replace('┤', '').replace('┼', '').replace('│', '').replace('├', '')
    text = text.replace('┘', '').replace('└', '').replace('┐', '').replace('┌', '').replace('┴', '').replace('┬', '').replace(' ', '').replace(',', '')
    text = text.replace('\x1b[2K', '').replace('\x1b[1G', '').replace('\x1b[90m', '').replace('\x1b[39m', '').replace('\n\n', '\n')
    return text

def get_dic(text):
    result = text.split('\n')
    dic_pre = {}
    for re in result:
        if ':' in re:
            ss = re.split(":")
            key = ss[0]
            value = re[len(ss[0]) + 1:]
            dic_pre[key] = value
    return dic_pre

def up_block(text = "NoMessageInput!"):
    # 上传区块链
    title = 'symbol-cli transaction '
    trans_info = 'transfer --profile testsend -p 12345678 -f 1000000 --sync --announce -c "@symbol.xym::1000000" '
    trans_reci = '-r TCYMKI-FJPQIA-DNYVZ5-XJEDOG-ALL3HY-57L4ZU-NEBC -m ' + text
    trans_com = 'info -h '
    trans_push = clear_str(os.popen(title + trans_info + trans_reci).read())
    #print(trans_push)
    dic_push = get_dic(trans_push)
    #print(dic_push)
    hash_info = dic_push['Hash']
    trans_get = clear_str(os.popen(title + trans_com + hash_info).read())
    #print(trans_get)
    dic_get = get_dic(trans_get)
    #print(dic_get)
    return dic_get['Hash'], dic_get['Height(Block)'], dic_get['Message']

# 创建连接对象
db = pymysql.connect(host = "localhost", user = "root", password = "123456", database = "mysql", charset = "utf8mb4")

# 创建指针对象
cur_my = db.cursor()

cur_my.execute('SELECT * FROM blog_result WHERE blog_result.block_id IN \
    (SELECT block_id FROM blog_result LEFT JOIN (SELECT block_id AS id FROM blog_mail) \
    AS tra ON blog_result.block_id = tra.id where tra.id IS NULL);')
num = 0
results_num = cur_my.fetchall()
for result in results_num:
    if result[6] == 0 and result[7] >= 1 and result[8] >= 1:
        pre_mdtext = str(result[2]) + '/' + str(result[3]) + '/' + str(result[4])
        #print(pre_mdtext)
        # 初步加密
        aft_mdtext = hashlib.md5(pre_mdtext.encode("utf-8")).hexdigest()
        #print(aft_mdtext)
        num = num + 1
        cur_my.execute("INSERT INTO blog_mail(block_id, text_id, text_hash, text)VALUES(%s, %s, %s, %s);", (result[0], result[1], aft_mdtext, pre_mdtext))
        input_text = aft_mdtext.replace(' ', '') + '/' + pre_mdtext.replace(' ', '')
        if len(input_text) > 500:
            input_text = input_text[0:500]
        f_block_hash, f_block_high, f_block_text = up_block(input_text)
        # 调用API方法
        nem_api = 'http://api-02.ap-northeast-1.0941-v1.symboldev.network:3000/block/' + f_block_high
        re_info = requests.get(nem_api)
        re_json = json.loads(re_info.text)
        f_block_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(re_json['block']['timestamp']) / 1000 + 1573430400 + 28800))
        cur_my.execute("INSERT INTO blog_block(block_id, block_time, block_high, block_hash, block_text)VALUES(%s, %s, %s, %s, %s);", (result[0], f_block_time, f_block_high, f_block_hash, f_block_text))
        cur_my.execute("UPDATE blog_result SET state = %s WHERE blog_result.block_id = %s;", (1, result[0]))

# 关闭连接
db.commit()
cur_my.close()
db.close()

t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 28800))
print('执行时间：' + t + '    新增数据：' + str(num) + '条' + "    ALL DONE!")
