#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import Queue
import threading
import requests
import os
import time


class ThreadPool():
    # 线程池管理器
    def __init__(self, thread_num):
        # 初始化参数
        self.work_queue = Queue.Queue()
        self.thread_num = thread_num
        self.__init_threading_pool(self.thread_num)

    def __init_threading_pool(self, thread_num):
        # 初始化线程池，创建指定数量的线程池
        for i in range(thread_num):
            thread = Thread(self.work_queue)
            thread.start()

    def add_job(self, func, *args):
        # 将任务放入队列，等待线程池阻塞读取，参数是被执行的函数和函数的参数
        self.work_queue.put((func, args))


class Thread(threading.Thread):
    # 定义线程类，继承threading.Thread
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        # 线程守护使用上要注意主线程所在（next_net_page这个方法是递归翻页所以在第一次递归就结束了，在此就不开启线程守护）
        # self.daemon = True

    def run(self):
        # 启动线程
        while True:
            time.sleep(2)
            target, args = self.work_queue.get()
            target(*args)
            self.work_queue.task_done()


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
        # print u"下载成功"
        count[0] = count[0] + 1
        print count[0]
        open(path, 'wb').write(ir.content)


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
                print exception
        next_page(a['href'], 0, base_path)


def next_net_page(i=0):
    url = "https://www.mzitu.com/tag/ugirls/"
    if i > 0:
        url = "https://www.mzitu.com/tag/ugirls/page/%s/" % (i)

    response = requests.post(url=url)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'lxml')
        all_a = soup.select('.postlist ul li>a')
        next_net_page(i + 1)
        for a in all_a:
            # args: 线程执行方法接收的参数，该属性是一个元组，如果只有一个参数也需要在末尾加逗号。
            thread_pool.add_job(theme_to_page, *(a,))


thread_pool = ThreadPool(50)
count = []
count.append(0)
next_net_page()
