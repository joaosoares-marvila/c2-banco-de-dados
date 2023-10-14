/* -------------- Apaga os relacionamentos -------------- */
ALTER TABLE sys.PRODUTOS_MERCADOS DROP CONSTRAINT PRODUTOS_MERCADOS_PRODUTOS_FK;
ALTER TABLE sys.PRODUTOS_MERCADOS DROP CONSTRAINT PRODUTOS_MERCADOS_MERCADOS_FK;
ALTER TABLE sys.PRODUTOS_CARRINHO DROP CONSTRAINT PRODUTOS_CARRINHO_PRODUTOS_MERCADOS_FK;


/* -------------- Apaga as tabelas -------------- */
DROP TABLE sys.MERCADOS;
DROP TABLE sys.PRODUTOS;
DROP TABLE sys.PRODUTOS_MERCADOS;
DROP TABLE sys.PRODUTOS_CARRINHO;


/* -------------- Apaga as sequences -------------- */
DROP SEQUENCE sys.MERCADOS_CODIGO_MERCADO_SEQ;
DROP SEQUENCE sys.PRODUTOS_CODIGO_PRODUTO_SEQ;
DROP SEQUENCE sys.PRODUTOS_CARRINHO_CODIGO_PRODUTO_CARRINHO_SEQ;


/* -------------- Cria as sequences -------------- */
CREATE SEQUENCE sys.MERCADOS_CODIGO_MERCADO_SEQ START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE;
CREATE SEQUENCE sys.PRODUTOS_CODIGO_PRODUTO_SEQ START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE;
CREATE SEQUENCE sys.PRODUTOS_CARRINHO_CODIGO_PRODUTO_CARRINHO_SEQ START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE;


/* -------------- Cria as tabelas -------------- */
CREATE TABLE sys.MERCADOS (
    CODIGO_MERCADO NUMBER DEFAULT sys.MERCADOS_CODIGO_MERCADO_SEQ.NEXTVAL NOT NULL,
    NOME VARCHAR2(255) NOT NULL,
    URL VARCHAR2(255) NOT NULL,
    CONSTRAINT MERCADOS_PK PRIMARY KEY (CODIGO_MERCADO)
);

CREATE TABLE sys.PRODUTOS (
    CODIGO_PRODUTO NUMBER DEFAULT sys.MERCADOS_CODIGO_MERCADO_SEQ.NEXTVAL NOT NULL,
    DESCRICAO_PRODUTO VARCHAR2(255) NOT NULL,
    CONSTRAINT PRODUTOS_PK PRIMARY KEY (CODIGO_PRODUTO)
);

CREATE TABLE sys.PRODUTOS_MERCADOS (
    CODIGO_PRODUTO_MERCADO NUMBER NOT NULL,
    VALOR_UNITARIO NUMBER(9,2) NOT NULL,
    CODIGO_PRODUTO NUMBER NOT NULL,
    CODIGO_MERCADO NUMBER NOT NULL,
    CONSTRAINT PRODUTOS_MERCADOS_PK PRIMARY KEY (CODIGO_PRODUTO_MERCADO)
);

CREATE TABLE sys.PRODUTOS_CARRINHO (
    CODIGO_PRODUTO_CARRINHO NUMBER DEFAULT sys.PRODUTOS_CARRINHO_CODIGO_PRODUTO_CARRINHO_SEQ.NEXTVAL NOT NULL,
    CODIGO_PRODUTO_MERCADO NUMBER NOT NULL,
    QUANTIDADE NUMBER NOT NULL,
    CONSTRAINT PRODUTOS_CARRINHO_PK PRIMARY KEY (CODIGO_PRODUTO_CARRINHO)
);


/* -------------- Cria os relacionamentos -------------- */
ALTER TABLE sys.PRODUTOS_MERCADOS 
ADD CONSTRAINT PRODUTOS_MERCADOS_PRODUTOS_FK 
FOREIGN KEY (CODIGO_PRODUTO) 
REFERENCES sys.PRODUTOS (CODIGO_PRODUTO);

ALTER TABLE sys.PRODUTOS_MERCADOS 
ADD CONSTRAINT PRODUTOS_MERCADOS_MERCADOS_FK 
FOREIGN KEY (CODIGO_MERCADO) 
REFERENCES sys.MERCADOS (CODIGO_MERCADO);

ALTER TABLE sys.PRODUTOS_CARRINHO 
ADD CONSTRAINT PRODUTOS_CARRINHO_PRODUTOS_MERCADOS_FK 
FOREIGN KEY (CODIGO_PRODUTO_MERCADO) 
REFERENCES sys.PRODUTOS_MERCADOS (CODIGO_PRODUTO_MERCADO);


/* -------------- Garante acesso total as tabelas -------------- */
GRANT ALL ON sys.MERCADOS TO sys;
GRANT ALL ON sys.PRODUTOS TO sys;
GRANT ALL ON sys.PRODUTOS_MERCADOS TO sys;
GRANT ALL ON sys.PRODUTOS_CARRINHO TO sys;

ALTER USER sys quota unlimited on USERS;