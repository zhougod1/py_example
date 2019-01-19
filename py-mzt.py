#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import threading
import requests
import os

# python规定所有在赋值语句左面的变量都是局部变量（闭包规则）
# def a():
#     v = 1
#     def b():
#         v = v + 1 #会报赋值引用错误v已经变成了b中的v所以不能边赋值边引用


# 下载方法，手动拼接请求头，妹子图有做一层简单的反爬
def dowload_img(filePath, url):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'referer':
        'https://www.mzitu.com/'
    }
    # proxies=proxies
    ir = requests.get(url, headers=headers)
    name = os.path.basename(url)
    suffix = os.path.splitext(url)[1]
    path = filePath + os.sep + name + suffix
    if ir.status_code == 200:
        print u"下载成功"
        open(path, 'wb').write(ir.content).close()


# 每页请求成功后自动累加，实现翻页功能，直到请求不到网页（后期加入多线程提高效率）
def next_page(url, index, filePath):
    uri = url
    if index > 0:
        uri = uri + '/' + str(index)
    pr = requests.post(uri)

    if pr.status_code == 200:
        sc = BeautifulSoup(pr.content, 'lxml')
        current = sc.select('.main-image p a img')
        dowload_img(filePath, current[0]['src'])
        next_page(url, index + 1, filePath)


def theme_to_page(a):
    name = a.contents[0]['alt']
    base_path = "d:\\download\\crawler\\" + name

    if name != '':
        if not os.path.exists(base_path):
            try:
                os.makedirs(base_path)
            except (IOError, OSError) as exception:
                pass
        next_page(a['href'], 0, base_path)


response = requests.post("https://www.mzitu.com/tag/ugirls/")
html = response.content
soup = BeautifulSoup(html, 'lxml')
all_a = soup.select('.postlist ul li>a')
threads = []

for a in all_a:
    # args: 线程执行方法接收的参数，该属性是一个元组，如果只有一个参数也需要在末尾加逗号。
    t = threading.Thread(target=theme_to_page, args=(a,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
