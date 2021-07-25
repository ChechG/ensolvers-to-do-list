/*DROP DATABASE IF EXISTS todo_db;
CREATE DATABASE IF NOT EXISTS todo_db;
CREATE USER IF NOT EXISTS 'new_user'@'localhost' IDENTIFIED BY 'todolist';
GRANT ALL PRIVILEGES ON `todo_db`.* TO `new_user`@`localhost`;
FLUSH PRIVILEGES;*/

USE todo_db;
DROP TABLE IF EXISTS `folders`;
CREATE TABLE `folders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `lists`;
CREATE TABLE `lists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `todo` varchar(128) NOT NULL,
  `id_folder` int NOT NULL,
  PRIMARY KEY (`id`)
);

/*DROP TABLE IF EXISTS `ej`;
CREATE TABLE `ej` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ej_uno` varchar(128) NOT NULL,
  `ej_dos` int NOT NULL,
  PRIMARY KEY (`id`)
);

LOCK TABLES `ej` WRITE;
INSERT INTO `ej` (ej_uno, ej_dos) VALUES ("funca bebe", 35);
UNLOCK TABLES;*/

LOCK TABLES `folders` WRITE;
INSERT INTO `folders` (name) VALUES ('Work'), ('Daily Tasks');
UNLOCK TABLES;

LOCK TABLES `lists` WRITE;
INSERT INTO `lists` (todo, id_folder) VALUES ('Meeting', 1), ('Eat', 2), ('Fill forms', 1), ('Take out the trash', 2), ('Clean your room', 2);
UNLOCK TABLES;