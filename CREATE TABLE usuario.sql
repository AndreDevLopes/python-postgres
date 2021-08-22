CREATE TABLE usuario (
    id  char(5) CONSTRAINT pk_id PRIMARY KEY,
    nome     varchar(40) NOT NULL,
    email    varchar(40) NOT NULL,
    senha    varchar(40) NOT NULL
);