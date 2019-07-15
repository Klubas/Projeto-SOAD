--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4
-- Dumped by pg_dump version 11.2

-- Started on 2019-07-15 06:37:50

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
-- TOC entry 3051 (class 1262 OID 13012)
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
-- TOC entry 3052 (class 0 OID 0)
-- Dependencies: 3051
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
-- TOC entry 254 (class 1255 OID 17551)
-- Name: fnc_relatorio_cidades(character varying, character varying, character varying); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_relatorio_cidades"("p_pais" character varying, "p_estado" character varying, "p_cidade" character varying) RETURNS TABLE("cidade_id" integer, "cidade" character varying, "estado_id" integer, "estado" character varying, "pais_id" integer, "pais" character varying)
    LANGUAGE "plpgsql"
    AS $$begin
	return query select t_cidade.id_cidade, t_cidade.cidade, t_cidade.id_estado, t_cidade.estado, t_cidade.id_pais, t_cidade.pais
					from soad.vw_cidade as t_cidade
						where 1=1
						and t_cidade.cidade like p_cidade
						and t_cidade.estado like p_estado
						and t_cidade.pais   like p_pais;
end;
$$;


ALTER FUNCTION "soad"."fnc_relatorio_cidades"("p_pais" character varying, "p_estado" character varying, "p_cidade" character varying) OWNER TO "postgres";

--
-- TOC entry 259 (class 1255 OID 17545)
-- Name: prc_definicoes_iniciais(); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_definicoes_iniciais"()
    LANGUAGE "plpgsql"
    AS $$

BEGIN
	-- Cadastra Unidade de medida
	RAISE NOTICE 'Cadastrando unidades de medida...';
	BEGIN
		CALL soad.prc_insert_or_update_unidade_medida('unidade', 'un');
		CALL soad.prc_insert_or_update_unidade_medida('KILOGRAMA', 'kg');
        CALL soad.prc_insert_or_update_unidade_medida('GRAMA', 'g');
		CALL soad.prc_insert_or_update_unidade_medida('LITRO', 'l');
		CALL soad.prc_insert_or_update_unidade_medida('MILILITRO', 'ml');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das unidades de medida.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;

	-- Cadastra Modalidades
	RAISE NOTICE 'Cadastrando modalidades';
	BEGIN
		CALL soad.prc_insert_modalidade('Cliente'); -- 1
		CALL soad.prc_insert_modalidade('Fornecedor'); -- 2
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das modalidades.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;
	
	-- Cadastra paises
	RAISE NOTICE 'Cadastrando paises...';
	BEGIN
		CALL soad.prc_insert_cidade_estado_pais('', '', '', 'Brasil', 'BR');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro dos paises.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;
	
	-- Cadastra estados
	RAISE NOTICE 'Cadastrando estados...';
	BEGIN
		CALL soad.prc_insert_cidade_estado_pais('', 'Acre', 'AC', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Alagoas', 'AL', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Amapá', 'AP', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Amazonas', 'AM', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Bahia', 'BA', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Ceará', 'CE', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('Brasília', 'Distrito Federal', 'DF', 'Brasil', 'BR');
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
		CALL soad.prc_insert_cidade_estado_pais('Rio de Janeiro', 'Rio de Janeiro', 'RJ', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Rio Grande do Norte', 'RN', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Rio Grande do Sul', 'RS', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Rondônia', 'RO', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Roraima', 'RR', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Santa Catarina', 'SC', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('São Paulo', 'São Paulo', 'SP', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Sergipe', 'SE', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('', 'Tocantins', 'TO', 'Brasil', 'BR');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro dos estados.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;

	-- Cadastra Cidades
	RAISE NOTICE 'Cadastrando cidades...';
	BEGIN
		CALL soad.prc_insert_cidade_estado_pais('Ponta Grossa', 'Paraná', 'PR', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('Curitiba', 'Paraná', 'PR', 'Brasil', 'BR');
		CALL soad.prc_insert_cidade_estado_pais('Castro', 'Paraná', 'PR', 'Brasil', 'BR');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das cidades.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;
	
	-- Cadastra pessoa
	RAISE NOTICE 'Cadastrando pessoas...';
	BEGIN
		CALL soad.prc_insert_pessoa('VIP Cartuchos', '', '4232240660', '00000000000000', '', 'VIP Cartuchos');
		CALL soad.prc_insert_pessoa('EMPRESA TESTE 1', '', '4232240660', '99999999999999', '', 'EMPRESA TESTE 1');
		CALL soad.prc_insert_pessoa('Lucas Klüber', 'lucas.kluber@gmail.com', '42999823030', '10841793930', '', '');
		CALL soad.prc_insert_pessoa('PESSOA TESTE 1', '', '', '00000000000', '', '');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das pessoas.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;
	
   	-- Vincula as pessoas com as modalidades
	RAISE NOTICE 'Definindo modalidades das pessoas cadastradas';
	BEGIN
		DECLARE
			v_aux_id integer := NULL;
		BEGIN
			-- Fornecedores
			SELECT modalidade.id_modalidade INTO v_aux_id FROM soad.modalidade WHERE modalidade.descricao = 'FORNECEDOR';
			CALL soad.prc_vincular_modalidade_pessoa(v_aux_id, '99999999999999');

			-- Clientes
			SELECT modalidade.id_modalidade INTO v_aux_id FROM soad.modalidade WHERE modalidade.descricao = 'CLIENTE';
			CALL soad.prc_vincular_modalidade_pessoa(v_aux_id, '00000000000');

		EXCEPTION WHEN OTHERS THEN
			RAISE NOTICE 'Não foi possível realizar o vinculo .';
			RAISE NOTICE '% %', SQLERRM, SQLSTATE;

		END;
	END;
	
	-- Cadastra endereços das pessoas
	RAISE NOTICE 'Cadastrando endereços...';
	BEGIN
		DECLARE
			v_pessoa_id integer := NULL;
			v_cidade_id integer := NULL;
			
		BEGIN
			SELECT vw_pessoa.id_pessoa INTO v_pessoa_id FROM soad.vw_pessoa
			WHERE vw_pessoa.documento = '10841793930';
			
			SELECT vw_cidade.id_cidade INTO v_cidade_id FROM soad.vw_cidade
			WHERE vw_cidade.cidade = upper('PONTA GROSSA');
			
			CALL soad.prc_insert_endereco(v_pessoa_id, v_cidade_id, 'Rua Comandante Paulo Pinheiro Schimdt', '354', 'Uvaranas', '84031029', '');
			
		EXCEPTION WHEN OTHERS THEN
			RAISE NOTICE 'Não foi possível cadastrar os endereços.';
			RAISE NOTICE '% %', SQLERRM, SQLSTATE;
			
		END;
	END;
    
    RAISE NOTICE 'Cadastrando produtos..';
    BEGIN
        DECLARE
		    v_unidade_medida_id integer := NULL;
		    v_insumo_id integer := NULL;
			
		BEGIN
            -- Produto  
            SELECT unidade_medida.id_unidade_medida INTO v_unidade_medida_id FROM soad.unidade_medida
			WHERE unidade_medida.abreviacao = 'un';
			
            CALL soad.prc_insert_produto('Produto 1', 'Marca 1', v_unidade_medida_id, 'PRODUTO');
			
            -- Insumo
            SELECT unidade_medida.id_unidade_medida INTO v_unidade_medida_id FROM soad.unidade_medida
			WHERE unidade_medida.abreviacao = 'ml';
			
            CALL soad.prc_insert_produto('Insumo 3', 'HP', '107', 'INSUMO', CAST(v_unidade_medida_id AS text), '276');
            
			-- Casco
			SELECT min(insumo.id_insumo) INTO v_insumo_id FROM soad.insumo;
			
            CALL soad.prc_insert_produto('Casco 1', 'HP', '276', 'CASCO', CAST(v_insumo_id AS text), '20');
			
		EXCEPTION WHEN OTHERS THEN
			RAISE NOTICE 'Não foi possível cadastrar os produtos.';
			RAISE NOTICE '% %', SQLERRM, SQLSTATE;
			
        END;
    END;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_definicoes_iniciais"() OWNER TO "postgres";

--
-- TOC entry 255 (class 1255 OID 17567)
-- Name: prc_insert_cidade_estado_pais("text", "text", "text", "text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_cidade_estado_pais"("p_cidade_nome" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text")
    LANGUAGE "plpgsql"
    AS $$DECLARE
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
	
	-- Insere apenas pais OU atualiza o pais
	IF v_cidade_nome = '' AND v_estado_nome = '' AND v_pais_nome <> '' THEN
	
		INSERT INTO soad.pais (nome, sigla)
		VALUES (v_pais_nome, v_pais_sigla); 
		
	RETURN;
	
	-- Insere apenas estado
	ELSIF v_cidade_nome = '' AND v_estado_nome <> '' AND v_pais_nome <> '' THEN

		SELECT id_pais into v_aux FROM soad.pais WHERE pais.sigla = v_pais_sigla;

		INSERT INTO soad.estado (fk_pais_id, nome, sigla)
		VALUES (v_aux, v_estado_nome, v_estado_sigla);
		
	RETURN;
	
	END IF;

   -- Precisa dessa separacao por que se não tiver inserido o registro pai ainda 
   -- o postgres nao acha a chave primaria pra colocar como estrangeira no filho
   
   -------- A partir daqui tenta inserir novo pais, novo estado e nova cidade ---------
	
	-- valida parametros
	IF v_pais_nome = '' OR v_pais_sigla = '' THEN
		RAISE EXCEPTION 'É preciso informar um país.';
	ELSIF v_estado_nome = '' OR v_estado_sigla = '' THEN
		RAISE EXCEPTION 'É preciso informar um estado.';
	ELSIF v_cidade_nome = '' THEN
		RAISE EXCEPTION 'É preciso informar uma cidade';
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
	
	-- Teoricamente nunca chega nessa exception
	RAISE NOTICE 'ERRO: Nenhuma informação foi registrada';

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_cidade_estado_pais"("p_cidade_nome" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text") OWNER TO "postgres";

--
-- TOC entry 256 (class 1255 OID 25434)
-- Name: prc_insert_endereco(integer, integer, "text", "text", "text", "text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_endereco"("p_pessoa_id" integer, "p_cidade_id" integer, "p_logradouro" "text", "p_numero" "text", "p_bairro" "text", "p_cep" "text", "p_complemento" "text")
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pessoa_id integer = p_pessoa_id;
	v_cidade_id integer = p_cidade_id;
	v_logradouro text = p_logradouro;
	v_numero text = p_numero;
	v_bairro text = p_bairro;
	v_cep text = p_cep;
	v_complemento text = p_complemento;

BEGIN

	INSERT INTO soad.endereco(fk_cidade_id, fk_pessoa_id, logradouro, numero, bairro, cep, complemento)
	VALUES (v_cidade_id, v_pessoa_id, v_logradouro, v_numero, v_bairro, v_cep, v_complemento);

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER PROCEDURE "soad"."prc_insert_endereco"("p_pessoa_id" integer, "p_cidade_id" integer, "p_logradouro" "text", "p_numero" "text", "p_bairro" "text", "p_cep" "text", "p_complemento" "text") OWNER TO "postgres";

--
-- TOC entry 252 (class 1255 OID 17241)
-- Name: prc_insert_modalidade("text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_modalidade"("p_modalidade" "text")
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_modalidade text := upper(p_modalidade);
	
BEGIN
	INSERT INTO soad.modalidade (descricao)
	VALUES (v_modalidade);
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_modalidade"("p_modalidade" "text") OWNER TO "postgres";

--
-- TOC entry 253 (class 1255 OID 17541)
-- Name: prc_insert_or_update_unidade_medida("text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_or_update_unidade_medida"("p_descricao" "text", "p_abreviacao" "text")
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_abreviacao text := lower(p_abreviacao);
	v_descricao text := upper(p_descricao);
	
BEGIN
	-- Insere ou atualiza unidade de medida
	-- Não pode atualizar a abreviacao
	INSERT INTO soad.unidade_medida (descricao, abreviacao)
	VALUES (v_descricao, v_abreviacao)
	ON CONFLICT ON CONSTRAINT ukc_unidade_medida_abreviacao
	DO UPDATE SET descricao = v_descricao;
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_or_update_unidade_medida"("p_descricao" "text", "p_abreviacao" "text") OWNER TO "postgres";

--
-- TOC entry 3053 (class 0 OID 0)
-- Dependencies: 253
-- Name: PROCEDURE "prc_insert_or_update_unidade_medida"("p_descricao" "text", "p_abreviacao" "text"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_insert_or_update_unidade_medida"("p_descricao" "text", "p_abreviacao" "text") IS 'Cadastra unidade de medida.
Se a abreviacao ja existir irá atualizar a descrição';


--
-- TOC entry 251 (class 1255 OID 25452)
-- Name: prc_insert_pedido(); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_pedido"()
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	

BEGIN

-- Compra ou venda
-- Vincualar mercadorias
-- Vincular remanufaturas

END;
$$;


ALTER PROCEDURE "soad"."prc_insert_pedido"() OWNER TO "postgres";

--
-- TOC entry 250 (class 1255 OID 17202)
-- Name: prc_insert_pessoa("text", "text", "text", "text", "text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text", "p_fantasia" "text")
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_nome text := p_nome;
	v_email text := p_email;
	v_telefone text := p_telefone;
	v_documento text := p_documento;
	v_inscricao_estadual text := p_inscricao_estadual;
	v_fantasia text := p_fantasia;
	v_data_cadastro date := statement_timestamp();
	
BEGIN

	IF v_inscricao_estadual = '' THEN
		v_inscricao_estadual = 'ISENTO';
	END IF;

	IF length(v_documento) = 14 THEN -- insere pessoa e pessoa juridica
		WITH ins_p AS (
			INSERT INTO soad.pessoa (
				nome
				, email
				, telefone
				, inscricao_estadual
				, data_cadastro
			)
				VALUES (v_nome, v_email, v_telefone, v_inscricao_estadual, v_data_cadastro)	
				RETURNING id_pessoa
		)
		
		INSERT INTO soad.pessoa_juridica (
			fk_pessoa_id, cnpj
			, fantasia
			, data_cadastro
		)
			SELECT id_pessoa, v_documento, v_fantasia, v_data_cadastro
			FROM ins_p;
			

	ELSIF length(v_documento) = 11 THEN 	-- insere pessoa e pessoa fisica
		WITH ins_p AS (
			INSERT INTO soad.pessoa (
				nome
				, email
				, telefone
				, inscricao_estadual
				, data_cadastro
			)
				VALUES (v_nome, v_email, v_telefone, v_inscricao_estadual, v_data_cadastro)	
				RETURNING id_pessoa
		)

		INSERT INTO soad.pessoa_fisica (
			fk_pessoa_id
			, cpf
			, data_cadastro
		) 
		SELECT id_pessoa, v_documento, v_data_cadastro
		FROM ins_p;
		
	END IF;
	
EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text", "p_fantasia" "text") OWNER TO "postgres";

--
-- TOC entry 258 (class 1255 OID 25451)
-- Name: prc_insert_produto("text", "text", integer, "text", "text"[]); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_produto"("p_descricao" "text", "p_marca" "text", "p_unidade_medida_id" integer, "p_tipo" "text", VARIADIC "args" "text"[] DEFAULT NULL::"text"[])
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	-- mercadoria
	v_descricao text 					:= upper(p_descricao);
	v_marca text 						:= upper(p_marca);
	v_unidade_medida_id integer 		:= p_unidade_medida_id;
	v_tipo text 						:= upper(p_tipo);
	
	-- casco
	v_casco_insumo_id integer			:= NULL;
	v_casco_quantidade_insumo real		:= NULL;
	
	-- insumo
	v_insumo_quantidade_embalagem real	:= NULL;
	v_insumo_unidade_medida_id integer	:= NULL;
	v_insumo_permite_venda boolean		:= NULL;
	
BEGIN
	
	-- Inserir produto/mercadoria
	IF v_tipo = 'PRODUTO' THEN
		INSERT INTO soad.mercadoria (descricao, marca, fk_unidade_medida_id, tipo)
		VALUES (v_descricao, v_marca, v_unidade_medida_id, v_tipo);
		
	RETURN;
	
	-- Inserir insumo
	ELSIF v_tipo = 'INSUMO' THEN
    
        IF args[3] IS null THEN args[3] = '0'; END IF;
        
		IF 
			args[1] IS NOT null 
			AND args[2] IS NOT null
			AND args[3] IS NOT null 
		THEN
			v_insumo_quantidade_embalagem	:= args[1];
			v_insumo_unidade_medida_id 		:= args[2];
			v_insumo_permite_venda 			:= args[3];
		ELSE
			RAISE EXCEPTION 'Parametros não podem ser nulos % % %', args[1], args[2], args[3];
		END IF;
			
		WITH t_mercadoria AS (
			INSERT INTO soad.mercadoria (descricao, marca, fk_unidade_medida_id, tipo)
			VALUES (v_descricao, v_marca, v_unidade_medida_id, v_tipo)
			RETURNING id_mercadoria
		) INSERT INTO soad.insumo (fk_mercadoria_id, quantidade_embalagem, fk_unidade_medida_id, permite_venda)
			SELECT id_mercadoria, v_insumo_quantidade_embalagem, v_insumo_unidade_medida_id, v_insumo_permite_venda
			FROM t_mercadoria;
			
	RETURN;
	
	-- Inserir casco
	ELSIF v_tipo = 'CASCO' THEN
		IF 
			args[1] IS NOT null 
			AND args[2] IS NOT null
		THEN
			v_casco_insumo_id			:= args[1];
			v_casco_quantidade_insumo	:= args[2];
		ELSE
			RAISE EXCEPTION 'Parametros não podem ser nulos % %', args[1], args[2];
		END IF;
	
		WITH t_mercadoria AS (
			INSERT INTO soad.mercadoria (descricao, marca, fk_unidade_medida_id, tipo)
			VALUES (v_descricao, v_marca, v_unidade_medida_id, v_tipo)
			RETURNING id_mercadoria
		) INSERT INTO soad.casco (fk_mercadoria_id, fk_insumo_id, quantidade_insumo)
			SELECT id_mercadoria, v_casco_insumo_id, v_casco_quantidade_insumo
			FROM t_mercadoria;
			
	RETURN;
	
	ELSE
	
		RAISE EXCEPTION 'Tipo de mercadoria inválida: %', v_tipo;
	
	END IF;

	-- Não deveria chegar nesse raise
	RAISE EXCEPTION 'Não foi criado nenhum registro';

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER PROCEDURE "soad"."prc_insert_produto"("p_descricao" "text", "p_marca" "text", "p_unidade_medida_id" integer, "p_tipo" "text", VARIADIC "args" "text"[]) OWNER TO "postgres";

--
-- TOC entry 257 (class 1255 OID 25399)
-- Name: prc_vincular_modalidade_pessoa(integer, "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_vincular_modalidade_pessoa"("p_modalidade_id" integer, "p_documento" "text")
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_modalidade_id integer := p_modalidade_id;
	v_documento text := p_documento;
	v_pessoa_id integer := NULL;

BEGIN
	-- Valida parametros
	IF v_modalidade_id is null THEN
		RAISE EXCEPTION 'Informe uma modalidade';
	END IF;
	
	IF v_documento = '' THEN
		RAISE EXCEPTION 'Informe uma pessoa';
	END IF;
	
	-- Valida documento e busca o pessoa.pessoa_id
	IF length(v_documento) = 11 THEN -- CPF
		SELECT fk_pessoa_id INTO v_pessoa_id FROM soad.pessoa_fisica WHERE pessoa_fisica.cpf = v_documento;
		
	ELSIF length(v_documento) = 14 THEN -- CNPJ
		SELECT fk_pessoa_id INTO v_pessoa_id FROM soad.pessoa_juridica WHERE pessoa_juridica.cnpj = v_documento;
		
	ELSE -- Tamanho inválido
		RAISE EXCEPTION 'Documento % é inválido', v_documento;
	END IF;
	
	-- Valida se modalidade existe
	IF (SELECT COUNT(*) FROM soad.modalidade WHERE modalidade.id_modalidade = v_modalidade_id) = 0 THEN 
		RAISE EXCEPTION 'Modalidade ID % não existe', v_modalidade_id;
	END IF;
	
	-- Vincula modalidade com pessoa
	IF v_pessoa_id IS NOT null THEN
		INSERT INTO soad.modalidade_pessoa (fk_modalidade_id, fk_pessoa_id)
		VALUES (v_modalidade_id, v_pessoa_id)
		ON CONFLICT ON CONSTRAINT ukc_modalidade_pessoa_fk_pessoa_id_fk_modalidade_id DO NOTHING;
	ELSE
		RAISE EXCEPTION 'Pessoa não encontrada para o documento %', v_documento;
	END IF;

END;
$$;


ALTER PROCEDURE "soad"."prc_vincular_modalidade_pessoa"("p_modalidade_id" integer, "p_documento" "text") OWNER TO "postgres";

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 208 (class 1259 OID 16916)
-- Name: casco; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."casco" (
    "id_casco" integer NOT NULL,
    "fk_insumo_id" integer NOT NULL,
    "fk_mercadoria_id" integer NOT NULL,
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
-- TOC entry 3054 (class 0 OID 0)
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
    "cep" character varying(8),
    "complemento" character varying(60),
    "tipo" character varying(20)
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
-- TOC entry 3055 (class 0 OID 0)
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
-- TOC entry 3056 (class 0 OID 0)
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
    "fk_mercadoria_id" integer NOT NULL,
    "quantidade_embalagem" real NOT NULL,
    "fk_unidade_medida_id" integer NOT NULL,
    "permite_venda" boolean NOT NULL
);


ALTER TABLE "soad"."insumo" OWNER TO "postgres";

--
-- TOC entry 3057 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN "insumo"."permite_venda"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."insumo"."permite_venda" IS 'Define se esse insumo pode ser vendido para clientes
1 = sim
0 = não';


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
-- TOC entry 3058 (class 0 OID 0)
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
-- TOC entry 3059 (class 0 OID 0)
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
-- TOC entry 3060 (class 0 OID 0)
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
-- TOC entry 3061 (class 0 OID 0)
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
-- TOC entry 3062 (class 0 OID 0)
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
-- TOC entry 3063 (class 0 OID 0)
-- Dependencies: 225
-- Name: lote_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."lote_id_seq" OWNED BY "soad"."lote"."id_lote";


--
-- TOC entry 206 (class 1259 OID 16906)
-- Name: mercadoria; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."mercadoria" (
    "id_mercadoria" integer NOT NULL,
    "fk_unidade_medida_id" integer NOT NULL,
    "descricao" character varying(120) NOT NULL,
    "marca" character varying(80),
    "tipo" character varying(10) DEFAULT 'PRODUTO'::character varying NOT NULL,
    CONSTRAINT "cc_mercadoria_tipo" CHECK (((("tipo")::"text" = 'PRODUTO'::"text") OR (("tipo")::"text" = 'INSUMO'::"text") OR (("tipo")::"text" = 'CASCO'::"text")))
);


ALTER TABLE "soad"."mercadoria" OWNER TO "postgres";

--
-- TOC entry 3064 (class 0 OID 0)
-- Dependencies: 206
-- Name: COLUMN "mercadoria"."tipo"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."mercadoria"."tipo" IS 'PRODUTO
INSUMO
CASO';


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
-- TOC entry 3065 (class 0 OID 0)
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
-- TOC entry 3066 (class 0 OID 0)
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
-- TOC entry 3067 (class 0 OID 0)
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
    CONSTRAINT "cc_pedido_situacao" CHECK (((("situacao")::"text" = 'CADASTRADO'::"text") OR (("situacao")::"text" = 'ENCERRADO'::"text") OR (("situacao")::"text" = 'CANCELADO'::"text")))
);


ALTER TABLE "soad"."pedido" OWNER TO "postgres";

--
-- TOC entry 3068 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN "pedido"."tipo_pedido"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."pedido"."tipo_pedido" IS '0 = Entrada
1 = Saida';


--
-- TOC entry 3069 (class 0 OID 0)
-- Dependencies: 218
-- Name: CONSTRAINT "cc_pedido_situacao" ON "pedido"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "cc_pedido_situacao" ON "soad"."pedido" IS 'Define as situacoes permitidas para o pedido';


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
-- TOC entry 3070 (class 0 OID 0)
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
    "data_cadastro" "date" NOT NULL,
    "inscricao_estadual" character varying(20)
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
-- TOC entry 3071 (class 0 OID 0)
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
-- TOC entry 3072 (class 0 OID 0)
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
-- TOC entry 3073 (class 0 OID 0)
-- Dependencies: 201
-- Name: pessoa_juridica_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."pessoa_juridica_id_seq" OWNED BY "soad"."pessoa_juridica"."id_pessoa_juridica";


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
-- TOC entry 3074 (class 0 OID 0)
-- Dependencies: 205
-- Name: produto_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."produto_id_seq" OWNED BY "soad"."mercadoria"."id_mercadoria";


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
-- TOC entry 3075 (class 0 OID 0)
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
-- TOC entry 3076 (class 0 OID 0)
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
-- TOC entry 3077 (class 0 OID 0)
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
-- TOC entry 3078 (class 0 OID 0)
-- Dependencies: 211
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."usuario_id_seq" OWNED BY "soad"."usuario"."id_usuario";


--
-- TOC entry 236 (class 1259 OID 25418)
-- Name: vw_cidade; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_cidade" AS
 SELECT "cidade"."id_cidade",
    "cidade"."nome" AS "cidade",
    "estado"."id_estado",
    "estado"."nome" AS "estado",
    "pais"."id_pais",
    "pais"."nome" AS "pais"
   FROM (("soad"."cidade"
     JOIN "soad"."estado" ON (("cidade"."fk_estado_id" = "estado"."id_estado")))
     JOIN "soad"."pais" ON (("estado"."fk_pais_id" = "pais"."id_pais")));


ALTER TABLE "soad"."vw_cidade" OWNER TO "postgres";

--
-- TOC entry 237 (class 1259 OID 25426)
-- Name: vw_pessoa; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_pessoa" AS
 SELECT "pessoa"."id_pessoa",
    "pessoa"."nome",
    "pessoa"."email",
    "pessoa"."telefone",
    "concat"("pessoa_fisica"."cpf", "pessoa_juridica"."cnpj") AS "documento",
    "pessoa"."inscricao_estadual",
    "pessoa_juridica"."fantasia"
   FROM (("soad"."pessoa"
     LEFT JOIN "soad"."pessoa_fisica" ON (("pessoa"."id_pessoa" = "pessoa_fisica"."fk_pessoa_id")))
     LEFT JOIN "soad"."pessoa_juridica" ON (("pessoa"."id_pessoa" = "pessoa_juridica"."fk_pessoa_id")));


ALTER TABLE "soad"."vw_pessoa" OWNER TO "postgres";

--
-- TOC entry 2823 (class 2604 OID 16919)
-- Name: casco id_casco; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco" ALTER COLUMN "id_casco" SET DEFAULT "nextval"('"soad"."toner_id_seq"'::"regclass");


--
-- TOC entry 2835 (class 2604 OID 17009)
-- Name: cidade id_cidade; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade" ALTER COLUMN "id_cidade" SET DEFAULT "nextval"('"soad"."cidade_id_seq"'::"regclass");


--
-- TOC entry 2834 (class 2604 OID 17001)
-- Name: endereco id_endereco; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco" ALTER COLUMN "id_endereco" SET DEFAULT "nextval"('"soad"."endereco_id_seq"'::"regclass");


--
-- TOC entry 2836 (class 2604 OID 17017)
-- Name: estado id_estado; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado" ALTER COLUMN "id_estado" SET DEFAULT "nextval"('"soad"."estado_id_seq"'::"regclass");


--
-- TOC entry 2824 (class 2604 OID 16927)
-- Name: insumo id_insumo; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo" ALTER COLUMN "id_insumo" SET DEFAULT "nextval"('"soad"."insumo_id_seq"'::"regclass");


--
-- TOC entry 2832 (class 2604 OID 16985)
-- Name: item_lote id_item_lote_id; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote" ALTER COLUMN "id_item_lote_id" SET DEFAULT "nextval"('"soad"."item_lote_id_seq"'::"regclass");


--
-- TOC entry 2831 (class 2604 OID 16977)
-- Name: item_pedido id_item_pedido; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido" ALTER COLUMN "id_item_pedido" SET DEFAULT "nextval"('"soad"."item_pedido_id_seq"'::"regclass");


--
-- TOC entry 2833 (class 2604 OID 16993)
-- Name: lote id_lote; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote" ALTER COLUMN "id_lote" SET DEFAULT "nextval"('"soad"."lote_id_seq"'::"regclass");


--
-- TOC entry 2820 (class 2604 OID 16909)
-- Name: mercadoria id_mercadoria; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."mercadoria" ALTER COLUMN "id_mercadoria" SET DEFAULT "nextval"('"soad"."produto_id_seq"'::"regclass");


--
-- TOC entry 2817 (class 2604 OID 16883)
-- Name: modalidade id_modalidade; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade" ALTER COLUMN "id_modalidade" SET DEFAULT "nextval"('"soad"."modalidade_id_seq"'::"regclass");


--
-- TOC entry 2826 (class 2604 OID 16943)
-- Name: modalidade_pessoa id_modalidade_pessoa; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa" ALTER COLUMN "id_modalidade_pessoa" SET DEFAULT "nextval"('"soad"."modalidade_pessoa_id_seq"'::"regclass");


--
-- TOC entry 2837 (class 2604 OID 17025)
-- Name: pais id_pais; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais" ALTER COLUMN "id_pais" SET DEFAULT "nextval"('"soad"."pais_id_seq"'::"regclass");


--
-- TOC entry 2828 (class 2604 OID 16961)
-- Name: pedido id_pedido; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido" ALTER COLUMN "id_pedido" SET DEFAULT "nextval"('"soad"."pedido_id_seq"'::"regclass");


--
-- TOC entry 2819 (class 2604 OID 16901)
-- Name: pessoa id_pessoa; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa" ALTER COLUMN "id_pessoa" SET DEFAULT "nextval"('"soad"."pessoa_id_seq"'::"regclass");


--
-- TOC entry 2816 (class 2604 OID 16873)
-- Name: pessoa_fisica id_pessoa_fisica; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica" ALTER COLUMN "id_pessoa_fisica" SET DEFAULT "nextval"('"soad"."pessoa_fisica_id_seq"'::"regclass");


--
-- TOC entry 2818 (class 2604 OID 16891)
-- Name: pessoa_juridica id_pessoa_juridica; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica" ALTER COLUMN "id_pessoa_juridica" SET DEFAULT "nextval"('"soad"."pessoa_juridica_id_seq"'::"regclass");


--
-- TOC entry 2830 (class 2604 OID 16969)
-- Name: remanufatura id_remanufatura; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura" ALTER COLUMN "id_remanufatura" SET DEFAULT "nextval"('"soad"."remanufatura_id_seq"'::"regclass");


--
-- TOC entry 2827 (class 2604 OID 16951)
-- Name: unidade_medida id_unidade_medida; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida" ALTER COLUMN "id_unidade_medida" SET DEFAULT "nextval"('"soad"."unidade_medida_id_seq"'::"regclass");


--
-- TOC entry 2825 (class 2604 OID 16935)
-- Name: usuario id_usuario; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario" ALTER COLUMN "id_usuario" SET DEFAULT "nextval"('"soad"."usuario_id_seq"'::"regclass");


--
-- TOC entry 2889 (class 2606 OID 17011)
-- Name: cidade pkc_id_cidade; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade"
    ADD CONSTRAINT "pkc_id_cidade" PRIMARY KEY ("id_cidade");


--
-- TOC entry 2885 (class 2606 OID 17003)
-- Name: endereco pkc_id_endereco; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "pkc_id_endereco" PRIMARY KEY ("id_endereco");


--
-- TOC entry 2893 (class 2606 OID 17019)
-- Name: estado pkc_id_estado; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "pkc_id_estado" PRIMARY KEY ("id_estado");


--
-- TOC entry 2863 (class 2606 OID 16929)
-- Name: insumo pkc_id_insumo; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "pkc_id_insumo" PRIMARY KEY ("id_insumo");


--
-- TOC entry 2881 (class 2606 OID 16987)
-- Name: item_lote pkc_id_item_lote; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "pkc_id_item_lote" PRIMARY KEY ("id_item_lote_id");


--
-- TOC entry 2879 (class 2606 OID 16979)
-- Name: item_pedido pkc_id_item_pedido; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "pkc_id_item_pedido" PRIMARY KEY ("id_item_pedido");


--
-- TOC entry 2883 (class 2606 OID 16995)
-- Name: lote pkc_id_lote; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "pkc_id_lote" PRIMARY KEY ("id_lote");


--
-- TOC entry 2857 (class 2606 OID 16911)
-- Name: mercadoria pkc_id_mercadoria; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."mercadoria"
    ADD CONSTRAINT "pkc_id_mercadoria" PRIMARY KEY ("id_mercadoria");


--
-- TOC entry 2845 (class 2606 OID 16885)
-- Name: modalidade pkc_id_modalidade; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade"
    ADD CONSTRAINT "pkc_id_modalidade" PRIMARY KEY ("id_modalidade");


--
-- TOC entry 2867 (class 2606 OID 16945)
-- Name: modalidade_pessoa pkc_id_modalidade_pessoa; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "pkc_id_modalidade_pessoa" PRIMARY KEY ("id_modalidade_pessoa");


--
-- TOC entry 2897 (class 2606 OID 17027)
-- Name: pais pkc_id_pais; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais"
    ADD CONSTRAINT "pkc_id_pais" PRIMARY KEY ("id_pais");


--
-- TOC entry 2875 (class 2606 OID 16963)
-- Name: pedido pkc_id_pedido; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido"
    ADD CONSTRAINT "pkc_id_pedido" PRIMARY KEY ("id_pedido");


--
-- TOC entry 2855 (class 2606 OID 16903)
-- Name: pessoa pkc_id_pessoa; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa"
    ADD CONSTRAINT "pkc_id_pessoa" PRIMARY KEY ("id_pessoa");


--
-- TOC entry 2839 (class 2606 OID 16875)
-- Name: pessoa_fisica pkc_id_pessoa_fisica; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "pkc_id_pessoa_fisica" PRIMARY KEY ("id_pessoa_fisica");


--
-- TOC entry 2849 (class 2606 OID 16893)
-- Name: pessoa_juridica pkc_id_pessoa_juridica; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "pkc_id_pessoa_juridica" PRIMARY KEY ("id_pessoa_juridica");


--
-- TOC entry 2877 (class 2606 OID 16971)
-- Name: remanufatura pkc_id_remanufatura; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "pkc_id_remanufatura" PRIMARY KEY ("id_remanufatura");


--
-- TOC entry 2861 (class 2606 OID 16921)
-- Name: casco pkc_id_toner; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "pkc_id_toner" PRIMARY KEY ("id_casco");


--
-- TOC entry 2871 (class 2606 OID 16953)
-- Name: unidade_medida pkc_id_unidade_medida; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida"
    ADD CONSTRAINT "pkc_id_unidade_medida" PRIMARY KEY ("id_unidade_medida");


--
-- TOC entry 2865 (class 2606 OID 16937)
-- Name: usuario pkc_id_usuario; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario"
    ADD CONSTRAINT "pkc_id_usuario" PRIMARY KEY ("id_usuario");


--
-- TOC entry 2891 (class 2606 OID 17566)
-- Name: cidade ukc_cidade_nome_fk_estado_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade"
    ADD CONSTRAINT "ukc_cidade_nome_fk_estado_id" UNIQUE ("nome", "fk_estado_id");


--
-- TOC entry 3079 (class 0 OID 0)
-- Dependencies: 2891
-- Name: CONSTRAINT "ukc_cidade_nome_fk_estado_id" ON "cidade"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "ukc_cidade_nome_fk_estado_id" ON "soad"."cidade" IS 'Cada cidade deve ser única no estado';


--
-- TOC entry 2887 (class 2606 OID 25438)
-- Name: endereco ukc_endereco_pessoa_id_cidade_id_logradouro_numero_bairro_cep; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "ukc_endereco_pessoa_id_cidade_id_logradouro_numero_bairro_cep" UNIQUE ("fk_pessoa_id") INCLUDE ("fk_cidade_id", "logradouro", "numero", "bairro", "cep");


--
-- TOC entry 2895 (class 2606 OID 17557)
-- Name: estado ukc_estado_sigla_fk_pais_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "ukc_estado_sigla_fk_pais_id" UNIQUE ("sigla") INCLUDE ("fk_pais_id");


--
-- TOC entry 3080 (class 0 OID 0)
-- Dependencies: 2895
-- Name: CONSTRAINT "ukc_estado_sigla_fk_pais_id" ON "estado"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "ukc_estado_sigla_fk_pais_id" ON "soad"."estado" IS 'Cada estado deve ser unico no pais';


--
-- TOC entry 2859 (class 2606 OID 25432)
-- Name: mercadoria ukc_mercadoria_descricao; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."mercadoria"
    ADD CONSTRAINT "ukc_mercadoria_descricao" UNIQUE ("descricao");


--
-- TOC entry 2847 (class 2606 OID 17571)
-- Name: modalidade ukc_modalidade_descricao; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade"
    ADD CONSTRAINT "ukc_modalidade_descricao" UNIQUE ("descricao");


--
-- TOC entry 2869 (class 2606 OID 17573)
-- Name: modalidade_pessoa ukc_modalidade_pessoa_fk_pessoa_id_fk_modalidade_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "ukc_modalidade_pessoa_fk_pessoa_id_fk_modalidade_id" UNIQUE ("fk_pessoa_id") INCLUDE ("fk_modalidade_id");


--
-- TOC entry 2899 (class 2606 OID 17553)
-- Name: pais ukc_pais_sigla; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais"
    ADD CONSTRAINT "ukc_pais_sigla" UNIQUE ("sigla");


--
-- TOC entry 2841 (class 2606 OID 17577)
-- Name: pessoa_fisica ukc_pessoa_fisica_cpf; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "ukc_pessoa_fisica_cpf" UNIQUE ("cpf");


--
-- TOC entry 3081 (class 0 OID 0)
-- Dependencies: 2841
-- Name: CONSTRAINT "ukc_pessoa_fisica_cpf" ON "pessoa_fisica"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "ukc_pessoa_fisica_cpf" ON "soad"."pessoa_fisica" IS 'cpf deve ser unico';


--
-- TOC entry 2843 (class 2606 OID 17581)
-- Name: pessoa_fisica ukc_pessoa_fisica_fk_pessoa; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "ukc_pessoa_fisica_fk_pessoa" UNIQUE ("fk_pessoa_id");


--
-- TOC entry 2851 (class 2606 OID 17579)
-- Name: pessoa_juridica ukc_pessoa_juridica_cnpj; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "ukc_pessoa_juridica_cnpj" UNIQUE ("cnpj");


--
-- TOC entry 3082 (class 0 OID 0)
-- Dependencies: 2851
-- Name: CONSTRAINT "ukc_pessoa_juridica_cnpj" ON "pessoa_juridica"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "ukc_pessoa_juridica_cnpj" ON "soad"."pessoa_juridica" IS 'cnpj deve ser unico';


--
-- TOC entry 2853 (class 2606 OID 17583)
-- Name: pessoa_juridica ukc_pessoa_juridica_fk_pessoa; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "ukc_pessoa_juridica_fk_pessoa" UNIQUE ("fk_pessoa_id");


--
-- TOC entry 2873 (class 2606 OID 17569)
-- Name: unidade_medida ukc_unidade_medida_abreviacao; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida"
    ADD CONSTRAINT "ukc_unidade_medida_abreviacao" UNIQUE ("abreviacao");


--
-- TOC entry 2920 (class 2606 OID 17291)
-- Name: cidade fkc_cidade_estado_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."cidade"
    ADD CONSTRAINT "fkc_cidade_estado_id" FOREIGN KEY ("fk_estado_id") REFERENCES "soad"."estado"("id_estado");


--
-- TOC entry 2919 (class 2606 OID 17268)
-- Name: endereco fkc_endereco_cidade_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "fkc_endereco_cidade_id" FOREIGN KEY ("fk_cidade_id") REFERENCES "soad"."cidade"("id_cidade");


--
-- TOC entry 2918 (class 2606 OID 17277)
-- Name: endereco fkc_endereco_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "fkc_endereco_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa");


--
-- TOC entry 2921 (class 2606 OID 17357)
-- Name: estado fkc_estado_pais_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "fkc_estado_pais_id" FOREIGN KEY ("fk_pais_id") REFERENCES "soad"."pais"("id_pais");


--
-- TOC entry 2906 (class 2606 OID 17377)
-- Name: insumo fkc_insumo_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "fkc_insumo_mercadoria_id" FOREIGN KEY ("fk_mercadoria_id") REFERENCES "soad"."mercadoria"("id_mercadoria") ON DELETE CASCADE;


--
-- TOC entry 2905 (class 2606 OID 17386)
-- Name: insumo fkc_insumo_unidade_medida_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "fkc_insumo_unidade_medida_id" FOREIGN KEY ("fk_unidade_medida_id") REFERENCES "soad"."unidade_medida"("id_unidade_medida");


--
-- TOC entry 2915 (class 2606 OID 17105)
-- Name: item_lote fkc_item_lote_lote_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "fkc_item_lote_lote_id" FOREIGN KEY ("fk_lote_id") REFERENCES "soad"."lote"("id_lote");


--
-- TOC entry 2914 (class 2606 OID 17408)
-- Name: item_pedido fkc_item_pedido_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "fkc_item_pedido_mercadoria_id" FOREIGN KEY ("fk_produto_id") REFERENCES "soad"."mercadoria"("id_mercadoria");


--
-- TOC entry 2913 (class 2606 OID 17399)
-- Name: item_pedido fkc_item_pedido_pedido_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "fkc_item_pedido_pedido_id" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 2916 (class 2606 OID 17426)
-- Name: lote fkc_lote_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "fkc_lote_mercadoria_id" FOREIGN KEY ("fk_produto_id") REFERENCES "soad"."mercadoria"("id_mercadoria");


--
-- TOC entry 2917 (class 2606 OID 17417)
-- Name: lote fkc_lote_pedido_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "fkc_lote_pedido_id" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 2902 (class 2606 OID 17493)
-- Name: mercadoria fkc_mercadoria_unidade_medida_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."mercadoria"
    ADD CONSTRAINT "fkc_mercadoria_unidade_medida_id" FOREIGN KEY ("fk_unidade_medida_id") REFERENCES "soad"."unidade_medida"("id_unidade_medida");


--
-- TOC entry 2909 (class 2606 OID 17256)
-- Name: modalidade_pessoa fkc_modalidade_pessoa_modalidade_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "fkc_modalidade_pessoa_modalidade_id" FOREIGN KEY ("fk_modalidade_id") REFERENCES "soad"."modalidade"("id_modalidade") ON DELETE SET NULL;


--
-- TOC entry 2908 (class 2606 OID 17247)
-- Name: modalidade_pessoa fkc_modalidade_pessoa_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "fkc_modalidade_pessoa_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE SET NULL;


--
-- TOC entry 2910 (class 2606 OID 17450)
-- Name: pedido fkc_pedido_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido"
    ADD CONSTRAINT "fkc_pedido_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa");


--
-- TOC entry 2900 (class 2606 OID 17463)
-- Name: pessoa_fisica fkc_pessoa_fisica_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "fkc_pessoa_fisica_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2901 (class 2606 OID 17483)
-- Name: pessoa_juridica fkc_pessoa_juridica_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "fkc_pessoa_juridica_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2911 (class 2606 OID 17514)
-- Name: remanufatura fkc_remanufatura_casco_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "fkc_remanufatura_casco_id" FOREIGN KEY ("fk_casco_id") REFERENCES "soad"."casco"("id_casco");


--
-- TOC entry 2912 (class 2606 OID 17505)
-- Name: remanufatura fkc_remanufatura_pedido_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "fkc_remanufatura_pedido_id" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 2904 (class 2606 OID 17304)
-- Name: casco fkc_toner_insumo_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "fkc_toner_insumo_id" FOREIGN KEY ("fk_insumo_id") REFERENCES "soad"."insumo"("id_insumo") ON DELETE CASCADE;


--
-- TOC entry 2903 (class 2606 OID 17313)
-- Name: casco fkc_toner_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "fkc_toner_mercadoria_id" FOREIGN KEY ("fk_mercadoria_id") REFERENCES "soad"."mercadoria"("id_mercadoria") ON DELETE CASCADE;


--
-- TOC entry 2907 (class 2606 OID 17531)
-- Name: usuario fkc_usuario_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario"
    ADD CONSTRAINT "fkc_usuario_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE CASCADE;


-- Completed on 2019-07-15 06:37:50

--
-- PostgreSQL database dump complete
--

