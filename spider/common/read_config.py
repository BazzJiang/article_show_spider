import os
from configparser import RawConfigParser

from loguru import logger


class ReadConfig:
    """
    配置文件读取
    """
    def __init__(self):
        config = RawConfigParser()
        env = str(os.environ.get('APP_ENV', 'prd'))
        current_path = os.path.dirname(os.path.realpath(__file__))
        if env == 'dev':
            logger.info('正在激活dev配置文件crawler_conf_dev.ini')
            config.read(os.path.join(current_path, '../..', 'resources/crawler_conf_dev.ini'))
            self.config=config
        elif env == 'prd':
            logger.info('正在激活prd配置文件crawler_conf_prd.ini')
            config.read(os.path.join(current_path, '../..', 'resources/crawler_conf_prd.ini'))
            self.config = config
        else:
            logger.error('无法识别当前配置文件，启动失败!')
            exit(1)
        self.db_config = self.__read_db_config()
        self.cos_config = self.__read_cos_config()
        self.log_config = self.__read_log_config()
        self.proxy_config = self.__read_proxy_config()

    def __read_db_config(self):
        """
        读取DB配置
        :return:
        """
        db_config = {}
        db_config['database'] = self.config['PostgreSQL']['database']
        db_config['host'] = self.config['PostgreSQL']['host']
        db_config['port'] = self.config['PostgreSQL']['port']
        db_config['username'] = self.config['PostgreSQL']['username']
        db_config['password'] = self.config['PostgreSQL']['password']
        return db_config

    def __read_cos_config(self):
        """
        读取cos配置
        :return:
        """
        cos_config = {}
        cos_config['accessKey'] = self.config['Cos']['accessKey']
        cos_config['secretKey'] = self.config['Cos']['secretKey']
        cos_config['systemUrl'] = self.config['Cos']['systemUrl']
        cos_config['bucketName'] = self.config['Cos']['bucketName']
        return cos_config

    def __read_log_config(self):
        """
        读取日志配置
        :return:
        """
        log_config={}
        log_config['Log'] = self.config['Log']['logPath']
        return log_config

    def __read_proxy_config(self):
        """
        读取代理配置
        :return:
        """
        proxy_config = {}
        proxy_config['proxyUsername'] = self.config['Proxy']['proxyUsername']
        proxy_config['proxyPassword'] = self.config['Proxy']['proxyPassword']
        proxy_config['orderid'] = self.config['Proxy']['orderid']
        return proxy_config
