CREATE TABLE `pessoas_partido` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`nome` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci,
	`cpf` VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
	`email` VARCHAR(80) CHARACTER SET utf8 COLLATE utf8_general_ci,
	`data_insercao` TIMESTAMP,
	`data_ultima_atualizacao` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	`telefone` VARCHAR(80),
	`ip` VARCHAR(70),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


CREATE TABLE `pessoas_partido_historico` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`nome` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci,
	`cpf` VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_general_ci,
	`email` VARCHAR(80) CHARACTER SET utf8 COLLATE utf8_general_ci,
	`data_atualizacao` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	`telefone` VARCHAR(80),
	`ip` VARCHAR(70),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;


INSERT INTO `coleta`.`pessoas_partido` (`nome`, `cpf`, `email`, `data_insercao`, `data_ultima_atualizacao`, `telefone`) VALUES ('Josefino da Silva Andrade', '04411786675', 'josefino@gmail.com', '2023-07-16 15:49:37', '2023-07-16 15:49:37', '(31)31313-3131');
INSERT INTO `coleta`.`pessoas_partido` (`nome`, `cpf`, `email`, `data_insercao`, `data_ultima_atualizacao`, `telefone`) VALUES ('Luciene Alves', '28973666367', 'luci.alves@hotmail.com', '2023-07-16 15:49:37', '2023-07-16 15:49:37', '(61)99999-3021');
INSERT INTO `coleta`.`pessoas_partido` (`nome`, `cpf`, `email`, `data_insercao`, `data_ultima_atualizacao`, `telefone`) VALUES ('Kayke Andrade', '45808735369', 'kaka@mdb.com.br', '2023-07-16 15:49:37', '2023-07-16 15:49:37', '(61)98735-8888');
