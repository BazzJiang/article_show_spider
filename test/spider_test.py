import unittest
from loguru import logger

from spider.article.oracle_article_spider import get_and_save_oracle_blog_article


class ConfigReadTest(unittest.TestCase):
    """
    oracle文章读取测试
    """
    def test_oracle_spider(self):
        logger.info("爬取oracle文章:")
        get_and_save_oracle_blog_article()