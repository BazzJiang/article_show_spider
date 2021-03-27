"""
对request库的封装
"""
import requests
import urllib3
import time
from loguru import logger
from spider.common.global_var import proxies, proxy_token
import traceback


accept_encoding = 'Gzip'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'


def send_post_request_by_proxy(url, data=None, headers=None, verify=True):
    """
    发送post请求
    :return:
    """
    time.sleep(1)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    if headers is None:
        headers = {}
    headers['Accept-Encoding'] = 'Gzip'
    headers['Proxy-Authorization'] = proxy_token
    headers['User-Agent'] = user_agent
    response = requests.post(url=url,data=data,proxies=proxies, headers=headers, verify=verify)
    return response


def send_get_request_by_proxy(url, params=None, headers=None, verify=True):
    """
    通过代理发送发送GET请求
    """
    time.sleep(1)
    if headers is None:
        headers = {}
    headers['Accept-Encoding'] = 'Gzip'
    headers['Proxy-Authorization'] = proxy_token
    headers['User-Agent'] = user_agent
    try:
        response = requests.get(url, params=params, proxies=proxies, headers=headers, verify=verify,timeout=300)
        return response, True
    except:
        traceback.print_exc()
        logger.info('无法打开URL{}，此URL跳过', url)
        return None, False


