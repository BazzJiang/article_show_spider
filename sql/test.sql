DROP TABLE IF EXISTS `test`;
CREATE TABLE `test`(
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
    `code` VARCHAR(24) NOT NULL DEFAULT '' COMMENT '代码',
    PRIMARY KEY (`id`)
);