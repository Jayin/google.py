# -*- coding: utf-8 -*-
__author__ = 'jayin'

import requests
import codecs
import json
import threading
import sys
import os
from threadpool import ThreadPool, makeRequests
import urllib


lock = threading.Lock()
pool = ThreadPool(8)
finish = False
ok_url = ''
keyword = None
ips_file = os.path.join(os.path.dirname(__file__),'data/ips.json')

if len(sys.argv) > 1:
    keyword = ' '.join(sys.argv[1:])

if keyword is not None:
    tpl_url = u'http://{ip}/search?q=' + urllib.quote(keyword)
else:
    tpl_url = u'http://{ip}'

with codecs.open(ips_file) as f:
    _ips = f.read()

ips = json.loads(_ips)


def ping(url):
    global finish, ok_url
    try:
        print('-->%s' % url)
        res = requests.head(url, timeout=2)
        if finish:
            return
        if res.status_code == 200:
            finish = True
            ok_url = url
        else:
            print('%s is block!' % url)
    except Exception as e:
        pass


def callback(res, err):
    if finish:
        print('%s is ok' % ok_url)
        os.system('open %s' % ok_url)
        sys.exit()


def main():
    worker_requests = makeRequests(ping, [tpl_url.format(ip=ip) for ip in ips], callback=callback)

    for req in worker_requests:
        pool.putRequest(req)
    try:
        pool.wait()
        print('已经尝试所有ip，均失败，请重试')
    except Exception as e:
        print(e)


