CREATE DATABASE loja_do_ryan

USE loja_do_ryan;

CREATE TABLE ryan_vendasa (
id int NOT NULL AUTO_INCREMENT,
nome varchar(30) NOT NULL,
nascimento date NOT NULL,
sexo enum('M','F') NOT NULL,
peso decimal(5,2),
altura decimal(3,2),
nacionalidade varchar(20) DEFAULT 'América',
PRIMARY KEY (id)

) DEFAULT CHARSET = UTF8;

INSERT INTO loja_do_ryan.ryan_vendasa
(nome, nascimento, sexo, peso, altura, nacionalidade) VALUES
('Ryan','2005-03-24','F','70','1.80','Brasileiro')

SELECT nome, sexo from ryan_vendasa