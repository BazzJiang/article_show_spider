"""
定义统一的全局变量
"""
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from spider.common.read_config import ReadConfig
from spider.common.proxy import get_proxy

__all__ = ['app_config', 'Session']

# 爬虫配置读取
from spider.db.mysql_connection import get_mysql_connection

app_config = ReadConfig()

# 创建Scope Session
_engine = get_mysql_connection(app_config.db_config)
Session = scoped_session(sessionmaker(bind=_engine, expire_on_commit=False))

# 快代理
# (proxies, proxy_token) = get_proxy(app_config.proxy_config)

# 公司代理
# proxies = {
#     "http": "http://{}:{}".format('100.69.146.4', '9443'),
#     "https": "https://{}:{}".format('100.69.146.4', '9443')
# }
