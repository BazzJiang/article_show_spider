import base64
from hashlib import sha1
import hmac


def is_blank(input_str):
    """
    判断字符串是否为空
    :param input_str:输入字符串
    :return:
    """
    if input_str in (None, '') or not input_str.strip():
        return True
    else:
        return False


def safe_base64_encode(message):
    """
    base64编码工具类
    :param message:
    :return:
    """
    message_bytes = message.encode('UTF-8')
    base64_byte = base64.b64encode(message_bytes)
    base64_message = base64_byte.decode('UTF-8')
    return base64_message.replace('+', '-').replace('/', '_')


def hamcsha1(policy_data, secret_key):
    """
    hamcsha1前面算法
    :param policy_data:数据
    :param secret_key:密钥
    :return:返回十六进制的加密结果
    """
    hashed = hmac.new(secret_key.encode("UTF-8"), policy_data.encode("UTF-8"), sha1)
    hex_str = hashed.hexdigest().upper()
    return hex_str


def format_list(list):
    """
    将list转化为可打印格式
    :param list:
    """
    return ' '.join(str(e) for e in list)

