/* ModelagemLogico: */

CREATE SCHEMA IF NOT EXISTS soad;

SET search_path TO soad;

CREATE TABLE pessoa_fisica (
    id serial PRIMARY KEY UNIQUE,
    fk_pessoa_id bigint,
    cpf VARCHAR(11),
    data_nascimento DATE,
    UNIQUE (id, cpf)
);

CREATE TABLE modalidade (
    id serial PRIMARY KEY UNIQUE,
    descricao VARCHAR(30)
);

CREATE TABLE pessoa_juridica (
    id serial PRIMARY KEY UNIQUE,
    fk_pessoa_id bigint,
    cnpj VARCHAR(14),
    inscricao_estadual VARCHAR(15),
    fantasia VARCHAR(80),
    UNIQUE (id, cnpj, inscricao_estadual)
);

CREATE TABLE pessoa (
    id serial PRIMARY KEY UNIQUE,
    nome VARCHAR(60),
    email VARCHAR(80),
    telefone VARCHAR(20),
    data_cadastro DATE
);

CREATE TABLE produto (
    id serial PRIMARY KEY UNIQUE,
    fk_unidade_medida BIGINT,
    descricao VARCHAR(30),
    marca VARCHAR(30),
    UNIQUE (id, descricao)
);

CREATE TABLE toner (
    id serial PRIMARY KEY UNIQUE,
    fk_insumo_id BIGINT,
    fk_produto_id BIGINT,
    quantidade_insumo REAL
);

CREATE TABLE insumo (
    id serial PRIMARY KEY UNIQUE,
    fk_produto_id BIGINT,
    quantidade_embalagem REAL,
    fk_unidade_medida BIGINT
);

CREATE TABLE usuario (
    id serial PRIMARY KEY UNIQUE,
    fk_pessoa_id bigint,
    usuario VARCHAR(20),
    funcao INTEGER
);

CREATE TABLE modalidade_pessoa (
    id serial PRIMARY KEY UNIQUE,
    fk_pessoa_id bigint,
    fk_modalidade_id BIGINT
);

CREATE TABLE unidade_medida (
    id serial PRIMARY KEY UNIQUE,
    descricao VARCHAR(30),
    abreviacao VARCHAR(5),
    UNIQUE (id, descricao, abreviacao)
);

CREATE TABLE pedido (
    id serial PRIMARY KEY UNIQUE,
    fk_pessoa bigint,
    data_entrega DATE,
    situacao INTEGER,
    tipo_pedido BOOLEAN,
    data_cadastro DATE,
    observacao VARCHAR(160)
);

CREATE TABLE remanufatura (
    id serial PRIMARY KEY UNIQUE,
    fk_pedido BIGINT,
    fk_toner BIGINT,
    quantidade INTEGER,
    valor_unitario REAL
);

CREATE TABLE item_pedido (
    id serial PRIMARY KEY UNIQUE,
    fk_pedido BIGINT,
    fk_produto BIGINT,
    quantidade INTEGER,
    valor_unitario REAL
);

CREATE TABLE item_lote (
    id serial PRIMARY KEY UNIQUE,
    fk_lote BIGINT,
    fk_item_pedido_saida BIGINT,
    data_validade DATE,
    lote_fabricante VARCHAR(30),
    data_retirada DATE,
    motivo_retirada VARCHAR(60)
);

CREATE TABLE lote (
    id serial PRIMARY KEY UNIQUE,
    fk_pedido_entrada BIGINT,
    fk_produto BIGINT,
    data_entrada DATE,
    vazio BOOLEAN
);

CREATE TABLE endereco (
    id serial PRIMARY KEY UNIQUE,
    fk_cidade bigint,
    fk_pessoa bigint,
    rua varchar(60),
    numero varchar(10),
    bairro varchar(60),
    cep varchar(15)
);

CREATE TABLE cidade (
    id serial PRIMARY KEY UNIQUE,
    fk_estado bigint,
    nome varchar(60)
);

CREATE TABLE estado (
    id serial PRIMARY KEY UNIQUE,
    fk_pais bigint,
    nome varchar(60)
);

CREATE TABLE pais (
    id serial PRIMARY KEY UNIQUE,
    nome varchar(60),
    UNIQUE (nome, id)
);
 
ALTER TABLE pessoa_fisica ADD CONSTRAINT FK_pessoa_fisica_2
    FOREIGN KEY (fk_pessoa_id)
    REFERENCES pessoa (id)
    ON DELETE CASCADE;
 
ALTER TABLE pessoa_juridica ADD CONSTRAINT FK_pessoa_juridica_3
    FOREIGN KEY (fk_pessoa_id)
    REFERENCES pessoa (id);
 
ALTER TABLE produto ADD CONSTRAINT FK_produto_3
    FOREIGN KEY (fk_unidade_medida)
    REFERENCES unidade_medida (id);
 
ALTER TABLE toner ADD CONSTRAINT FK_toner_2
    FOREIGN KEY (fk_insumo_id)
    REFERENCES insumo (id)
    ON DELETE CASCADE;
 
ALTER TABLE toner ADD CONSTRAINT FK_toner_3
    FOREIGN KEY (fk_produto_id)
    REFERENCES produto (id)
    ON DELETE CASCADE;
 
ALTER TABLE insumo ADD CONSTRAINT FK_insumo_2
    FOREIGN KEY (fk_produto_id)
    REFERENCES produto (id)
    ON DELETE CASCADE;
 
ALTER TABLE insumo ADD CONSTRAINT FK_insumo_4
    FOREIGN KEY (fk_unidade_medida)
    REFERENCES unidade_medida (id);
 
ALTER TABLE usuario ADD CONSTRAINT FK_usuario_2
    FOREIGN KEY (fk_pessoa_id)
    REFERENCES pessoa (id)
    ON DELETE CASCADE;
 
ALTER TABLE modalidade_pessoa ADD CONSTRAINT FK_modalidade_pessoa_1
    FOREIGN KEY (fk_modalidade_id)
    REFERENCES modalidade (id)
    ON DELETE SET NULL;
 
ALTER TABLE modalidade_pessoa ADD CONSTRAINT FK_modalidade_pessoa_2
    FOREIGN KEY (fk_pessoa_id)
    REFERENCES pessoa (id)
    ON DELETE SET NULL;
 
ALTER TABLE pedido ADD CONSTRAINT FK_pedido_3
    FOREIGN KEY (fk_pessoa)
    REFERENCES pessoa (id);
 
ALTER TABLE remanufatura ADD CONSTRAINT FK_remanufatura_3
    FOREIGN KEY (fk_pedido)
    REFERENCES pedido (id);
 
ALTER TABLE remanufatura ADD CONSTRAINT FK_remanufatura_4
    FOREIGN KEY (fk_toner)
    REFERENCES toner (id);
 
ALTER TABLE item_pedido ADD CONSTRAINT FK_item_pedido_3
    FOREIGN KEY (fk_produto)
    REFERENCES produto (id);
 
ALTER TABLE item_pedido ADD CONSTRAINT FK_item_pedido_4
    FOREIGN KEY (fk_pedido)
    REFERENCES pedido (id);
 
ALTER TABLE item_lote ADD CONSTRAINT FK_item_lote_3
    FOREIGN KEY (fk_lote)
    REFERENCES lote (id);
 
ALTER TABLE lote ADD CONSTRAINT FK_lote_1
    FOREIGN KEY (fk_pedido_entrada)
    REFERENCES pedido (id);
 
ALTER TABLE lote ADD CONSTRAINT FK_lote_4
    FOREIGN KEY (fk_produto)
    REFERENCES produto (id);
 
ALTER TABLE endereco ADD CONSTRAINT FK_endereco_1
    FOREIGN KEY (fk_pessoa)
    REFERENCES pessoa (id);
 
ALTER TABLE endereco ADD CONSTRAINT FK_endereco_4
    FOREIGN KEY (fk_cidade)
    REFERENCES cidade (id);
 
ALTER TABLE cidade ADD CONSTRAINT FK_cidade_1
    FOREIGN KEY (fk_estado)
    REFERENCES estado (id);
 
ALTER TABLE estado ADD CONSTRAINT FK_estado_3
    FOREIGN KEY (fk_pais)
    REFERENCES pais (id);