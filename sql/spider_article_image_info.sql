DROP TABLE IF EXISTS `spider_article_image_info`;
CREATE TABLE `spider_article_image_info` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `article_id` INT(11) NOT NULL COMMENT '关联文章id',
  `name` VARCHAR(256) DEFAULT '' COMMENT '图片名称',
  `size` INT(11) DEFAULT '' COMMENT '图片大小',
  `source_url` VARCHAR(256) DEFAULT '' COMMENT '源地址',
  `publish_time` VARCHAR(24) DEFAULT '' COMMENT '发表时间',
  `md5` CHAR(32) DEFAULT '' COMMENT '图片md5值',
  `attach_ext` VARCHAR(10) DEFAULT NULL COMMENT '附件扩展名',
  `attach_id` VARCHAR(100) DEFAULT NULL COMMENT '文件系统的附件id',
  `attach_url` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '附件URL',
  `attach_md5` CHAR(32) NOT NULL DEFAULT '' COMMENT '附件MD5',
  `attach_batch_order` TINYINT(4) NOT NULL DEFAULT '0' COMMENT '附件批次顺序',
  `attach_status` TINYINT(4) NOT NULL DEFAULT '1' COMMENT '附件状态',
  `create_by` VARCHAR(24) NOT NULL DEFAULT '' COMMENT '创建人',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `update_by` VARCHAR(24) NOT NULL DEFAULT '' COMMENT '更新人',
  `update_time` TIMESTAMP DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8bin COMMENT='oracle博客文章表';