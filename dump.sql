DROP DATABASE IF EXISTS todo_db;
CREATE DATABASE IF NOT EXISTS todo_db;
CREATE USER IF NOT EXISTS 'new_user'@'localhost' IDENTIFIED BY 'todolist';
GRANT ALL PRIVILEGES ON `todo_db`.* TO `new_user`@`localhost`;
FLUSH PRIVILEGES;

USE todo_db;
DROP TABLE IF EXISTS `lists`;
CREATE TABLE `lists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `todo` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
);

LOCK TABLES `lists` WRITE;
INSERT INTO `lists` (todo) VALUES ('Meeting'), ('Eat'), ('Fill forms'), ('Take out the trash'), ('Clean your room');
UNLOCK TABLES;