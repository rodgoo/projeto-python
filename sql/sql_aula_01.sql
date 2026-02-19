USE cadastro_teste;

CREATE TABLE pessoas_teste (
id int NOT NULL AUTO_INCREMENT,
nome varchar(30) NOT NULL,
nascimento date NOT NULL,
sexo enum('M','F') NOT NULL,
peso decimal(5,2),
altura decimal(3,2),
nacionalidade varchar(20) DEFAULT 'América',
PRIMARY KEY (id)

) DEFAULT CHARSET = UTF8,
