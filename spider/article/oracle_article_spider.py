import os

from bs4 import BeautifulSoup

from spider.util.spider_requests_client import send_get_request_by_proxy
from loguru import logger

# 文章列表页URL
oracle_blog_article_list_url = 'https://blogs.oracle.com/javamagazine/'

# 文章列表xpath
oracle_blog_article_section_selector = 'body > div.f11w1 > section.f19.f19v1.cpad > div > div > section > section > div'

# 文章详情页url
oracle_article_detail_url = 'https://blogs.oracle.com/javamagazine/{articleTitle}'


def get_and_save_oracle_blog_article():
    "获取并保存oracle文章列表"
    response, result = send_get_request_by_proxy(url=oracle_blog_article_list_url)
    if not response:
        logger.error('无法获取文章列表页信息!')
        return
    response_html = response.text
    parse_info_from_article_html_list_page(response_html)


def parse_info_from_article_html_list_page(htm_content):
    soup_list = BeautifulSoup(htm_content, 'html.parser')
    section_tag = soup_list.select(oracle_blog_article_section_selector)[0]
    for child_tag in section_tag.children:
        if child_tag.name == 'div':
            article_title_tag = child_tag.select('h4 > a[href]')[0]
            article_title = article_title_tag.string
            article_url = article_title_tag['href']
            article_author_tag = child_tag.select('div[class="cb136info"] > span')[0]
            article_author = article_author_tag.string
            article_label_tag = child_tag.select('div[class="cb136info"] > span')[1]
            article_label = article_label_tag.string
            article_summary_tag = child_tag.select('div[class="cb136copy"] > p')[0]
            article_summary = article_summary_tag.string
            logger.info("文章信息如下标题:{},url:{},作者:{},标签:{}摘要:{}", article_title, article_url, article_author,
                        article_label, article_summary)


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_path, '../..', 'webpage/oracle_blog_article.html')
    f = open(path, 'r', encoding='UTF-8')
    html_content = f.read()
    parse_info_from_article_html_list_page(html_content)
    f.close()
