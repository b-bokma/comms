PRAGMA journal_mode = MEMORY;
PRAGMA synchronous = OFF;
PRAGMA foreign_keys = OFF;
PRAGMA ignore_check_constraints = OFF;
PRAGMA auto_vacuum = NONE;
PRAGMA secure_delete = OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS `Questions`;
CREATE TABLE `Questions` (
`id` INTEGER NULL  DEFAULT NULL,
`status_id` INTEGER NULL DEFAULT NULL,
`created_on` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`deadline` DATETIME NULL DEFAULT NULL,
`created_by` INTEGER NULL DEFAULT NULL,
`spokesperson_id` INTEGER NULL DEFAULT NULL,
`subject` TEXT NOT NULL DEFAULT 'NULL',
`question` MEDIUMTEXT NULL DEFAULT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`status_id`) REFERENCES `Status` (id),
FOREIGN KEY (`created_by`) REFERENCES `Users` (id),
FOREIGN KEY (`spokesperson_id`) REFERENCES `Spokespersons` (id) 
);

DROP TABLE IF EXISTS `Journalists`;
CREATE TABLE `Journalists` (
`id` INTEGER NULL  DEFAULT NULL,
`first_name` TEXT NULL DEFAULT NULL,
`middle_name` TEXT NULL DEFAULT NULL,
`last_name` TEXT NULL DEFAULT NULL,
PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `JournalistMediaMap`;
CREATE TABLE `JournalistMediaMap` (
`id` INTEGER NULL  DEFAULT NULL,
`journalist_id` INTEGER NULL DEFAULT NULL,
`media_id` INTEGER NULL DEFAULT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`journalist_id`) REFERENCES `Journalists` (id),
FOREIGN KEY (`media_id`) REFERENCES `Media` (id)
);

DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
`id` INTEGER NULL  DEFAULT NULL,
`email` TEXT NULL DEFAULT NULL,
`username` TEXT NULL DEFAULT NULL,
`first_name` TEXT NULL DEFAULT NULL,
`last_name` TEXT NULL DEFAULT NULL,
`hash` MEDIUMTEXT(128) NULL DEFAULT NULL,
PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `Spokespersons`;
CREATE TABLE `Spokespersons` (
`id` INTEGER NULL  DEFAULT NULL,
`title` TEXT NULL DEFAULT NULL,
`first_name` TEXT NULL DEFAULT NULL,
`middle_name` TEXT NULL DEFAULT NULL,
`last_name` TEXT NULL DEFAULT NULL,
PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `Status`;
CREATE TABLE `Status` (
`id` INTEGER NULL  DEFAULT NULL,
`status` TEXT NOT NULL DEFAULT 'NULL',
PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `Themes`;
CREATE TABLE `Themes` (
`id` INTEGER NULL  DEFAULT NULL,
`name` INTEGER NULL DEFAULT NULL,
PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `QuestionJournalistMap`;
CREATE TABLE `QuestionJournalistMap` (
`id` INTEGER NULL  DEFAULT NULL,
`question_id` INTEGER NOT NULL DEFAULT NULL,
`journalist_id` INTEGER NOT NULL DEFAULT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`question_id`) REFERENCES `Questions` (id),
FOREIGN KEY (`journalist_id`) REFERENCES `Journalists` (id)
);


DROP TABLE IF EXISTS `QuestionThemeMap`;
CREATE TABLE `QuestionThemeMap` (
`id` INTEGER NULL  DEFAULT NULL,
`question_id` INTEGER NULL DEFAULT NULL,
`theme_id` INTEGER NULL DEFAULT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`question_id`) REFERENCES `Questions` (id),
FOREIGN KEY (`theme_id`) REFERENCES `Themes` (id)
);

DROP TABLE IF EXISTS `Media`;
CREATE TABLE `Media` (
`id` INTEGER NULL  DEFAULT NULL,
`name` INTEGER NULL DEFAULT NULL,
`address` INTEGER NULL DEFAULT NULL,
`city` INTEGER NULL DEFAULT NULL,
PRIMARY KEY (`id`)
);

COMMIT;
PRAGMA ignore_check_constraints = ON;
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
