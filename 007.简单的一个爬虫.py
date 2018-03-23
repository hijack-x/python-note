#!/bin/python3

# -*- coding: utf-8 -*-

import urllib.request
import re
import time
import os
import threading


def download(url):
    resp = urllib.request.urlopen(url)
    return resp.read()


def findAllLinks(data, refUrl):
    data = data.decode('utf-8')
    searchObj = re.search('(http(s)?)://[^/]+', refUrl)
    baseUrl = searchObj.group()
    schema = searchObj.groups(1)[0]
    pos = refUrl.rfind('/')
    if pos == -1:
        parentUrl = refUrl
    else:
        parentUrl = refUrl[0:pos]
    all = re.findall('<a[\S ]+?href="([^"]+?)"[\S ]+?>[\s\S]+?</a>', data)
    links = []
    for val in all:
        if val.startswith('javascript:'):
            continue
        elif val.startswith('http://') or val.startswith('https://'):
            links.append(val)
        elif val.startswith('//'):
            links.append(schema + ':' + val)
        elif val.startswith('/'):
            links.append(baseUrl + val)
        else:
            links.append(parentUrl + '/' + val)
    return links


def url2path(url):
    arr = url.split('://')
    filename = arr[1]
    pos = filename.rfind('?')
    if pos != -1:
        filename = filename[0:pos]
    pos = filename.rfind('#')
    if pos != -1:
        filename = filename[0:pos]
    if filename.rfind('/') == -1:
        filename += '/'
    if filename.endswith('/'):
        filename += 'index.html'
    return filename


def writeFile(filename, data):
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    file = open(filename, 'wb')
    file.write(data)
    file.close()


def doJob(url):
    filename = url2path(url)
    fullPath = os.path.join(savePath, filename)

    print('begin download', url, '...')
    try:
        data = download(url)
        writeFile(fullPath, data)
        print('save to', fullPath)
    except BaseException as e:
        print('download or save fail', e)

    time.sleep(0.05)


class MyThread(threading.Thread):
    def __init__(self, threadNum, links, idx):
        threading.Thread.__init__(self)
        self.threadNum = threadNum
        self.links = links
        self.idx = idx
        self.count = 0

    def run(self):
        for i in range(self.idx, len(self.links), self.threadNum):
            link = self.links[i]
            doJob(link)
            # print(link, self.idx, i)


url = 'http://www.runoob.com/python3/python3-tutorial.html'
savePath = 'd:/download/'

data = download(url)
links = findAllLinks(data, url)


threads = []
threadNum = 4
for i in range(threadNum):
    thread = MyThread(threadNum, links, i)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('All done!')
