import urllib.request
import traceback
import socket


def check_url_connected(url):
    """
    测试URL是否联通
    """
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    try:
        host = socket.gethostbyname(url)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


if __name__ == "__main__":
    print('能否连接百度:' + str(check_url_connected("https://www.baidu.com")))
    print('能否连接谷歌:' + str(check_url_connected("https://www.google.com")))
    print('能否连接COS:' + str(check_url_connected("https://cos-di1.dev.cmrh.com")))
