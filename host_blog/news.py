from bs4 import BeautifulSoup
import requests
import jieba.analyse

# 按顺序爬取新闻
def get_links(page_url, word):
    if word != None:
        page_url = page_url + '?s=' + word
    try:
        html_doc = requests.get(page_url).content.decode()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)
        return 0
    page_soup = BeautifulSoup(html_doc, 'html.parser')
    if word != None:
        page_links = page_soup.find('div', id = 'wrap').find('div', attrs = {'class':'wrap container'}).find('div', attrs = {'class':'main'}).find_all('a')
    else:
        page_links = page_soup.find('div', id = 'wrap').find('div', attrs = {'class':'container wrap'}).find('div', attrs = {'class':'main'}).find_all('a')
    url_list = []
    for link in page_links:
        url = link.get('href')
        url_list.append(url)
    url_list = list(set(list(filter(lambda url_str: ('http' in url_str and 'zixun' in url_str and 'page' not in url_str), url_list))))
    url_list.sort()
    if 'https://www.lianyi.com/zixun/' in url_list:
        url_list.remove('https://www.lianyi.com/zixun/')
    elif 'https://www.lianyi.com/zixun' in url_list:
        url_list.remove('https://www.lianyi.com/zixun')
    else:
        pass
    return url_list

# 获取新闻内容，包括标题、信息、正文
def get_art(art_url):
    try:
        html_doc = requests.get(art_url).content.decode()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)
        return 0
    art_soup = BeautifulSoup(html_doc, 'html.parser')
    art_links = art_soup.find('div', id = 'wrap').find('div', attrs = {'class':'wrap container'}).find('div', attrs = {'class':'main'}).find('article').find('div', attrs = {'class':'entry'})
    art_title = art_links.find('div', attrs = {'class':'entry-head'}).find('h1', attrs = {'class':'entry-title'}).text.replace('\n', '')
    art_info = art_links.find('div', attrs = {'class':'entry-head'}).find('div', attrs = {'class':'entry-info'}).text.replace('\n', ' ')[1:]
    art_content = art_links.find('div', attrs = {'class':'entry-content clearfix'}).text.replace('\r', '').replace('\xa0', '').replace('\t', '').split('\n')
    art_content = [art for art in art_content if (art != '' and art != ' ')]
    if len(art_content) >= 2:
        art_content[-2] = art_content[-2].replace(' ', '')
        art_content[-1] = art_content[-1].replace(' ', '')
    art_result = {}
    art_result['title'] = art_title
    art_result['info'] = art_info
    art_result['content'] = art_content
    return art_result

# 提取新闻关键词
def get_key(article):
    need = 5 #关键词数量
    data = article['title']
    for p in article['content']:
        data = data + p
    key_list = []
    for keyword, weight in jieba.analyse.extract_tags(data, topK = need, withWeight = True):
        key_list.append(keyword)
    return key_list

# 新闻爬虫
def get_news(page_num, list_num, word = None):
    page_url = 'https://www.lianyi.com/zixun/page/' + str(page_num)
    url_list = get_links(page_url, word)
    if list_num > len(url_list) - 1:
        list_num = len(url_list) - 1
        print('请输入数字：0-' + str(len(url_list) - 1))
    show_article = get_art(url_list[list_num])
    show_article['link'] = url_list[list_num]
    show_article['keywords'] = get_key(show_article)
    print('新闻标题：', show_article['title'])
    print('新闻信息：', show_article['info'])
    print('新闻内容：', show_article['content'])
    print('新闻关键词：', show_article['keywords'])
    print('新闻链接：', show_article['link'])
    return 0

if __name__ == '__main__':
    # 第几页
    page = 2
    # 第几条
    num = 4
    # 搜索关键词，可不填
    key = '比特币'
    a = get_news(page, num, key)
    print(a)
    b = get_news(2, 2)
    print(b)
