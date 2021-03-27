# -*- coding: utf-8 -*-
"""python3提取api链接并使用requests库进行http代理"""
import base64
import random

import requests
from loguru import logger

def get_proxy(proxy_config):
    """
    获取代理
    :return:
    """
    orderid = proxy_config['orderid']
    password = proxy_config['proxyPassword']
    username = proxy_config['proxyUsername']
    api_url = 'http://kps.kdlapi.com/api/getkps?orderid=%(orderid)s&num=1&pt=1&format=json&sep=1' % {'orderid': orderid}
    proxy_ip = requests.get(api_url).json()['data']['proxy_list']
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)},
        "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)}
    }
    data_str = "%(user)s:%(pwd)s" % {'user': username, 'pwd': password}
    proxy_token = 'Basic ' + base64.b64encode(bytes(data_str, encoding='utf-8')).decode('utf-8')
    # 测试代理是否可用
    test_request_proxy(proxies, proxy_token)
    return proxies, proxy_token


def test_request_proxy(proxies, proxy_token):
    """
    request测试代理可用性
    :return:
    """
    # 测试URL
    page_url = "http://dev.kdlapi.com/testproxy"
    headers={}
    headers['Accept-Encoding'] = 'Gzip'
    headers['Proxy-Authorization'] = proxy_token
    response = requests.get(page_url, proxies=proxies, headers=headers)
    if response.status_code == 200:
        logger.info("已连接至快代理:{}!", proxy_token)
    else:
        logger.error("快代理不可用!")
        exit(1)
