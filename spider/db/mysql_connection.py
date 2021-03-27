import traceback

import sqlalchemy
from loguru import logger


def __connect_mysql_by_usr_pwd(username, password, database, host, port):
    """
    根据用户名和密码创建Mysql数据库连接
    :param username:用户名
    :param password:密码
    :param database:数据库名称
    :param host:主机
    :param port:端口
    :return:
    """
    url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'
    url = url.format(username, password, host, port, database)
    try:
        engine = sqlalchemy.create_engine(url)
        meta = sqlalchemy.MetaData(bind=engine)
        logger.info('MySQL数据库{}连接成功!', host)
        return engine, meta
    except Exception as e:
        traceback.print_exc()
        logger.error("MySQL数据库连接失败:{}!", str(e))
        exit(1)


def get_pg_connection(db_config):
    """
    返回数据库连接
    :return:
    """
    database = db_config['database']
    username = db_config['username']
    password = db_config['password']
    host = db_config['host']
    port = db_config['port']
    engine, meta = __connect_mysql_by_usr_pwd(username=username, password=password, database=database, host=host,
                                              port=port)
    return engine


if __name__ == '__main__':
    "测试数据库是否能够正常连接"
    db_config = {
        'database': 'article_spider_dev',
        'username': 'root',
        'password': 'jiangke1994',
        'host': 'rm-bp15wzk7gpro3c2d3lo.mysql.rds.aliyuncs.com',
        'port': '3306',
    }
    get_pg_connection(db_config)
