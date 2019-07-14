--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4
-- Dumped by pg_dump version 11.2

-- Started on 2019-07-14 04:24:56

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "postgres";
--
-- TOC entry 3025 (class 1262 OID 13012)
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "postgres" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Portuguese_Brazil.1252' LC_CTYPE = 'Portuguese_Brazil.1252';


ALTER DATABASE "postgres" OWNER TO "postgres";

\connect "postgres"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3026 (class 0 OID 0)
-- Dependencies: 3025
-- Name: DATABASE "postgres"; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE "postgres" IS 'default administrative connection database';


--
-- TOC entry 5 (class 2615 OID 16618)
-- Name: soad; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA "soad";


ALTER SCHEMA "soad" OWNER TO "postgres";

--
-- TOC entry 252 (class 1255 OID 17551)
-- Name: fnc_relatorio_cidades(character varying, character varying, character varying); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_relatorio_cidades"("p_pais" character varying, "p_estado" character varying, "p_cidade" character varying) RETURNS TABLE("cidade_id" integer, "cidade" character varying, "estado_id" integer, "estado" character varying, "pais_id" integer, "pais" character varying)
    LANGUAGE "plpgsql"
    AS $$
begin
	return query select cidade.id_cidade, cidade.nome, estado.id_estado, estado.nome, pais.id_pais, pais.nome
					from soad.cidade
						inner join soad.estado on cidade.fk_estado_id = estado.id_estado
						inner join soad.pais on estado.fk_pais_id = pais.id_pais
						where 1=1
						and cidade.nome like p_cidade
						and estado.nome like p_estado
						and pais.nome   like p_estado;
end;
$$;


ALTER FUNCTION "soad"."fnc_relatorio_cidades"("p_pais" character varying, "p_estado" character varying, "p_cidade" character varying) OWNER TO "postgres";

--
-- TOC entry 250 (class 1255 OID 17545)
-- Name: prc_definicoes_iniciais(); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_definicoes_iniciais"()
    LANGUAGE "plpgsql"
    AS $$
BEGIN
	-- Cadastra Unidade de medida
	CALL soad.prc_insert_unidade_medida('KILOGRAMA', 'kg');
	CALL soad.prc_insert_unidade_medida('LITRO', 'l');
	CALL soad.prc_insert_unidade_medida('MILIGRAMA', 'mg');
	CALL soad.prc_insert_unidade_medida('MILILITRO', 'ml');

	-- Cadastra Modalidades
	CALL soad.prc_insert_modalidade('Cliente');
	CALL soad.prc_insert_modalidade('Fornecedor');
		
	-- Cadastra paises
	CALL soad.prc_insert_cidade_estado_pais('', '', '', 'Brasil', 'BR');
	
	-- Cadastra estados
	CALL soad.prc_insert_cidade_estado_pais('', 'Acre', 'AC', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Alagoas', 'AL', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Amapá', 'AP', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Amazonas', 'AM', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Bahia', 'BA', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Ceará', 'CE', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Distrito Federal', 'DF', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Espírito Santo', 'ES', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Goiás', 'GO', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Maranhão', 'MA', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Mato Grosso', 'MT', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Mato Grosso do Sul', 'MS', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Minas Gerais', 'MG', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Pará', 'PA', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Paraíba', 'PB', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Paraná', 'PR', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Pernambuco', 'PE', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Piauí', 'PI', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Rio de Janeiro', 'RJ', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Rio Grande do Norte', 'RN', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Rio Grande do Sul', 'RS', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Rondônia', 'RO', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Roraima', 'RR', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Santa Catarina', 'SC', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'São Paulo', 'SP', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Sergipe', 'SE', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('', 'Tocantins', 'TO', 'Brasil', 'BR');

	-- Cadastra Cidades
	CALL soad.prc_insert_cidade_estado_pais('Ponta Grossa', 'Paraná', 'PR', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('Curitiba', 'Paraná', 'PR', 'Brasil', 'BR');
	CALL soad.prc_insert_cidade_estado_pais('Castro', 'Paraná', 'PR', 'Brasil', 'BR');
	
	-- Cadastra pessoa
	CALL soad.prc_insert_pessoa('VIP Cartuchos', '', '4232240660', '00000000000000', '', 'VIP Cartuchos');
	CALL soad.prc_insert_pessoa('Lucas Klüber', 'lucas.kluber@gmail.com', '42999823030', '10841793930', '', '');
	
	
END;
$$;


ALTER PROCEDURE "soad"."prc_definicoes_iniciais"() OWNER TO "postgres";

--
-- TOC entry 253 (class 1255 OID 17567)
-- Name: prc_insert_cidade_estado_pais("text", "text", "text", "text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_cidade_estado_pais"("p_cidade_nome" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text")
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	-- Pega os parametros e deixa em maiusculo
	v_cidade_nome text := upper(p_cidade_nome);
	v_estado_nome text := upper(p_estado_nome);
	v_estado_sigla text := upper(p_estado_sigla);
	v_pais_sigla text := upper(p_pais_sigla);
	v_pais_nome text := upper(p_pais_nome);
	v_data_cadastro date := statement_timestamp();
	-- variaveis auxiliares
	v_aux integer := NULL;

BEGIN
	------ É possível inserir apenas o estado ou apenas o pais caso cidade ou cidade e estado estejam em branco -------
	
	-- Insere apenas pais
	IF v_cidade_nome = '' AND v_estado_nome = '' AND v_pais_nome <> '' THEN
	
		INSERT INTO soad.pais (nome, sigla)
		VALUES (v_pais_nome, v_pais_sigla)
		ON CONFLICT ON CONSTRAINT pais_sigla_key DO NOTHING;
	
	RETURN;
	
	-- Insere apenas estado
	ELSIF v_cidade_nome = '' AND v_estado_nome <> '' AND v_pais_nome <> '' THEN

		SELECT id_pais into v_aux FROM soad.pais WHERE pais.sigla = v_pais_sigla;

		INSERT INTO soad.estado (fk_pais_id, nome, sigla)
		VALUES (v_aux, v_estado_nome, v_estado_sigla)
		ON CONFLICT ON CONSTRAINT estado_sigla_fk_pais_id_key DO NOTHING;

	RETURN;
	
	END IF;

   -- Precisa dessa separacao por que se não tiver inserido o registro pai ainda 
   -- o postgres nao acha a chave primaria pra colocar como estrangeira no filho
   
   -------- A partir daqui tenta inserir novo pais, novo estado e nova cidade ---------
	
	-- valida parametros
	IF v_pais_nome = '' OR v_pais_sigla = '' THEN
		RAISE NOTICE 'É preciso informar um país.';
	ELSIF v_estado_nome = '' OR v_estado_sigla = '' THEN
		RAISE NOTICE 'É preciso informar um estado.';
	ELSIF v_cidade_nome = '' THEN
		RAISE NOTICE 'É preciso informar uma cidade';
	END IF;
	
	-- Insere cidade, estado e pais
	IF (SELECT count(*) FROM soad.pais WHERE pais.sigla = v_pais_sigla) = 0 THEN

		WITH t_pais AS (
		  INSERT INTO soad.pais (nome, sigla)
		  VALUES (v_pais_nome, v_pais_sigla)
		  RETURNING id_pais
		), t_estado as (
		  INSERT INTO soad.estado (fk_pais_id, nome, sigla)
		  SELECT id_pais, v_estado_nome, v_estado_sigla
		  FROM t_pais
		  RETURNING id_estado
		)
		INSERT INTO soad.cidade (fk_estado_id, nome)
		SELECT id_estado, v_cidade_nome
		FROM t_estado;
	
	RETURN;
		
	-- Insere novo estado e nova cidade
	ELSIF (SELECT count(*) FROM soad.estado WHERE estado.sigla = v_estado_sigla) = 0 THEN
		
		SELECT id_pais into v_aux FROM soad.pais WHERE pais.sigla = v_pais_sigla;
	
		WITH t_estado AS (
		  INSERT INTO soad.estado (fk_pais_id, nome, sigla)
		  VALUES (v_aux, v_estado_nome, v_estado_sigla)
		  RETURNING id_estado
		)
		INSERT INTO soad.cidade (fk_estado_id, nome)
		SELECT id_estado, v_cidade_nome
		FROM t_estado;
	
	RETURN;
		
	-- Insere apenas nova cidade
	ELSIF (SELECT count(*) FROM soad.cidade WHERE cidade.nome = v_cidade_nome) = 0 THEN
		
		SELECT estado.id_estado into v_aux 
		FROM soad.estado 
		INNER JOIN soad.pais ON estado.fk_pais_id = pais.id_pais
		WHERE estado.sigla = v_estado_sigla;

		INSERT INTO soad.cidade (fk_estado_id, nome)
		VALUES (v_aux, v_cidade_nome);
		
	RETURN;
	
	END IF;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_cidade_estado_pais"("p_cidade_nome" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text") OWNER TO "postgres";

--
-- TOC entry 249 (class 1255 OID 17241)
-- Name: prc_insert_modalidade("text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_modalidade"("p_modalidade" "text")
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_modalidade text := upper(p_modalidade);
	
BEGIN
	INSERT INTO soad.modalidade (descricao)
	VALUES (v_modalidade);
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_modalidade"("p_modalidade" "text") OWNER TO "postgres";

--
-- TOC entry 248 (class 1255 OID 17202)
-- Name: prc_insert_pessoa("text", "text", "text", "text", "text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text", "p_fantasia" "text")
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_data_cadastro date := statement_timestamp();
	
BEGIN
	
	IF length(p_documento) = 14 THEN -- insere pessoa e pessoa juridica
		WITH ins_p AS (
			INSERT INTO soad.pessoa (
				nome
				, email
				, telefone
				, data_cadastro
			)
				VALUES (p_nome, p_email, p_telefone, v_data_cadastro)	
				RETURNING id_pessoa
		)
		
		INSERT INTO soad.pessoa_juridica (
			fk_pessoa_id, cnpj
			, inscricao_estadual
			, fantasia
			, data_cadastro
		)
			SELECT id_pessoa, p_documento, p_inscricao_estadual, p_fantasia, v_data_cadastro
			FROM ins_p;
			

	ELSIF length(p_documento) = 11 THEN 	-- insere pessoa e pessoa fisica
		WITH ins_p AS (
			INSERT INTO soad.pessoa (
				nome
				, email
				, telefone
				, data_cadastro
			)
				VALUES (p_nome, p_email, p_telefone, v_data_cadastro)	
				RETURNING id_pessoa
		)

		INSERT INTO soad.pessoa_fisica (
			fk_pessoa_id
			, cpf
			, data_cadastro
		) 
		SELECT id_pessoa, p_documento, v_data_cadastro
		FROM ins_p;
		
	END IF;
	
EXCEPTION WHEN OTHERS THEN
	--RAISE NOTICE 'ERRO OCORREU';
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text", "p_fantasia" "text") OWNER TO "postgres";

--
-- TOC entry 251 (class 1255 OID 17541)
-- Name: prc_insert_unidade_medida("text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_unidade_medida"("p_descricao" "text", "p_abreviacao" "text")
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_abreviacao text := lower(p_abreviacao);
	v_descricao text := upper(p_descricao);
	
BEGIN
	INSERT INTO soad.unidade_medida (descricao, abreviacao)
	VALUES (v_descricao, v_abreviacao)
	ON CONFLICT ON CONSTRAINT unidade_medida_abreviacao_key DO NOTHING;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_unidade_medida"("p_descricao" "text", "p_abreviacao" "text") OWNER TO "postgres";

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 208 (class 1259 OID 16916)
-- Name: casco; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."casco" (
    "id_casco" integer NOT NULL,
    "fk_insumo_id" integer NOT NULL,
    "fk_produto_id" integer NOT NULL,
    "quantidade_insumo" real NOT NULL
);


ALTER TABLE "soad"."casco" OWNER TO "postgres";

--
-- TOC entry 230 (class 1259 OID 17006)
-- Name: cidade; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."cidade" (
    "id_cidade" integer NOT NULL,
    "fk_estado_id" integer NOT NULL,
    "nome" character varying(120) NOT NULL
);


ALTER TABLE "soad"."cidade" OWNER TO "postgres";

--
-- TOC entry 229 (class 1259 OID 17004)
-- Name: cidade_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."cidade_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."cidade_id_seq" OWNER TO "postgres";

--
-- TOC entry 3027 (class 0 OID 0)
-- Dependencies: 229
-- Name: cidade_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."cidade_id_seq" OWNED BY "soad"."cidade"."id_cidade";


--
-- TOC entry 235 (class 1259 OID 17203)
-- Name: dicionario_dados; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."dicionario_dados" AS
 SELECT "columns"."table_name",
    "columns"."column_name",
    "columns"."is_nullable",
    "columns"."data_type"
   FROM "information_schema"."columns"
  WHERE (("columns"."table_schema")::"text" = 'soad'::"text");


ALTER TABLE "soad"."dicionario_dados" OWNER TO "postgres";

--
-- TOC entry 228 (class 1259 OID 16998)
-- Name: endereco; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."endereco" (
    "id_endereco" integer NOT NULL,
    "fk_cidade_id" integer NOT NULL,
    "fk_pessoa_id" integer NOT NULL,
    "logradouro" character varying(150) NOT NULL,
    "numero" character varying(5),
    "bairro" character varying(100),
    "cep" character varying(8)
);


ALTER TABLE "soad"."endereco" OWNER TO "postgres";

--
-- TOC entry 227 (class 1259 OID 16996)
-- Name: endereco_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."endereco_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."endereco_id_seq" OWNER TO "postgres";

--
-- TOC entry 3028 (class 0 OID 0)
-- Dependencies: 227
-- Name: endereco_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."endereco_id_seq" OWNED BY "soad"."endereco"."id_endereco";


--
-- TOC entry 232 (class 1259 OID 17014)
-- Name: estado; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."estado" (
    "id_estado" integer NOT NULL,
    "fk_pais_id" integer NOT NULL,
    "nome" character varying(60) NOT NULL,
    "sigla" character varying(2) NOT NULL
);


ALTER TABLE "soad"."estado" OWNER TO "postgres";

--
-- TOC entry 231 (class 1259 OID 17012)
-- Name: estado_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."estado_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."estado_id_seq" OWNER TO "postgres";

--
-- TOC entry 3029 (class 0 OID 0)
-- Dependencies: 231
-- Name: estado_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."estado_id_seq" OWNED BY "soad"."estado"."id_estado";


--
-- TOC entry 210 (class 1259 OID 16924)
-- Name: insumo; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."insumo" (
    "id_insumo" integer NOT NULL,
    "fk_produto_id" integer NOT NULL,
    "quantidade_embalagem" real NOT NULL,
    "fk_unidade_medida_id" integer NOT NULL
);


ALTER TABLE "soad"."insumo" OWNER TO "postgres";

--
-- TOC entry 209 (class 1259 OID 16922)
-- Name: insumo_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."insumo_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."insumo_id_seq" OWNER TO "postgres";

--
-- TOC entry 3030 (class 0 OID 0)
-- Dependencies: 209
-- Name: insumo_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."insumo_id_seq" OWNED BY "soad"."insumo"."id_insumo";


--
-- TOC entry 224 (class 1259 OID 16982)
-- Name: item_lote; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."item_lote" (
    "id_item_lote_id" integer NOT NULL,
    "fk_lote_id" bigint NOT NULL,
    "fk_item_pedido_id" bigint NOT NULL,
    "data_validade" "date",
    "lote_fabricante" character varying(60),
    "data_retirada" timestamp(4) with time zone NOT NULL,
    "motivo_retirada" character varying(300) NOT NULL
);


ALTER TABLE "soad"."item_lote" OWNER TO "postgres";

--
-- TOC entry 3031 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN "item_lote"."fk_item_pedido_id"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."item_lote"."fk_item_pedido_id" IS 'ID do item_pedido de saída desse item_lote';


--
-- TOC entry 223 (class 1259 OID 16980)
-- Name: item_lote_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."item_lote_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."item_lote_id_seq" OWNER TO "postgres";

--
-- TOC entry 3032 (class 0 OID 0)
-- Dependencies: 223
-- Name: item_lote_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."item_lote_id_seq" OWNED BY "soad"."item_lote"."id_item_lote_id";


--
-- TOC entry 222 (class 1259 OID 16974)
-- Name: item_pedido; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."item_pedido" (
    "id_item_pedido" integer NOT NULL,
    "fk_pedido_id" integer NOT NULL,
    "fk_produto_id" integer NOT NULL,
    "quantidade" integer NOT NULL,
    "valor_unitario" real NOT NULL
);


ALTER TABLE "soad"."item_pedido" OWNER TO "postgres";

--
-- TOC entry 221 (class 1259 OID 16972)
-- Name: item_pedido_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."item_pedido_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."item_pedido_id_seq" OWNER TO "postgres";

--
-- TOC entry 3033 (class 0 OID 0)
-- Dependencies: 221
-- Name: item_pedido_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."item_pedido_id_seq" OWNED BY "soad"."item_pedido"."id_item_pedido";


--
-- TOC entry 226 (class 1259 OID 16990)
-- Name: lote; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."lote" (
    "id_lote" integer NOT NULL,
    "fk_pedido_id" integer NOT NULL,
    "fk_produto_id" integer NOT NULL,
    "data_entrada" "date" NOT NULL,
    "vazio" boolean NOT NULL
);


ALTER TABLE "soad"."lote" OWNER TO "postgres";

--
-- TOC entry 3034 (class 0 OID 0)
-- Dependencies: 226
-- Name: COLUMN "lote"."fk_pedido_id"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."lote"."fk_pedido_id" IS 'ID do pedido de entrada da mercadoria';


--
-- TOC entry 225 (class 1259 OID 16988)
-- Name: lote_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."lote_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."lote_id_seq" OWNER TO "postgres";

--
-- TOC entry 3035 (class 0 OID 0)
-- Dependencies: 225
-- Name: lote_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."lote_id_seq" OWNED BY "soad"."lote"."id_lote";


--
-- TOC entry 200 (class 1259 OID 16880)
-- Name: modalidade; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."modalidade" (
    "id_modalidade" integer NOT NULL,
    "descricao" character varying(20) NOT NULL
);


ALTER TABLE "soad"."modalidade" OWNER TO "postgres";

--
-- TOC entry 199 (class 1259 OID 16878)
-- Name: modalidade_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."modalidade_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."modalidade_id_seq" OWNER TO "postgres";

--
-- TOC entry 3036 (class 0 OID 0)
-- Dependencies: 199
-- Name: modalidade_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."modalidade_id_seq" OWNED BY "soad"."modalidade"."id_modalidade";


--
-- TOC entry 214 (class 1259 OID 16940)
-- Name: modalidade_pessoa; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."modalidade_pessoa" (
    "id_modalidade_pessoa" integer NOT NULL,
    "fk_pessoa_id" integer NOT NULL,
    "fk_modalidade_id" integer NOT NULL
);


ALTER TABLE "soad"."modalidade_pessoa" OWNER TO "postgres";

--
-- TOC entry 213 (class 1259 OID 16938)
-- Name: modalidade_pessoa_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."modalidade_pessoa_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."modalidade_pessoa_id_seq" OWNER TO "postgres";

--
-- TOC entry 3037 (class 0 OID 0)
-- Dependencies: 213
-- Name: modalidade_pessoa_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."modalidade_pessoa_id_seq" OWNED BY "soad"."modalidade_pessoa"."id_modalidade_pessoa";


--
-- TOC entry 234 (class 1259 OID 17022)
-- Name: pais; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."pais" (
    "id_pais" integer NOT NULL,
    "nome" character varying(60) NOT NULL,
    "sigla" character varying(2) NOT NULL
);


ALTER TABLE "soad"."pais" OWNER TO "postgres";

--
-- TOC entry 233 (class 1259 OID 17020)
-- Name: pais_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."pais_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."pais_id_seq" OWNER TO "postgres";

--
-- TOC entry 3038 (class 0 OID 0)
-- Dependencies: 233
-- Name: pais_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."pais_id_seq" OWNED BY "soad"."pais"."id_pais";


--
-- TOC entry 218 (class 1259 OID 16958)
-- Name: pedido; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."pedido" (
    "id_pedido" integer NOT NULL,
    "fk_pessoa_id" integer NOT NULL,
    "data_entrega" "date",
    "tipo_pedido" boolean NOT NULL,
    "data_cadastro" timestamp(4) with time zone NOT NULL,
    "observacao" character varying(300),
    "situacao" character varying(10) NOT NULL,
    CONSTRAINT "cc_pedido_situacao_check" CHECK (((("situacao")::"text" = 'CADASTRADO'::"text") OR (("situacao")::"text" = 'ENCERRADO'::"text") OR (("situacao")::"text" = 'CANCELADO'::"text")))
);


ALTER TABLE "soad"."pedido" OWNER TO "postgres";

--
-- TOC entry 3039 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN "pedido"."tipo_pedido"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."pedido"."tipo_pedido" IS '0 = Entrada
1 = Saida';


--
-- TOC entry 3040 (class 0 OID 0)
-- Dependencies: 218
-- Name: CONSTRAINT "cc_pedido_situacao_check" ON "pedido"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "cc_pedido_situacao_check" ON "soad"."pedido" IS 'Define as situacoes permitidas para o pedido';


--
-- TOC entry 217 (class 1259 OID 16956)
-- Name: pedido_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."pedido_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."pedido_id_seq" OWNER TO "postgres";

--
-- TOC entry 3041 (class 0 OID 0)
-- Dependencies: 217
-- Name: pedido_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."pedido_id_seq" OWNED BY "soad"."pedido"."id_pedido";


--
-- TOC entry 204 (class 1259 OID 16898)
-- Name: pessoa; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."pessoa" (
    "id_pessoa" integer NOT NULL,
    "nome" character varying(100) NOT NULL,
    "email" character varying(100),
    "telefone" character varying(20),
    "data_cadastro" "date" NOT NULL
);


ALTER TABLE "soad"."pessoa" OWNER TO "postgres";

--
-- TOC entry 198 (class 1259 OID 16870)
-- Name: pessoa_fisica; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."pessoa_fisica" (
    "id_pessoa_fisica" integer NOT NULL,
    "fk_pessoa_id" integer NOT NULL,
    "cpf" character varying(11) NOT NULL,
    "data_cadastro" timestamp(4) with time zone NOT NULL
);


ALTER TABLE "soad"."pessoa_fisica" OWNER TO "postgres";

--
-- TOC entry 197 (class 1259 OID 16868)
-- Name: pessoa_fisica_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."pessoa_fisica_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."pessoa_fisica_id_seq" OWNER TO "postgres";

--
-- TOC entry 3042 (class 0 OID 0)
-- Dependencies: 197
-- Name: pessoa_fisica_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."pessoa_fisica_id_seq" OWNED BY "soad"."pessoa_fisica"."id_pessoa_fisica";


--
-- TOC entry 203 (class 1259 OID 16896)
-- Name: pessoa_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."pessoa_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."pessoa_id_seq" OWNER TO "postgres";

--
-- TOC entry 3043 (class 0 OID 0)
-- Dependencies: 203
-- Name: pessoa_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."pessoa_id_seq" OWNED BY "soad"."pessoa"."id_pessoa";


--
-- TOC entry 202 (class 1259 OID 16888)
-- Name: pessoa_juridica; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."pessoa_juridica" (
    "id_pessoa_juridica" integer NOT NULL,
    "fk_pessoa_id" integer NOT NULL,
    "cnpj" character varying(14) NOT NULL,
    "inscricao_estadual" character varying(15),
    "fantasia" character varying(150) NOT NULL,
    "data_cadastro" timestamp(4) with time zone NOT NULL
);


ALTER TABLE "soad"."pessoa_juridica" OWNER TO "postgres";

--
-- TOC entry 201 (class 1259 OID 16886)
-- Name: pessoa_juridica_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."pessoa_juridica_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."pessoa_juridica_id_seq" OWNER TO "postgres";

--
-- TOC entry 3044 (class 0 OID 0)
-- Dependencies: 201
-- Name: pessoa_juridica_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."pessoa_juridica_id_seq" OWNED BY "soad"."pessoa_juridica"."id_pessoa_juridica";


--
-- TOC entry 206 (class 1259 OID 16906)
-- Name: produto; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."produto" (
    "id_produto" integer NOT NULL,
    "fk_unidade_medida_id" integer NOT NULL,
    "descricao" character varying(120) NOT NULL,
    "marca" character varying(80)
);


ALTER TABLE "soad"."produto" OWNER TO "postgres";

--
-- TOC entry 205 (class 1259 OID 16904)
-- Name: produto_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."produto_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."produto_id_seq" OWNER TO "postgres";

--
-- TOC entry 3045 (class 0 OID 0)
-- Dependencies: 205
-- Name: produto_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."produto_id_seq" OWNED BY "soad"."produto"."id_produto";


--
-- TOC entry 220 (class 1259 OID 16966)
-- Name: remanufatura; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."remanufatura" (
    "id_remanufatura" integer NOT NULL,
    "fk_pedido_id" integer NOT NULL,
    "fk_casco_id" integer NOT NULL,
    "quantidade" integer NOT NULL,
    "valor_unitario" real NOT NULL
);


ALTER TABLE "soad"."remanufatura" OWNER TO "postgres";

--
-- TOC entry 219 (class 1259 OID 16964)
-- Name: remanufatura_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."remanufatura_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."remanufatura_id_seq" OWNER TO "postgres";

--
-- TOC entry 3046 (class 0 OID 0)
-- Dependencies: 219
-- Name: remanufatura_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."remanufatura_id_seq" OWNED BY "soad"."remanufatura"."id_remanufatura";


--
-- TOC entry 207 (class 1259 OID 16914)
-- Name: toner_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."toner_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."toner_id_seq" OWNER TO "postgres";

--
-- TOC entry 3047 (class 0 OID 0)
-- Dependencies: 207
-- Name: toner_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."toner_id_seq" OWNED BY "soad"."casco"."id_casco";


--
-- TOC entry 216 (class 1259 OID 16948)
-- Name: unidade_medida; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."unidade_medida" (
    "id_unidade_medida" integer NOT NULL,
    "descricao" character varying(30) NOT NULL,
    "abreviacao" character varying(5) NOT NULL
);


ALTER TABLE "soad"."unidade_medida" OWNER TO "postgres";

--
-- TOC entry 215 (class 1259 OID 16946)
-- Name: unidade_medida_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."unidade_medida_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."unidade_medida_id_seq" OWNER TO "postgres";

--
-- TOC entry 3048 (class 0 OID 0)
-- Dependencies: 215
-- Name: unidade_medida_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."unidade_medida_id_seq" OWNED BY "soad"."unidade_medida"."id_unidade_medida";


--
-- TOC entry 212 (class 1259 OID 16932)
-- Name: usuario; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."usuario" (
    "id_usuario" integer NOT NULL,
    "fk_pessoa_id" integer,
    "usuario" character varying(20),
    "funcao" integer
);


ALTER TABLE "soad"."usuario" OWNER TO "postgres";

--
-- TOC entry 211 (class 1259 OID 16930)
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."usuario_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."usuario_id_seq" OWNER TO "postgres";

--
-- TOC entry 3049 (class 0 OID 0)
-- Dependencies: 211
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."usuario_id_seq" OWNED BY "soad"."usuario"."id_usuario";


--
-- TOC entry 2809 (class 2604 OID 16919)
-- Name: casco id_casco; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco" ALTER COLUMN "id_casco" SET DEFAULT "nextval"('"soad"."toner_id_seq"'::"regclass");


--
-- TOC entry 2821 (class 2604 OID 17009)
-- Name: cidade id_cidade; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade" ALTER COLUMN "id_cidade" SET DEFAULT "nextval"('"soad"."cidade_id_seq"'::"regclass");


--
-- TOC entry 2820 (class 2604 OID 17001)
-- Name: endereco id_endereco; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco" ALTER COLUMN "id_endereco" SET DEFAULT "nextval"('"soad"."endereco_id_seq"'::"regclass");


--
-- TOC entry 2822 (class 2604 OID 17017)
-- Name: estado id_estado; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado" ALTER COLUMN "id_estado" SET DEFAULT "nextval"('"soad"."estado_id_seq"'::"regclass");


--
-- TOC entry 2810 (class 2604 OID 16927)
-- Name: insumo id_insumo; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo" ALTER COLUMN "id_insumo" SET DEFAULT "nextval"('"soad"."insumo_id_seq"'::"regclass");


--
-- TOC entry 2818 (class 2604 OID 16985)
-- Name: item_lote id_item_lote_id; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote" ALTER COLUMN "id_item_lote_id" SET DEFAULT "nextval"('"soad"."item_lote_id_seq"'::"regclass");


--
-- TOC entry 2817 (class 2604 OID 16977)
-- Name: item_pedido id_item_pedido; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido" ALTER COLUMN "id_item_pedido" SET DEFAULT "nextval"('"soad"."item_pedido_id_seq"'::"regclass");


--
-- TOC entry 2819 (class 2604 OID 16993)
-- Name: lote id_lote; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote" ALTER COLUMN "id_lote" SET DEFAULT "nextval"('"soad"."lote_id_seq"'::"regclass");


--
-- TOC entry 2805 (class 2604 OID 16883)
-- Name: modalidade id_modalidade; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade" ALTER COLUMN "id_modalidade" SET DEFAULT "nextval"('"soad"."modalidade_id_seq"'::"regclass");


--
-- TOC entry 2812 (class 2604 OID 16943)
-- Name: modalidade_pessoa id_modalidade_pessoa; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa" ALTER COLUMN "id_modalidade_pessoa" SET DEFAULT "nextval"('"soad"."modalidade_pessoa_id_seq"'::"regclass");


--
-- TOC entry 2823 (class 2604 OID 17025)
-- Name: pais id_pais; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais" ALTER COLUMN "id_pais" SET DEFAULT "nextval"('"soad"."pais_id_seq"'::"regclass");


--
-- TOC entry 2814 (class 2604 OID 16961)
-- Name: pedido id_pedido; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido" ALTER COLUMN "id_pedido" SET DEFAULT "nextval"('"soad"."pedido_id_seq"'::"regclass");


--
-- TOC entry 2807 (class 2604 OID 16901)
-- Name: pessoa id_pessoa; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa" ALTER COLUMN "id_pessoa" SET DEFAULT "nextval"('"soad"."pessoa_id_seq"'::"regclass");


--
-- TOC entry 2804 (class 2604 OID 16873)
-- Name: pessoa_fisica id_pessoa_fisica; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica" ALTER COLUMN "id_pessoa_fisica" SET DEFAULT "nextval"('"soad"."pessoa_fisica_id_seq"'::"regclass");


--
-- TOC entry 2806 (class 2604 OID 16891)
-- Name: pessoa_juridica id_pessoa_juridica; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica" ALTER COLUMN "id_pessoa_juridica" SET DEFAULT "nextval"('"soad"."pessoa_juridica_id_seq"'::"regclass");


--
-- TOC entry 2808 (class 2604 OID 16909)
-- Name: produto id_produto; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."produto" ALTER COLUMN "id_produto" SET DEFAULT "nextval"('"soad"."produto_id_seq"'::"regclass");


--
-- TOC entry 2816 (class 2604 OID 16969)
-- Name: remanufatura id_remanufatura; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura" ALTER COLUMN "id_remanufatura" SET DEFAULT "nextval"('"soad"."remanufatura_id_seq"'::"regclass");


--
-- TOC entry 2813 (class 2604 OID 16951)
-- Name: unidade_medida id_unidade_medida; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida" ALTER COLUMN "id_unidade_medida" SET DEFAULT "nextval"('"soad"."unidade_medida_id_seq"'::"regclass");


--
-- TOC entry 2811 (class 2604 OID 16935)
-- Name: usuario id_usuario; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario" ALTER COLUMN "id_usuario" SET DEFAULT "nextval"('"soad"."usuario_id_seq"'::"regclass");


--
-- TOC entry 2865 (class 2606 OID 17566)
-- Name: cidade cidade_nome_fk_estado_id_key; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade"
    ADD CONSTRAINT "cidade_nome_fk_estado_id_key" UNIQUE ("nome", "fk_estado_id");


--
-- TOC entry 3050 (class 0 OID 0)
-- Dependencies: 2865
-- Name: CONSTRAINT "cidade_nome_fk_estado_id_key" ON "cidade"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "cidade_nome_fk_estado_id_key" ON "soad"."cidade" IS 'Cada cidade deve ser única no estado';


--
-- TOC entry 2867 (class 2606 OID 17011)
-- Name: cidade cidade_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade"
    ADD CONSTRAINT "cidade_pkey" PRIMARY KEY ("id_cidade");


--
-- TOC entry 2863 (class 2606 OID 17003)
-- Name: endereco endereco_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "endereco_pkey" PRIMARY KEY ("id_endereco");


--
-- TOC entry 2869 (class 2606 OID 17019)
-- Name: estado estado_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "estado_pkey" PRIMARY KEY ("id_estado");


--
-- TOC entry 2871 (class 2606 OID 17557)
-- Name: estado estado_sigla_fk_pais_id_key; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "estado_sigla_fk_pais_id_key" UNIQUE ("sigla") INCLUDE ("fk_pais_id");


--
-- TOC entry 3051 (class 0 OID 0)
-- Dependencies: 2871
-- Name: CONSTRAINT "estado_sigla_fk_pais_id_key" ON "estado"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "estado_sigla_fk_pais_id_key" ON "soad"."estado" IS 'Cada estado deve ser unico no pais';


--
-- TOC entry 2843 (class 2606 OID 16929)
-- Name: insumo insumo_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "insumo_pkey" PRIMARY KEY ("id_insumo");


--
-- TOC entry 2859 (class 2606 OID 16987)
-- Name: item_lote item_lote_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "item_lote_pkey" PRIMARY KEY ("id_item_lote_id");


--
-- TOC entry 2857 (class 2606 OID 16979)
-- Name: item_pedido item_pedido_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "item_pedido_pkey" PRIMARY KEY ("id_item_pedido");


--
-- TOC entry 2861 (class 2606 OID 16995)
-- Name: lote lote_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "lote_pkey" PRIMARY KEY ("id_lote");


--
-- TOC entry 2847 (class 2606 OID 16945)
-- Name: modalidade_pessoa modalidade_pessoa_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "modalidade_pessoa_pkey" PRIMARY KEY ("id_modalidade_pessoa");


--
-- TOC entry 2829 (class 2606 OID 16885)
-- Name: modalidade modalidade_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade"
    ADD CONSTRAINT "modalidade_pkey" PRIMARY KEY ("id_modalidade");


--
-- TOC entry 2873 (class 2606 OID 17027)
-- Name: pais pais_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais"
    ADD CONSTRAINT "pais_pkey" PRIMARY KEY ("id_pais");


--
-- TOC entry 2875 (class 2606 OID 17553)
-- Name: pais pais_sigla_key; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais"
    ADD CONSTRAINT "pais_sigla_key" UNIQUE ("sigla");


--
-- TOC entry 2853 (class 2606 OID 16963)
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido"
    ADD CONSTRAINT "pedido_pkey" PRIMARY KEY ("id_pedido");


--
-- TOC entry 2825 (class 2606 OID 17153)
-- Name: pessoa_fisica pessoa_fisica_id_cpf_key; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "pessoa_fisica_id_cpf_key" UNIQUE ("id_pessoa_fisica", "cpf");


--
-- TOC entry 2827 (class 2606 OID 16875)
-- Name: pessoa_fisica pessoa_fisica_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "pessoa_fisica_pkey" PRIMARY KEY ("id_pessoa_fisica");


--
-- TOC entry 2831 (class 2606 OID 17151)
-- Name: pessoa_juridica pessoa_juridica_id_cnpj_inscricao_estadual_key; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "pessoa_juridica_id_cnpj_inscricao_estadual_key" UNIQUE ("id_pessoa_juridica", "cnpj", "inscricao_estadual");


--
-- TOC entry 2833 (class 2606 OID 16893)
-- Name: pessoa_juridica pessoa_juridica_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "pessoa_juridica_pkey" PRIMARY KEY ("id_pessoa_juridica");


--
-- TOC entry 2835 (class 2606 OID 16903)
-- Name: pessoa pessoa_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa"
    ADD CONSTRAINT "pessoa_pkey" PRIMARY KEY ("id_pessoa");


--
-- TOC entry 2837 (class 2606 OID 17504)
-- Name: produto produto_id_descricao_key; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."produto"
    ADD CONSTRAINT "produto_id_descricao_key" UNIQUE ("id_produto", "descricao");


--
-- TOC entry 2839 (class 2606 OID 16911)
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."produto"
    ADD CONSTRAINT "produto_pkey" PRIMARY KEY ("id_produto");


--
-- TOC entry 2855 (class 2606 OID 16971)
-- Name: remanufatura remanufatura_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "remanufatura_pkey" PRIMARY KEY ("id_remanufatura");


--
-- TOC entry 2841 (class 2606 OID 16921)
-- Name: casco toner_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "toner_pkey" PRIMARY KEY ("id_casco");


--
-- TOC entry 2849 (class 2606 OID 17569)
-- Name: unidade_medida unidade_medida_abreviacao_key; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida"
    ADD CONSTRAINT "unidade_medida_abreviacao_key" UNIQUE ("abreviacao");


--
-- TOC entry 2851 (class 2606 OID 16953)
-- Name: unidade_medida unidade_medida_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida"
    ADD CONSTRAINT "unidade_medida_pkey" PRIMARY KEY ("id_unidade_medida");


--
-- TOC entry 2845 (class 2606 OID 16937)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario"
    ADD CONSTRAINT "usuario_pkey" PRIMARY KEY ("id_usuario");


--
-- TOC entry 2896 (class 2606 OID 17291)
-- Name: cidade fk_cidade_1; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade"
    ADD CONSTRAINT "fk_cidade_1" FOREIGN KEY ("fk_estado_id") REFERENCES "soad"."estado"("id_estado");


--
-- TOC entry 2895 (class 2606 OID 17277)
-- Name: endereco fk_endereco_1; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "fk_endereco_1" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa");


--
-- TOC entry 2894 (class 2606 OID 17268)
-- Name: endereco fk_endereco_4; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "fk_endereco_4" FOREIGN KEY ("fk_cidade_id") REFERENCES "soad"."cidade"("id_cidade");


--
-- TOC entry 2897 (class 2606 OID 17357)
-- Name: estado fk_estado_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "fk_estado_3" FOREIGN KEY ("fk_pais_id") REFERENCES "soad"."pais"("id_pais");


--
-- TOC entry 2881 (class 2606 OID 17377)
-- Name: insumo fk_insumo_2; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "fk_insumo_2" FOREIGN KEY ("fk_produto_id") REFERENCES "soad"."produto"("id_produto") ON DELETE CASCADE;


--
-- TOC entry 2882 (class 2606 OID 17386)
-- Name: insumo fk_insumo_4; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "fk_insumo_4" FOREIGN KEY ("fk_unidade_medida_id") REFERENCES "soad"."unidade_medida"("id_unidade_medida");


--
-- TOC entry 2891 (class 2606 OID 17105)
-- Name: item_lote fk_item_lote_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "fk_item_lote_3" FOREIGN KEY ("fk_lote_id") REFERENCES "soad"."lote"("id_lote");


--
-- TOC entry 2890 (class 2606 OID 17408)
-- Name: item_pedido fk_item_pedido_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "fk_item_pedido_3" FOREIGN KEY ("fk_produto_id") REFERENCES "soad"."produto"("id_produto");


--
-- TOC entry 2889 (class 2606 OID 17399)
-- Name: item_pedido fk_item_pedido_4; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "fk_item_pedido_4" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 2892 (class 2606 OID 17417)
-- Name: lote fk_lote_1; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "fk_lote_1" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 2893 (class 2606 OID 17426)
-- Name: lote fk_lote_4; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "fk_lote_4" FOREIGN KEY ("fk_produto_id") REFERENCES "soad"."produto"("id_produto");


--
-- TOC entry 2885 (class 2606 OID 17256)
-- Name: modalidade_pessoa fk_modalidade_pessoa_1; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "fk_modalidade_pessoa_1" FOREIGN KEY ("fk_modalidade_id") REFERENCES "soad"."modalidade"("id_modalidade") ON DELETE SET NULL;


--
-- TOC entry 2884 (class 2606 OID 17247)
-- Name: modalidade_pessoa fk_modalidade_pessoa_2; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "fk_modalidade_pessoa_2" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE SET NULL;


--
-- TOC entry 2886 (class 2606 OID 17450)
-- Name: pedido fk_pedido_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido"
    ADD CONSTRAINT "fk_pedido_3" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa");


--
-- TOC entry 2876 (class 2606 OID 17463)
-- Name: pessoa_fisica fk_pessoa_fisica_2; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "fk_pessoa_fisica_2" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2877 (class 2606 OID 17483)
-- Name: pessoa_juridica fk_pessoa_juridica_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "fk_pessoa_juridica_3" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2878 (class 2606 OID 17493)
-- Name: produto fk_produto_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."produto"
    ADD CONSTRAINT "fk_produto_3" FOREIGN KEY ("fk_unidade_medida_id") REFERENCES "soad"."unidade_medida"("id_unidade_medida");


--
-- TOC entry 2887 (class 2606 OID 17505)
-- Name: remanufatura fk_remanufatura_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "fk_remanufatura_3" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 2888 (class 2606 OID 17514)
-- Name: remanufatura fk_remanufatura_4; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "fk_remanufatura_4" FOREIGN KEY ("fk_casco_id") REFERENCES "soad"."casco"("id_casco");


--
-- TOC entry 2879 (class 2606 OID 17304)
-- Name: casco fk_toner_2; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "fk_toner_2" FOREIGN KEY ("fk_insumo_id") REFERENCES "soad"."insumo"("id_insumo") ON DELETE CASCADE;


--
-- TOC entry 2880 (class 2606 OID 17313)
-- Name: casco fk_toner_3; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "fk_toner_3" FOREIGN KEY ("fk_produto_id") REFERENCES "soad"."produto"("id_produto") ON DELETE CASCADE;


--
-- TOC entry 2883 (class 2606 OID 17531)
-- Name: usuario fk_usuario_2; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario"
    ADD CONSTRAINT "fk_usuario_2" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE CASCADE;


-- Completed on 2019-07-14 04:24:56

--
-- PostgreSQL database dump complete
--

