DROP TABLE IF EXISTS `spider_oracle_blog_article`;
CREATE TABLE `spider_oracle_blog_article` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `title` VARCHAR(256) DEFAULT '' COMMENT '文章标题',
  `author` VARCHAR(24) DEFAULT '' COMMENT '文章作者',
  `tags` VARCHAR(100) DEFAULT '' COMMENT '文章标签',
  `summary` VARCHAR(256) DEFAULT '' COMMENT '文章摘要',
  `page_html_content` TEXT COMMENT '文章整个网页html内容',
  `article_html_content` TEXT COMMENT '文章html内容',
  `article_txt_content` TEXT COMMENT '文章html内容',
  `source_website` VARCHAR(24) DEFAULT '' COMMENT '源网站',
  `source_url` VARCHAR(500) DEFAULT '' COMMENT '源地址',
  `publish_time` VARCHAR(24) DEFAULT '' COMMENT '发表时间',
  `create_by` VARCHAR(24) NOT NULL DEFAULT '' COMMENT '创建人',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `update_by` VARCHAR(24) NOT NULL DEFAULT '' COMMENT '更新人',
  `update_time` TIMESTAMP NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='oracle博客文章表';