--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4
-- Dumped by pg_dump version 11.3

-- Started on 2019-09-07 18:28:02

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "postgres";
--
-- TOC entry 3225 (class 1262 OID 13012)
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
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3226 (class 0 OID 0)
-- Dependencies: 3225
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
-- TOC entry 289 (class 1255 OID 82805)
-- Name: fnc_buscar_registro("text", "text", "text", "text"); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_buscar_registro"("p_tabela" "text", "p_coluna" "text", "p_valor" "text" DEFAULT ''::"text", "p_operador" "text" DEFAULT '='::"text") RETURNS "json"
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_schema text := 'soad';
	v_tabela text := p_tabela;
	v_coluna text := p_coluna;
	v_valor text := upper(p_valor);
	v_operador text := p_operador;
	
	v_tipo text;
	v_colunas text;
	sql_query text;
	
	v_linha RECORD;
	v_json_linha json;
	v_array json ARRAY;
	v_json_array json;
	

BEGIN
	-- Identifica todas as coluna da tabela "v_tabela"
	v_colunas := array_to_string(ARRAY(
		SELECT c.column_name 
		FROM information_schema.columns As c 
		WHERE table_name = v_tabela
	), ',');
	
	SELECT 
		(CASE
			-- Tratamento para tipo do campo utilizado para busca
			WHEN c.data_type = 'character varying' THEN 'text' 
			ELSE c.data_type
		END) AS tipo
	INTO v_tipo 
	FROM information_schema.columns AS c 
	WHERE table_name = v_tabela
	AND column_name = v_coluna ;
	
	-- select básico da busca
	sql_query := 'SELECT ' || v_colunas || ' FROM ' || v_schema || '.' || v_tabela;
	
	-- se tiver condicional vai fazer o tratamento aqui
	IF p_valor <> '' THEN
		-- Trata o tipo de operador "like" ou "="
		IF v_operador = 'like' THEN
			v_valor := '%' || v_valor || '%';
			v_coluna := 'upper(' || v_coluna || ')';
		END IF;
		
		-- Se for texto vai colocar quotes
		IF v_tipo = 'text' THEN
			v_valor = '''' || upper(v_valor) || '''';
		END IF;
		
		-- monta condicional da SQL
		sql_query := sql_query || ' WHERE ' || v_coluna  || ' ' || v_operador || ' ' || v_valor || '::' || v_tipo || ';';
		
	END IF;
		
	RAISE NOTICE '%', sql_query;
		
	BEGIN
		-- Busca todas as linhas de resultado
		FOR v_linha IN EXECUTE sql_query LOOP
			-- Transformar a linha em um json
			v_json_linha := row_to_json(v_linha);
			-- Adiciona esse json a um array de jsons
			v_array := v_array || v_json_linha;
		END LOOP;
		
		-- Retorna o array como um unico json com todas as linhas
		RETURN array_to_json(v_array);
	END;
	

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER FUNCTION "soad"."fnc_buscar_registro"("p_tabela" "text", "p_coluna" "text", "p_valor" "text", "p_operador" "text") OWNER TO "postgres";

--
-- TOC entry 3227 (class 0 OID 0)
-- Dependencies: 289
-- Name: FUNCTION "fnc_buscar_registro"("p_tabela" "text", "p_coluna" "text", "p_valor" "text", "p_operador" "text"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON FUNCTION "soad"."fnc_buscar_registro"("p_tabela" "text", "p_coluna" "text", "p_valor" "text", "p_operador" "text") IS 'Retorna json com registros de acordo com os parâmetros definidos';


--
-- TOC entry 302 (class 1255 OID 99137)
-- Name: fnc_cadastro_pedido("text", integer, "text", "date", "json", integer); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_cadastro_pedido"("p_tipo_pedido" "text", "p_pessoa_id" integer, "p_observacao" "text" DEFAULT NULL::"text", "p_data_entrega" "date" DEFAULT NULL::"date", "p_itens" "json" DEFAULT NULL::"json", "p_pedido_id" integer DEFAULT NULL::integer, OUT "pedido_id" integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	-- Retorno
	v_pedido_id 	integer := p_pedido_id;
	
	-- Pedido
	v_tipo_pedido 	text 	:= p_tipo_pedido;
	v_situacao 		text;
    v_pessoa_id 	integer := p_pessoa_id;
	v_observacao 	text	:= p_observacao;
	v_data_entrega 	date	:= p_data_entrega;
	
	-- manipular json
	v_json_itens	json	:= p_itens;
	v_json_temp		json	:= NULL;
	
    -- Define qual o tipo de item sendo inserido
	v_tipo_item 	text;

	-- Se aplica Mercadoria
	v_mercadoria_id 	integer	:= NULL;
	v_unidade_medida_id integer := NULL;
	v_item_pedido_id	integer := NULL;
	
	-- Se aplica a Remanufatura
	v_casco_id 			integer := NULL;
	v_insumo_id			integer := NULL;
	v_nova_remanufatura boolean	:= TRUE;
	
	-- Se aplicam aos dois tipos
	v_quantidade 	 real;
	v_valor_unitario real;
	

BEGIN
	
    -- se for edição, desvincula mercadorias e remanufaturas para refazer o processo
	IF v_pedido_id IS NOT NULL THEN
		-- valida situação
		v_situacao := (SELECT pedido.situacao FROM soad.pedido WHERE id_pedido = v_pedido_id);
		IF v_situacao <> 'CADASTRADO' THEN 
			IF v_situacao <> 'ESTORNADO'  THEN
				RAISE EXCEPTION 'Não é possível editar um pedido %. O pedido precisa estar CADASTRADO ou ESTORNADO', v_situacao;
			END IF;
		END IF;
		
		CALL soad.prc_desvincular_remanufaturas_pedido(p_pedido_id=>v_pedido_id);
		
	END IF;
	
	-- Cadastra/edita pedido
	BEGIN
		v_pedido_id := soad.fnc_insert_pedido(v_tipo_pedido, v_pessoa_id, v_observacao, v_data_entrega);
		RAISE NOTICE 'JSON: %', v_json_itens;
	END;
	
	-- Desmonta a 'lista de jsons' do parametro em jsons separados e percorre
	BEGIN
		FOR v_json_temp IN 
			SELECT value
			FROM json_array_elements(v_json_itens) 
		-- Loop para vincular item de acordo com o tipo
		LOOP 

			v_tipo_item			:= v_json_temp::json->'tipo_item';
			v_tipo_item			:= trim('"' FROM v_tipo_item::text);
			v_quantidade		:= v_json_temp::json->'quantidade';
			v_valor_unitario	:= v_json_temp::json->'valor_unitario';

			IF v_tipo_item = 'REMANUFATURA' THEN
				v_casco_id 			:= v_json_temp::json->'casco_id';
				v_nova_remanufatura := v_json_temp::json->'nova_remanufatura';
				v_insumo_id			:= v_json_temp::json->'insumo_id';
				
				BEGIN
				
					CALL soad.prc_vincular_pedido_remanufatura(v_pedido_id, v_casco_id, v_insumo_id, v_quantidade, v_valor_unitario, v_nova_remanufatura);
					
				END;

			ELSIF v_tipo_item = 'MERCADORIA' THEN
				v_mercadoria_id  	:= v_json_temp::json->'mercadoria_id';
				v_unidade_medida_id	:= v_json_temp::json->'unidade_medida_id';
				v_item_pedido_id	:= v_json_temp::json->'item_pedido_id';
				
				v_item_pedido_id := (
					CASE WHEN v_item_pedido_id > 0 THEN v_item_pedido_id::integer ELSE NULL END
				);
				
				BEGIN
					
					CALL soad.prc_vincular_pedido_mercadoria(v_pedido_id, v_mercadoria_id, v_unidade_medida_id, v_quantidade, v_valor_unitario);
					
				END;

			ELSE 
				RAISE EXCEPTION 'Tipo de item (%) inválido.', v_tipo_item;

			END IF;

		END LOOP;
	END;
	
	pedido_id := v_pedido_id;
	RETURN;
	
EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
	
END;
$$;


ALTER FUNCTION "soad"."fnc_cadastro_pedido"("p_tipo_pedido" "text", "p_pessoa_id" integer, "p_observacao" "text", "p_data_entrega" "date", "p_itens" "json", "p_pedido_id" integer, OUT "pedido_id" integer) OWNER TO "postgres";

--
-- TOC entry 3228 (class 0 OID 0)
-- Dependencies: 302
-- Name: FUNCTION "fnc_cadastro_pedido"("p_tipo_pedido" "text", "p_pessoa_id" integer, "p_observacao" "text", "p_data_entrega" "date", "p_itens" "json", "p_pedido_id" integer, OUT "pedido_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON FUNCTION "soad"."fnc_cadastro_pedido"("p_tipo_pedido" "text", "p_pessoa_id" integer, "p_observacao" "text", "p_data_entrega" "date", "p_itens" "json", "p_pedido_id" integer, OUT "pedido_id" integer) IS 'Cadastra e atualiza informações do pedido';


--
-- TOC entry 298 (class 1255 OID 99173)
-- Name: fnc_cadastro_pessoa("text", "text", "text", "text", "text", "text", "text", "json", "json"); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_cadastro_pessoa"("p_nome" "text", "p_documento" "text", "p_email" "text" DEFAULT NULL::"text", "p_telefone" "text" DEFAULT NULL::"text", "p_inscricao_estadual" "text" DEFAULT 'ISENTO'::"text", "p_fantasia" "text" DEFAULT NULL::"text", "p_pessoa_id" "text" DEFAULT NULL::"text", "p_endereco" "json" DEFAULT NULL::"json", "p_modalidade" "json" DEFAULT NULL::"json", OUT "pessoa_id" integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE 

	v_pessoa_id 	integer;
	
	-- endereco
	v_municipio_id  integer;
	v_logradouro	text;
	v_numero		text;
	v_bairro		text;
	v_cep			text;
	v_complemento	text;
	v_tipo			text;
	v_endereco_id	text;
	
	-- modalidade
	v_modalidade_id	integer;
	v_documento		text;
	
	-- manipular json
	v_json_endereco		json	:= p_endereco;
	v_json_modalidade	json	:= p_modalidade;
	v_json_temp			json	:= NULL;
	

BEGIN
	-- Cadastra pessoa
	
	SELECT nova_pessoa.pessoa_id INTO v_pessoa_id 
	FROM soad.fnc_insert_update_pessoa(
		p_nome=>p_nome
		, p_email=>p_email
		, p_telefone=>p_telefone
		, p_documento=>p_documento
		, p_inscricao_estadual=>p_inscricao_estadual
		, p_fantasia=>p_fantasia
		, p_pessoa_id=>p_pessoa_id
	) as nova_pessoa;
	
	pessoa_id := v_pessoa_id;
	
	-- Vincula endereços
	
	BEGIN
		FOR v_json_temp IN 
			SELECT value FROM json_array_elements(v_json_endereco) 
		LOOP -- Loop para cadastrar endereco
			
			v_municipio_id			:= trim('"' FROM (v_json_temp::json->'id_municipio')::text);
			v_logradouro			:= trim('"' FROM (v_json_temp::json->'logradouro')::text);
			v_numero				:= trim('"' FROM (v_json_temp::json->'numero')::text);
			v_bairro				:= trim('"' FROM (v_json_temp::json->'bairro')::text);
			v_cep 					:= trim('"' FROM (v_json_temp::json->'cep')::text);
			v_complemento			:= trim('"' FROM (v_json_temp::json->'complemento')::text);
			v_tipo					:= trim('"' FROM (v_json_temp::json->'tipo')::text);
			v_endereco_id			:= trim('"' FROM (v_json_temp::json->'id_endereco')::text);
			
			IF v_endereco_id = '' THEN
				v_endereco_id = NULL;
			END IF;
			
			BEGIN
				SELECT endereco_id INTO v_endereco_id
				FROM soad.fnc_insert_update_endereco(
					v_pessoa_id::integer
					, v_municipio_id::integer
					, v_logradouro
					, v_numero
					, v_bairro
					, v_cep
					, v_complemento
					, v_tipo
					, v_endereco_id::integer
				);
			END;
			
		END LOOP;
			
		EXCEPTION WHEN no_data_found THEN
			RAISE NOTICE 'Sem endereços.';
	END;
	
	-- Desvincula todas as modalidades
	BEGIN
		DELETE FROM soad.modalidade_pessoa
		WHERE fk_pessoa_id=v_pessoa_id;
	END;
	
	-- Vincula modalidades
	BEGIN
		FOR v_modalidade_id IN 
			SELECT value FROM json_array_elements(v_json_modalidade) 
		LOOP -- Loop para vincular modalidade
			
			SELECT documento INTO v_documento 
			FROM soad.vw_pessoa 
			WHERE id_pessoa = v_pessoa_id;
		
			BEGIN
				CALL soad.prc_vincular_modalidade_pessoa(
					v_modalidade_id::integer
					, v_documento::text
				);
			END;

		END LOOP;
		
		EXCEPTION WHEN no_data_found THEN
			RAISE NOTICE 'Sem modalidades.';
	END;
	
	RETURN;

	
EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER FUNCTION "soad"."fnc_cadastro_pessoa"("p_nome" "text", "p_documento" "text", "p_email" "text", "p_telefone" "text", "p_inscricao_estadual" "text", "p_fantasia" "text", "p_pessoa_id" "text", "p_endereco" "json", "p_modalidade" "json", OUT "pessoa_id" integer) OWNER TO "postgres";

--
-- TOC entry 291 (class 1255 OID 90953)
-- Name: fnc_chamada_de_metodo("json"); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_chamada_de_metodo"("p_json_params" "json" DEFAULT NULL::"json", OUT "p_retorno" integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE

	v_metodo		text 	:= p_json_params::json->'metodo';
	v_json_params	json	:= p_json_params::json->'params';
	v_json 			json	:= p_json_params;
	
	v_id_requisicao integer	:= NULL;
	v_params_temp	text	:= NULL;
	v_params		text	:= NULL;
	v_retorno		integer := NULL;
	v_mensagem 		text;
	v_tipo			text;

BEGIN
	
	-- TODO: Permitir que receba vários métodos em um mesmo json
	-- REGISTRA REQUISICAO
	BEGIN
		v_metodo := trim('"' FROM v_metodo::text);
		v_tipo := split_part(v_metodo, '_', 1);
		v_metodo := 'soad.' || v_metodo;
		
		WITH t_requisicao AS (
			INSERT INTO soad.requisicao (metodo, params_json)
			VALUES (v_metodo, v_json_params)
			RETURNING id_requisicao
		) 

		SELECT id_requisicao INTO v_id_requisicao
		FROM t_requisicao;

	EXCEPTION WHEN OTHERS THEN
		RAISE EXCEPTION 'Método/Parâmetros não podem ser nulos. % %', SQLERRM, SQLSTATE;
	END;
		
	BEGIN

		-- Fazer um for para pegar mais de um método do 

		-- JSON PARSE 
		BEGIN
			-- transforma os parametros em uma string
			v_params := '';
			FOR v_params_temp IN 
				SELECT concat('p_', key, '=>', E'\'', value, E'\'', ', ')
				FROM json_each_text(v_json_params) 
			LOOP
				v_params := v_params || v_params_temp;
			END LOOP;
			v_params := TRIM(trailing ', ' from v_params); -- remove ultima virgula
		EXCEPTION WHEN OTHERS THEN 
			RAISE EXCEPTION 'Erro ao fazer o parse dos parâmetros. % % %', v_json_params, SQLERRM, SQLSTATE;
		END;

		-- CHAMA METODO
		BEGIN
			DECLARE
				sql_query text := v_metodo || '(' || v_params || ');';
			BEGIN
				
				IF v_tipo = 'prc' THEN
					sql_query := 'CALL ' || sql_query;
					EXECUTE sql_query;
					v_retorno := 100;
					
				ELSIF v_tipo = 'fnc' THEN
					sql_query := 'SELECT * FROM ' || sql_query;
					EXECUTE sql_query INTO v_retorno;
					
				END IF;
				
			END;
		END;

		-- REGISTRA RETORNO 
		-- 0 	- falha 
		-- 100 	- sucesso
		UPDATE soad.requisicao
		SET retorno=v_retorno
		WHERE id_requisicao = v_id_requisicao;
		
-- 	EXCEPTION WHEN OTHERS THEN
-- 		v_retorno := 0;
-- 		v_mensagem := SQLERRM;
-- 		UPDATE soad.requisicao
-- 		SET retorno=v_retorno,
-- 			mensagem=SQLERRM
-- 		WHERE id_requisicao = v_id_requisicao;

	END;
	
--COMMIT;

	IF v_retorno = '0' THEN
		-- Montar em json
		RAISE EXCEPTION 
			'{"erro": "Não foi possível executar a operacao.","metodo": "%","retorno": "%","parametros": "%","requisicao_id": "%"}' 
			, v_metodo, v_mensagem, v_json_params, v_id_requisicao;
	ELSE
		p_retorno := v_retorno;
		IF v_tipo = 'prc' THEN
			RETURN;
		ELSIF v_tipo = 'fnc' THEN
			RETURN;
		END IF;
	END IF;
	
END;
$$;


ALTER FUNCTION "soad"."fnc_chamada_de_metodo"("p_json_params" "json", OUT "p_retorno" integer) OWNER TO "postgres";

--
-- TOC entry 296 (class 1255 OID 99123)
-- Name: fnc_get_pedido(integer); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_get_pedido"("p_pedido_id" integer, OUT "json_pedido" "json") RETURNS "json"
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pedido_id integer := p_pedido_id;
	v_pedido RECORD;
	v_item_pedido RECORD;
	v_remanufatura RECORD;
	
	v_json_pedido json;
	v_json_item_pedido json;
	v_json_remanufatura json;
	
	v_json json;
	v_array json array;
	
BEGIN
	-- Busca pedido
	SELECT id_pedido
		, data_entrega
		, tipo_pedido
		, data_cadastro
		, observacao
		, situacao
		, id_pessoa
		, pessoa
		, email
		, telefone
		, documento
		, fantasia
	INTO v_pedido
	FROM soad.vw_pedido
	WHERE id_pedido = v_pedido_id;

	v_json_pedido := row_to_json(v_pedido);
	
	-- pegar item_pedido
	v_array := NULL;
	FOR v_item_pedido IN 
		SELECT id_item_pedido
			, id_mercadoria
			, descricao
			, marca
			, quantidade
			, valor_unitario
			, id_unidade_medida
			, unidade_medida
			, 'MERCADORIA' as tipo
		FROM soad.vw_item_pedido
		WHERE id_pedido = v_pedido_id
	LOOP
		v_json := row_to_json(v_item_pedido);
		v_array := v_array || v_json;
	END LOOP;
	
	
	-- pegar remanufatura
	-- Vai agrupar as remanufaturas do pedido
	FOR v_remanufatura IN 
		SELECT id_pedido
			, id_remanufatura
			, valor_unitario
			, id_casco
			, casco
			, id_insumo
			, insumo
			, 'REMANUFATURA' as tipo
		FROM soad.vw_remanufatura
		WHERE id_pedido = v_pedido_id
		--GROUP BY id_pedido, id_mercadoria, id_insumo
	LOOP
		v_json := row_to_json(v_remanufatura);
		v_array := v_array || v_json;
	END LOOP;
	
	v_json_item_pedido := array_to_json(v_array);
	
	-- montar json
	v_array := NULL;
	v_array = v_array || v_json_pedido;
	v_array = v_array || v_json_item_pedido; 
	
	json_pedido = array_to_json(v_array);
	
	RETURN;

END;
$$;


ALTER FUNCTION "soad"."fnc_get_pedido"("p_pedido_id" integer, OUT "json_pedido" "json") OWNER TO "postgres";

--
-- TOC entry 3229 (class 0 OID 0)
-- Dependencies: 296
-- Name: FUNCTION "fnc_get_pedido"("p_pedido_id" integer, OUT "json_pedido" "json"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON FUNCTION "soad"."fnc_get_pedido"("p_pedido_id" integer, OUT "json_pedido" "json") IS 'retorna json com pedido e os itens';


--
-- TOC entry 290 (class 1255 OID 90940)
-- Name: fnc_get_pessoa(integer); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_get_pessoa"("p_pessoa_id" integer, OUT "json_pessoa" "json") RETURNS "json"
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_pessoa_id integer = p_pessoa_id;
	
	v_pessoa RECORD;
	v_json_pessoa json;
	
	v_modalidade_pessoa RECORD;
	v_json_modalidade json;
	
	v_endereco RECORD;
	v_json_endereco json;
	
	v_array json ARRAY;
	
BEGIN
	-- pegar pessoa
	SELECT id_pessoa
		, nome
		, email
		, telefone
		, documento
		, inscricao_estadual
		, fantasia
	INTO v_pessoa
	FROM soad.vw_pessoa
	WHERE id_pessoa = v_pessoa_id;

	v_json_pessoa := row_to_json(v_pessoa);
	
	-- pegar endereço
	
	v_array := NULL;
	FOR v_endereco IN 
		SELECT id_endereco
			, id_pessoa
			, logradouro
			, numero
			, bairro
			, cep
			, complemento
			, tipo
			, id_municipio
			, municipio
			, id_estado
			, estado
			, sigla_uf
			, id_pais
			, pais
		FROM soad.vw_endereco
		WHERE id_pessoa = v_pessoa_id 
	LOOP
		v_json_endereco := row_to_json(v_endereco);
		v_array := v_array || v_json_endereco;
	END LOOP;
	
	v_json_endereco = array_to_json(v_array);
	
	-- pegar modalidade
	
	v_array := NULL;
	FOR v_modalidade_pessoa IN 
		SELECT modalidade.id_modalidade
			, modalidade.descricao
		FROM soad.modalidade_pessoa
		INNER JOIN soad.modalidade ON modalidade.id_modalidade = modalidade_pessoa.fk_modalidade_id
		WHERE fk_pessoa_id = v_pessoa_id 
	LOOP
		v_json_modalidade := row_to_json(v_modalidade_pessoa);
		v_array := v_array || v_json_modalidade;
	END LOOP;
	
	v_json_modalidade = array_to_json(v_array);
	
	-- montar json
	v_array := NULL;
	v_array = v_array || v_json_pessoa;
	v_array = v_array || v_json_endereco; 
	v_array = v_array || v_json_modalidade;
	
	json_pessoa = array_to_json(v_array);
	
	RETURN;
	
END;
$$;


ALTER FUNCTION "soad"."fnc_get_pessoa"("p_pessoa_id" integer, OUT "json_pessoa" "json") OWNER TO "postgres";

--
-- TOC entry 3230 (class 0 OID 0)
-- Dependencies: 290
-- Name: FUNCTION "fnc_get_pessoa"("p_pessoa_id" integer, OUT "json_pessoa" "json"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON FUNCTION "soad"."fnc_get_pessoa"("p_pessoa_id" integer, OUT "json_pessoa" "json") IS 'traz informações da pessoa, endereços e modalidades';


--
-- TOC entry 288 (class 1255 OID 66362)
-- Name: fnc_insert_mercadoria("text", "text", integer, "text", boolean, "text"[]); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_insert_mercadoria"("p_descricao" "text", "p_marca" "text", "p_unidade_medida_id" integer, "p_tipo" "text" DEFAULT 'PRODUTO'::"text", "p_permite_venda" boolean DEFAULT NULL::boolean, VARIADIC "args" "text"[] DEFAULT NULL::"text"[], OUT "p_id_mercadoria" integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_id_mercadoria integer;
	-- mercadoria
	v_descricao text 					:= upper(p_descricao);
	v_marca text 						:= upper(p_marca);
	v_unidade_medida_id integer 		:= p_unidade_medida_id;
	v_tipo text 						:= upper(p_tipo);
	v_permite_venda boolean				:= p_permite_venda;
	
	-- casco
	v_casco_insumo_id integer			:= NULL;
	v_casco_quantidade_insumo real		:= NULL;
	
	-- insumo
	v_insumo_quantidade_embalagem real	:= NULL;
	v_insumo_unidade_medida_id integer	:= NULL;
	
BEGIN

	IF v_permite_venda IS NULL THEN
		IF 	  v_tipo = 'MERCADORIA'	THEN v_permite_venda := True;
		ELSIF v_tipo 'CASCO' 		THEN v_permite_venda := False;
		ELSIF v_tipo 'INSUMO' 		THEN v_permite_venda := False;
		END IF;
	END IF;
		
	-- Inserir produto/mercadoria
	
	WITH t_mercadoria AS (
		INSERT INTO soad.mercadoria (descricao, marca, fk_unidade_medida_id, permite_venda)
		VALUES (v_descricao, v_marca, v_unidade_medida_id, v_permite_venda)
		RETURNING id_mercadoria
	) 

	SELECT id_mercadoria 
	INTO v_id_mercadoria
	FROM t_mercadoria;

	p_id_mercadoria := v_id_mercadoria;
		
	
	-- Inserir insumo
	IF v_tipo = 'INSUMO' THEN
    
        IF args[3] IS null THEN 
			args[3] = '0'; 
		END IF;
        
		IF 
			args[1] IS NOT null 
			AND args[2] IS NOT null
		THEN
			v_insumo_quantidade_embalagem	:= args[1];
			v_insumo_unidade_medida_id 		:= args[2];
		ELSE
			RAISE EXCEPTION 'Parametros não podem ser nulos % %', args[1], args[2];
		END IF;
			
		INSERT INTO soad.insumo (fk_mercadoria_id, quantidade_embalagem, fk_unidade_medida_id)
		VALUES (v_id_mercadoria, v_insumo_quantidade_embalagem, v_insumo_unidade_medida_id);
			
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
	
		INSERT INTO soad.casco (fk_mercadoria_id, fk_insumo_id, quantidade_insumo)
		VALUES (v_id_mercadoria, v_casco_insumo_id, v_casco_quantidade_insumo);
	
		RETURN;
			
	ELSIF v_tipo = 'MERCADORIA' THEN
		
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


ALTER FUNCTION "soad"."fnc_insert_mercadoria"("p_descricao" "text", "p_marca" "text", "p_unidade_medida_id" integer, "p_tipo" "text", "p_permite_venda" boolean, VARIADIC "args" "text"[], OUT "p_id_mercadoria" integer) OWNER TO "postgres";

--
-- TOC entry 297 (class 1255 OID 99135)
-- Name: fnc_insert_pedido("text", integer, "text", "date", integer); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_insert_pedido"("p_tipo_pedido" "text", "p_pessoa_id" integer, "p_observacao" "text", "p_data_entrega" "date", "p_pedido_id" integer DEFAULT NULL::integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	-- Pedido
	v_id_pedido		integer	:= p_pedido_id; -- Vai receber o id do pedido gravado
	
	v_tipo_pedido 	text	:= upper(p_tipo_pedido);
    v_pessoa_id 	integer	:= p_pessoa_id;
	v_observacao 	text	:= p_observacao;
	v_data_entrega 	date	:= p_data_entrega;
	
	v_data_cadastro date 	:= statement_timestamp();
	v_situacao 		text	:= 'CADASTRADO';
	
			  
BEGIN

	IF v_pessoa_id is NULL THEN
		RAISE EXCEPTION 'Não é possível inserir um pedido sem destinatário';
	END IF;
	
	-- Cadastra pedido	
	IF v_id_pedido IS NULL THEN
		BEGIN
			WITH t_pedido as (
				INSERT INTO soad.pedido (fk_pessoa_id, tipo_pedido, situacao, data_cadastro, observacao)
				VALUES (v_pessoa_id, v_tipo_pedido ,'CADASTRADO', v_data_cadastro, v_observacao)
				RETURNING id_pedido
			)
				SELECT id_pedido INTO v_id_pedido
				FROM t_pedido;

			RETURN v_id_pedido;
		END;
	
	-- Edita pedido
	ELSE
		BEGIN
			WITH t_pedido as (
				UPDATE soad.pedido 
				SET fk_pessoa_id=v_pessoa_id
					, observacao=v_observacao
				RETURNING id_pedido
			)
				SELECT id_pedido INTO v_id_pedido
				FROM t_pedido;

			RETURN v_id_pedido;
		END;
	END IF;
	
EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER FUNCTION "soad"."fnc_insert_pedido"("p_tipo_pedido" "text", "p_pessoa_id" integer, "p_observacao" "text", "p_data_entrega" "date", "p_pedido_id" integer) OWNER TO "postgres";

--
-- TOC entry 293 (class 1255 OID 90979)
-- Name: fnc_insert_update_endereco(integer, integer, "text", "text", "text", "text", "text", "text", integer); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_insert_update_endereco"("p_pessoa_id" integer, "p_municipio_id" integer, "p_logradouro" "text", "p_numero" "text", "p_bairro" "text", "p_cep" "text", "p_complemento" "text", "p_tipo" "text", "p_endereco_id" integer DEFAULT NULL::integer, OUT "endereco_id" integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pessoa_id 	integer 	:= p_pessoa_id;
	v_municipio_id 	integer 	:= p_municipio_id;
	v_logradouro 	text 		:= p_logradouro;
	v_numero 		text 		:= p_numero;
	v_bairro 		text 		:= p_bairro;
	v_cep 			text 		:= p_cep;
	v_complemento 	text    	:= p_complemento;
	v_endereco_id 	integer 	:= p_endereco_id;
	v_tipo			text        := p_tipo;

BEGIN
	
	IF v_endereco_id IS NULL THEN
	
		WITH t_endereco AS (

			INSERT INTO soad.endereco (
				fk_municipio_id
				, fk_pessoa_id
				, logradouro
				, numero
				, bairro
				, cep
				, complemento
				, tipo
			)

			VALUES (
				v_municipio_id
				, v_pessoa_id
				, v_logradouro
				, v_numero
				, v_bairro
				, v_cep
				, v_complemento
				, v_tipo
			)

			RETURNING id_endereco

		) 
		
		SELECT id_endereco INTO endereco_id 
		FROM t_endereco;
		
	ELSE
	
		UPDATE soad.endereco
		SET fk_municipio_id=v_municipio_id
			, fk_pessoa_id=v_pessoa_id
			, logradouro=v_logradouro
			, numero=v_numero
			, bairro=v_bairro
			, cep=v_cep
			, complemento=v_complemento
			, tipo=v_tipo
		WHERE id_endereco = v_endereco_id::integer;
		
		endereco_id := v_endereco_id::integer;
	
	END IF;

	RETURN;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER FUNCTION "soad"."fnc_insert_update_endereco"("p_pessoa_id" integer, "p_municipio_id" integer, "p_logradouro" "text", "p_numero" "text", "p_bairro" "text", "p_cep" "text", "p_complemento" "text", "p_tipo" "text", "p_endereco_id" integer, OUT "endereco_id" integer) OWNER TO "postgres";

--
-- TOC entry 294 (class 1255 OID 90982)
-- Name: fnc_insert_update_endereco(integer, integer, "text", "text", "text", "text", "text", "text", "text"); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_insert_update_endereco"("p_pessoa_id" integer, "p_municipio_id" integer, "p_logradouro" "text", "p_numero" "text", "p_bairro" "text", "p_cep" "text", "p_complemento" "text", "p_tipo" "text", "p_endereco_id" "text" DEFAULT NULL::"text", OUT "endereco_id" integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pessoa_id 	integer 	:= p_pessoa_id;
	v_municipio_id 	integer 	:= p_municipio_id;
	v_logradouro 	text 		:= p_logradouro;
	v_numero 		text 		:= p_numero;
	v_bairro 		text 		:= p_bairro;
	v_cep 			text 		:= p_cep;
	v_complemento 	text    	:= p_complemento;
	v_endereco_id 	text 	:= p_endereco_id;
	v_tipo			text        := p_tipo;

BEGIN
	
	IF v_endereco_id IS NULL THEN
	
		WITH t_endereco AS (

			INSERT INTO soad.endereco (
				fk_municipio_id
				, fk_pessoa_id
				, logradouro
				, numero
				, bairro
				, cep
				, complemento
				, tipo
			)

			VALUES (
				v_municipio_id
				, v_pessoa_id
				, v_logradouro
				, v_numero
				, v_bairro
				, v_cep
				, v_complemento
				, v_tipo
			)

			RETURNING id_endereco

		) 
		
		SELECT id_endereco INTO endereco_id 
		FROM t_endereco;
		
	ELSE
	
		UPDATE soad.endereco
		SET fk_municipio_id=v_municipio_id
			, fk_pessoa_id=v_pessoa_id
			, logradouro=v_logradouro
			, numero=v_numero
			, bairro=v_bairro
			, cep=v_cep
			, complemento=v_complemento
			, tipo=v_tipo
		WHERE id_endereco = v_endereco_id::integer;
		
		endereco_id := v_endereco_id::integer;
	
	END IF;

	RETURN;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER FUNCTION "soad"."fnc_insert_update_endereco"("p_pessoa_id" integer, "p_municipio_id" integer, "p_logradouro" "text", "p_numero" "text", "p_bairro" "text", "p_cep" "text", "p_complemento" "text", "p_tipo" "text", "p_endereco_id" "text", OUT "endereco_id" integer) OWNER TO "postgres";

--
-- TOC entry 292 (class 1255 OID 90969)
-- Name: fnc_insert_update_pessoa("text", "text", "text", "text", "text", "text", "text"); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_insert_update_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text" DEFAULT 'ISENTO'::"text", "p_fantasia" "text" DEFAULT NULL::"text", "p_pessoa_id" "text" DEFAULT NULL::"text", OUT "pessoa_id" integer) RETURNS integer
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_nome 					text 	:= p_nome;
	v_email 				text 	:= p_email;
	v_telefone 				text 	:= p_telefone;
	v_documento 			text 	:= p_documento;
	v_inscricao_estadual 	text 	:= p_inscricao_estadual;
	v_fantasia 				text 	:= p_fantasia;
	v_id_pessoa 			integer := p_pessoa_id;
	v_acao text;

BEGIN

	IF v_inscricao_estadual = '' THEN
		v_inscricao_estadual = 'ISENTO';
	END IF;
	
	BEGIN
		IF v_id_pessoa IS NULL THEN
			
			v_acao := 'INSERT';
		
			WITH t_pessoa AS (
				INSERT INTO soad.pessoa (
					nome
					, email
					, telefone
					, inscricao_estadual
				)
					VALUES (v_nome, v_email, v_telefone, v_inscricao_estadual)
					RETURNING id_pessoa
			)

			SELECT id_pessoa INTO v_id_pessoa
			FROM t_pessoa;
			
		ELSIF v_id_pessoa IS NOT NULL THEN
			
			v_acao := 'UPDATE';
			
			UPDATE soad.pessoa
			SET nome=v_nome
				, email=v_email
				, telefone=v_telefone
				, inscricao_estadual=v_inscricao_estadual
			WHERE pessoa.id_pessoa = v_id_pessoa;
			
		END IF;
		RAISE NOTICE '%', v_acao;
		IF length(v_documento) = 14 THEN -- insere pessoa e pessoa juridica
			
			IF v_acao = 'INSERT' THEN
			
				INSERT INTO soad.pessoa_juridica (fk_pessoa_id, cnpj, fantasia)
				VALUES (v_id_pessoa, v_documento, v_fantasia);
			
			ELSIF v_acao = 'UPDATE' THEN
			
				IF (SELECT cnpj FROM soad.pessoa_juridica WHERE fk_pessoa_id = v_id_pessoa) <> v_documento THEN
					UPDATE soad.pessoa_juridica
					SET cnpj=v_documento
					WHERE pessoa_juridica.fk_pessoa_id = v_id_pessoa;
				END IF;
			
				UPDATE soad.pessoa_juridica
				SET cnpj=v_documento
					, fantasia=v_fantasia
				WHERE pessoa_juridica.fk_pessoa_id = v_id_pessoa;
				
			END IF;

		ELSIF length(v_documento) = 11 THEN 	-- insere pessoa e pessoa fisica
		
			IF v_acao = 'INSERT' THEN

				INSERT INTO soad.pessoa_fisica (fk_pessoa_id, cpf) 
				VALUES (v_id_pessoa, v_documento);

			ELSIF v_acao = 'UPDATE' THEN
				
				IF (SELECT cpf FROM soad.pessoa_fisica WHERE fk_pessoa_id = v_id_pessoa) <> v_documento THEN
					UPDATE soad.pessoa_fisica
					SET cpf=v_documento
					WHERE pessoa_fisica.fk_pessoa_id = v_id_pessoa;
				END IF;
				
				-- atualiza outros dados aqui
				--UPDATE soad.pessoa_fisica
				--SET x=y
				--WHERE pessoa_fisica.fk_pessoa_id = v_id_pessoa;
			
			END IF;
		
		ELSE
			RAISE EXCEPTION 'Documento % inválido.', v_documento;

		END IF;
		
		pessoa_id := v_id_pessoa;
		RETURN;
	
	EXCEPTION WHEN OTHERS THEN
		RAISE EXCEPTION 'Não foi possível cadastrar a pessoa. % %', SQLERRM, SQLSTATE;		
	
	END;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
END;
$$;


ALTER FUNCTION "soad"."fnc_insert_update_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text", "p_fantasia" "text", "p_pessoa_id" "text", OUT "pessoa_id" integer) OWNER TO "postgres";

--
-- TOC entry 274 (class 1255 OID 49998)
-- Name: fnc_relatorio_municipios(character varying, character varying, character varying); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."fnc_relatorio_municipios"("p_pais" character varying, "p_estado" character varying, "p_municipio" character varying) RETURNS TABLE("municipio_id" integer, "municipio" character varying, "estado_id" integer, "estado" character varying, "pais_id" integer, "pais" character varying)
    LANGUAGE "plpgsql"
    AS $$begin
	return query select t_municipio.id_municipio, t_municipio.municipio, t_municipio.id_estado, t_municipio.estado, t_municipio.id_pais, t_municipio.pais
					from soad.vw_municipio as t_municipio
						where 1=1
						and t_municipio.municipio like p_municipio
						and t_municipio.estado like p_estado
						and t_municipio.pais   like p_pais;
end;
$$;


ALTER FUNCTION "soad"."fnc_relatorio_municipios"("p_pais" character varying, "p_estado" character varying, "p_municipio" character varying) OWNER TO "postgres";

--
-- TOC entry 300 (class 1255 OID 99183)
-- Name: prc_cancelar_pedido(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_cancelar_pedido"("p_pedido_id" integer)
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pedido_id integer := p_pedido_id;
	v_situacao_pedido text;
BEGIN
	
	SELECT pedido.situacao INTO v_situacao_pedido 
	FROM soad.pedido WHERE id_pedido = v_pedido_id;
	
	IF v_situacao_pedido = 'ENCERRADO' THEN
		RAISE EXCEPTION 'Não é possível cancelar um pedido encerrado. Realize o estorno desse pedido.';
	ELSIF v_situacao_pedido = 'CANCELADO' THEN
		RAISE EXCEPTION 'Esse pedido já está cancelado.';
	ELSIF v_situacao_pedido = 'CADASTRADO' OR v_situacao_pedido = 'ESTORNADO' THEN
		UPDATE soad.pedido
		SET situacao='CANCELADO'
		WHERE pedido.id_pedido = v_pedido_id;
		
		RAISE NOTICE 'Pedido % cancelado', v_pedido_id;
		
	ELSE
		RAISE EXCEPTION 'Situação do pedido % não identificada, não é possível cancelar.', v_situacao_pedido;
	END IF;
EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION 'Não foi possível cancelar o pedido. % %', SQLERRM, SQLSTATE; 

END;
$$;


ALTER PROCEDURE "soad"."prc_cancelar_pedido"("p_pedido_id" integer) OWNER TO "postgres";

--
-- TOC entry 3231 (class 0 OID 0)
-- Dependencies: 300
-- Name: PROCEDURE "prc_cancelar_pedido"("p_pedido_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_cancelar_pedido"("p_pedido_id" integer) IS 'cancelamento de pedido, só pode cancelar se não tiver encerrado';


--
-- TOC entry 279 (class 1255 OID 17545)
-- Name: prc_configuracao_definicoes_iniciais(); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_configuracao_definicoes_iniciais"()
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
		CALL soad.prc_insert_municipio_estado_pais('', '', '', 'Brasil', 'BR');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro dos paises.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;
	
	-- Cadastra estados
	RAISE NOTICE 'Cadastrando estados...';
	BEGIN
		CALL soad.prc_insert_municipio_estado_pais('', 'Acre', 'AC', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Alagoas', 'AL', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Amapá', 'AP', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Amazonas', 'AM', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Bahia', 'BA', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Ceará', 'CE', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('Brasília', 'Distrito Federal', 'DF', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Espírito Santo', 'ES', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Goiás', 'GO', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Maranhão', 'MA', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Mato Grosso', 'MT', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Mato Grosso do Sul', 'MS', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Minas Gerais', 'MG', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Pará', 'PA', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Paraíba', 'PB', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Paraná', 'PR', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Pernambuco', 'PE', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Piauí', 'PI', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('Rio de Janeiro', 'Rio de Janeiro', 'RJ', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Rio Grande do Norte', 'RN', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Rio Grande do Sul', 'RS', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Rondônia', 'RO', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Roraima', 'RR', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Santa Catarina', 'SC', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('São Paulo', 'São Paulo', 'SP', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Sergipe', 'SE', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('', 'Tocantins', 'TO', 'Brasil', 'BR');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro dos estados.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;

	-- Cadastra municipios
	RAISE NOTICE 'Cadastrando municipios...';
	BEGIN
		CALL soad.prc_insert_municipio_estado_pais('Ponta Grossa', 'Paraná', 'PR', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('Curitiba', 'Paraná', 'PR', 'Brasil', 'BR');
		CALL soad.prc_insert_municipio_estado_pais('Castro', 'Paraná', 'PR', 'Brasil', 'BR');
		
	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das municipios.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;
		
	END;
	
	-- Cadastra pessoa
	RAISE NOTICE 'Cadastrando pessoas...';
	BEGIN
		CALL soad.prc_insert_pessoa('VIP Cartuchos', '', '4232240660', '00000000000000', '', 'VIP Cartuchos');
		CALL soad.prc_insert_pessoa('EMPRESA TESTE 1', '', '4232240660', '99998899999999', '', 'EMPRESA TESTE 1');
		CALL soad.prc_insert_pessoa('Lucas Klüber', 'lucas.kluber@gmail.com', '42999823030', '10841793930', '', '');
		CALL soad.prc_insert_pessoa('PESSOA TESTE 1', '', '', '00000100000', '', '');
		
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
			v_municipio_id integer := NULL;
			
		BEGIN
			SELECT vw_pessoa.id_pessoa INTO v_pessoa_id FROM soad.vw_pessoa
			WHERE vw_pessoa.documento = '10841793930';
			
			SELECT vw_municipio.id_municipio INTO v_municipio_id FROM soad.vw_municipio
			WHERE vw_municipio.municipio = upper('PONTA GROSSA');
			
			CALL soad.prc_insert_endereco(v_pessoa_id, v_municipio_id, 'Rua Comandante Paulo Pinheiro Schimdt', '354', 'Uvaranas', '84031029', '');
			
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


ALTER PROCEDURE "soad"."prc_configuracao_definicoes_iniciais"() OWNER TO "postgres";

--
-- TOC entry 3232 (class 0 OID 0)
-- Dependencies: 279
-- Name: PROCEDURE "prc_configuracao_definicoes_iniciais"(); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_configuracao_definicoes_iniciais"() IS 'Algumas configurações iniciais para o uso do sistema';


--
-- TOC entry 280 (class 1255 OID 58272)
-- Name: prc_configuracao_gerador_trigger(); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_configuracao_gerador_trigger"()
    LANGUAGE "plpgsql"
    AS $$
BEGIN
SELECT
    'CREATE TRIGGER '
    || 'trg_auditoria'
    || ' AFTER INSERT OR UPDATE OR DELETE ON ' || tab_name || ' FOR EACH ROW EXECUTE PROCEDURE soad.trg_auditoria();' AS trigger_creation_query
FROM (
    SELECT
        quote_ident(table_schema) || '.' || quote_ident(table_name) as tab_name
    FROM
        information_schema.tables
    WHERE
        table_schema NOT IN ('pg_catalog', 'information_schema')
        AND table_schema NOT LIKE 'pg_toast%'
		AND table_name NOT LIKE 'vw_%'
) tablist;

END;
$$;


ALTER PROCEDURE "soad"."prc_configuracao_gerador_trigger"() OWNER TO "postgres";

--
-- TOC entry 295 (class 1255 OID 90989)
-- Name: prc_delete_pessoa(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_delete_pessoa"("p_pessoa_id" integer)
    LANGUAGE "plpgsql"
    AS $$
BEGIN

-- delete modalidade_pessoa
 	DELETE FROM soad.modalidade_pessoa
	WHERE fk_pessoa_id = p_pessoa_id;
	
-- delete endereco
	DELETE FROM soad.endereco
	WHERE fk_pessoa_id = p_pessoa_id;
	
-- delete pessoa fisica ou juridica
	DELETE FROM soad.pessoa_fisica
	WHERE fk_pessoa_id = p_pessoa_id;
	
	DELETE FROM soad.pessoa_juridica
	WHERE fk_pessoa_id = p_pessoa_id;
	
-- delete pessoa
	DELETE FROM soad.pessoa
	WHERE id_pessoa = p_pessoa_id;

END;
$$;


ALTER PROCEDURE "soad"."prc_delete_pessoa"("p_pessoa_id" integer) OWNER TO "postgres";

--
-- TOC entry 3233 (class 0 OID 0)
-- Dependencies: 295
-- Name: PROCEDURE "prc_delete_pessoa"("p_pessoa_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_delete_pessoa"("p_pessoa_id" integer) IS 'apaga a pessoa e seus vinculos';


--
-- TOC entry 299 (class 1255 OID 99175)
-- Name: prc_desvincular_remanufaturas_pedido(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_desvincular_remanufaturas_pedido"("p_pedido_id" integer)
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pedido_id		 	integer		:= p_pedido_id;
	v_id_remanufatura 	integer;
	v_pedido			RECORD;
	t_item				RECORD;

BEGIN

	SELECT situacao, tipo_pedido INTO v_pedido
	FROM soad.vw_pedido 
	WHERE id_pedido = v_pedido_id;
	
	IF v_pedido.situacao = 'ENCERRADO' THEN
		RAISE EXCEPTION 'Para manipular uma remanufatura vinculada, o pedido precisa estar na situacao CADASTRADO ou ESTORNADO';
	ELSIF v_pedido.tipo_pedido = 'COMPRA' THEN
		RAISE EXCEPTION 'Não é possível manipular uma remanufatura em um pedido do tipo COMPRA';
	END IF;
	
	-- Se tiver remanufatura REALIZADA vinculada, desvincula o pedido da remanufatura, 
	-- Se tiver só cadastrada EXCLUI
	<<REMANUFATURA>>
	FOR t_item IN 
		SELECT id_remanufatura, situacao FROM soad.remanufatura
		WHERE remanufatura.fk_pedido_id = v_pedido_id

	LOOP
		IF t_item.situacao = 'CADASTRADA' THEN
			DELETE FROM soad.remanufatura
			WHERE id_remanufatura = t_item.id_remanufatura;

		ELSIF t_item.situacao = 'REALIZADA' THEN
		
			UPDATE soad.remanufatura
			SET fk_pedido_id = NULL
				, valor_unitario = 0
			WHERE id_remanufatura = t_item.id_remanufatura;

		ELSIF t_item.situacao = 'ENCERRADA' THEN
			RAISE EXCEPTION 'Não é possível desvincular uma remanufatura ENCERRADA.';

		ELSE 
			RAISE EXCEPTION 'ALERTA: Remanufatura vinculada SITUACAO: %', t_item.situacao;

		END IF;
	END LOOP REMANUFATURA;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER PROCEDURE "soad"."prc_desvincular_remanufaturas_pedido"("p_pedido_id" integer) OWNER TO "postgres";

--
-- TOC entry 275 (class 1255 OID 99142)
-- Name: prc_encerrar_pedido(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_encerrar_pedido"("p_pedido_id" integer)
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_pedido_id   integer := p_pedido_id;
	v_situacao	  text;
	v_tipo_pedido text;

BEGIN
	
	-- verifica se pedido existe
	IF (SELECT id_pedido FROM soad.pedido WHERE id_pedido = v_pedido_id) IS NULL THEN
		RAISE EXCEPTION 'Pedido % não encontrado', v_pedido_id;
	END IF;

	-- valida situação
	v_situacao := (SELECT pedido.situacao FROM soad.pedido WHERE id_pedido = v_pedido_id);

	-- tenho quase certeza que esse não é a melhor forma de fazer isso
	IF v_situacao <> 'CADASTRADO' THEN 
		IF v_situacao <> 'ESTORNADO'  THEN
			RAISE EXCEPTION 'Não é possível encerrar um pedido %. O pedido precisa estar CADASTRADO ou ESTORNADO', v_situacao;
		END IF;	
	END IF;

	-- Muda status
	UPDATE soad.pedido
	SET situacao='ENCERRADO'
	WHERE id_pedido = v_pedido_id; 

	-- Identifica qual o tipo de pedido para tratar
	SELECT pedido.tipo_pedido INTO v_tipo_pedido
	FROM soad.pedido WHERE id_pedido = v_pedido_id;

	-- Registra lote/modifica lote
	IF v_tipo_pedido = 'COMPRA' THEN
		-- cadastrar lote
		CALL soad.prc_gerar_lote(v_pedido_id);
	ELSIF v_tipo_pedido = 'VENDA' THEN
		-- Vincular lotes existentes a um pedido de venda 
		CALL soad.prc_movimentar_lote(v_pedido_id);
	ELSE
		RAISE EXCEPTION 'O lote desse pedido não pode ser alterado';
	END IF;

	-- todo: Registra Log
--EXCEPTION WHEN OTHERS THEN
	--RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER PROCEDURE "soad"."prc_encerrar_pedido"("p_pedido_id" integer) OWNER TO "postgres";

--
-- TOC entry 3234 (class 0 OID 0)
-- Dependencies: 275
-- Name: PROCEDURE "prc_encerrar_pedido"("p_pedido_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_encerrar_pedido"("p_pedido_id" integer) IS 'Procedimento para encerrar pedido. Pedidos encerrados não podem ser alterados.';


--
-- TOC entry 282 (class 1255 OID 58177)
-- Name: prc_estornar_pedido(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_estornar_pedido"("p_pedido_id" integer)
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pedido_id		integer := p_pedido_id;
	v_tipo_pedido 	text;
	v_pedido		RECORD;
	t_item			RECORD;
	
BEGIN
	SELECT tipo_pedido, situacao
	INTO v_pedido 
	FROM soad.pedido 
	WHERE id_pedido = v_pedido_id;
	
	-- estornar pedido
	IF v_pedido.situacao <> 'ENCERRADO' THEN
		RAISE EXCEPTION 'Não é possível estornar um pedido na situacao %. O pedido deve estar ENCERRADO.', v_pedido.situacao;
	END IF;
	
	BEGIN 
		-- Muda status para 'ESTORNADO'
		UPDATE soad.pedido
		SET situacao='ESTORNADO'
			, observacao = observacao || '\nPedido estornado'
		WHERE id_pedido = v_pedido_id;
			
	END;
	
	BEGIN

		IF v_pedido.tipo_pedido = 'COMPRA' THEN
				<<VINCULOS_PEDIDO>>
				FOR t_item IN 
					-- Localiza os vinculos com pedidos de venda e remanufaturas dos lotes gerados pelo pedido
					SELECT 
						vw_item_lote.id_pedido_saida as pedido_saida_id
						, vw_item_lote.id_pedido_entrada as pedido_entrada_id
						, vw_item_lote.id_item_lote as item_lote_id
						, vw_item_lote.id_lote as lote_id
						, item_rem.id_item_lote_remanufatura
						, item_rem.fk_remanufatura_id as remanufatura_id
						, vw_item_lote.aberto
						, vw_item_lote.quantidade_item as quantidade
					FROM soad.vw_item_lote
						LEFT JOIN soad.item_lote_remanufatura item_rem 
							ON vw_item_lote.id_item_lote = item_rem.fk_item_lote_id
						WHERE vw_item_lote.id_pedido_entrada = v_pedido_id
				LOOP
						-- Tratamento caso não seja possível estornar
						-- Verifica se não tem venda OU remanufatura_item_lote vinculadas e não está aberto
						IF t_item.id_item_lote_remanufatura IS NOT NULL THEN
							RAISE EXCEPTION 
								'O item ID % do lote ID % desse pedido foi utilizado na remanufatura ID %. Não é possível realizar o estorno.'
								, t_item.item_lote_id, t_item.lote_id, t_item.remanufatura_id;
						ELSIF t_item.quantidade = 0 THEN
							RAISE EXCEPTION
								'O item ID % não está mais disponível no estoque (Pedido de Venda ID %). Não é possível realizar o estorno.'
								, t_item.item_lote_id, t_item.pedido_saida_id;
						ELSIF t_item.aberto = True THEN
							RAISE EXCEPTION
								'O item ID % já foi aberto. Não é possível realizar o estorno.'
								, t_item.item_lote_id;
						END IF;
						
				END LOOP VINCULOS_PEDIDO;
				
				t_item := NULL; -- reinicia a variável
				
				-- Se chegar até aqui então irá procurar todos os lotes e item_lotes gerados e excluir
				BEGIN
					
					<<REMOVER_LOTES>>
					FOR t_item IN
						-- localiza os lotes e itens lote viculados ao pedido
						SELECT id_lote, id_item_lote, id_pedido_entrada
						FROM soad.vw_item_lote
						WHERE id_pedido_entrada = v_pedido_id
					LOOP
						
						DELETE FROM soad.item_lote 
						WHERE item_lote.id_item_lote = t_item.id_item_lote;
						
						RAISE NOTICE 'Removido item_lote ID %.', t_item.id_item_lote;
					
					END LOOP REMOVER_LOTES;
					
					DELETE FROM soad.lote 
					WHERE lote.fk_pedido_id = v_pedido_id;
					
					RAISE NOTICE 'Lotes vinculados ao pedido removidos.';
					
					-- Sanity check, verifica se não ficou nenhum lote vinculado ao pedido antes de finalizar.
					IF (SELECT COUNT(*) FROM soad.lote WHERE lote.fk_pedido_id = v_pedido_id) <> 0 THEN
						RAISE EXCEPTION 'Não foi possível realizar o estorno do pedido. Lote(s) ainda vinculado(s).';
					END IF;					

				END;
		
		ELSIF v_pedido.tipo_pedido = 'VENDA' THEN
			-- Tenta desvincular as remanufaturas do pedido
			CALL soad.prc_desvincular_remanufaturas_pedido(p_pedido_id=>v_pedido_id);
			
			-- localiza os item_lote vinculados ao pedido de venda, desvincula e muda a quantidade para 1
			
			-- aberto=false
			-- quantidade=0
			-- fk_pedido_origem = v_pedido_id
			
			t_item := NULL;
			FOR t_item IN
				SELECT vw_item_lote.id_item_lote
					, vw_item_lote.id_lote
					, vw_item_lote.quantidade_item
					, vw_item_lote.aberto 
				FROM soad.vw_item_lote
				WHERE vw_item_lote.id_pedido_saida = v_pedido_id
				
			LOOP
				-- validacoes
				IF t_item.aberto THEN
					RAISE EXCEPTION 'Existem items abertos no lote, não foi possível estornar o pedido.';
				ELSIF t_item.quantidade_item <> 0 THEN
					RAISE EXCEPTION 'O item do lote vínculado a venda não está vazio. Não foi possível estornar o pedido.';
				END IF;
				
				-- desfaz vinculos com pedido
				UPDATE soad.item_lote
				SET fk_item_pedido_saida_id = NULL
					, data_retirada = NULL
					, motivo_retirada = NULL
					, quantidade_item = 1
				WHERE id_item_lote = t_item.id_item_lote;
				
				-- Muda lote para vazio=false
				BEGIN
					CALL soad.prc_esvazia_lote(t_item.id_lote);
				END;
				
			END LOOP;
			
		ELSE
			RAISE EXCEPTION 'Esse tipo de pedido não pode ser estornado.';
		END IF;
	END;
	
	RAISE NOTICE 'Pedido estornado com sucesso.';
	-- todo: Registra log

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_estornar_pedido"("p_pedido_id" integer) OWNER TO "postgres";

--
-- TOC entry 3235 (class 0 OID 0)
-- Dependencies: 282
-- Name: PROCEDURE "prc_estornar_pedido"("p_pedido_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_estornar_pedido"("p_pedido_id" integer) IS 'Estorna o encerramento do pedido, desfazendo as movimentações';


--
-- TOC entry 278 (class 1255 OID 58171)
-- Name: prc_esvazia_lote(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_esvazia_lote"("p_lote_id" integer)
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_lote_id integer = p_lote_id;
	v_quantidade real;
	
BEGIN
	
	IF (SELECT COUNT(*) FROM soad.item_lote) = 0 THEN
		RAISE EXCEPTION 'Lote % não encontrado', v_lote_id;
	END IF;
	
	SELECT SUM(quantidade_item) INTO v_quantidade
	FROM soad.item_lote
	WHERE item_lote.fk_lote_id = v_lote_id;

	IF v_quantidade = 0 THEN
		UPDATE soad.lote
		SET vazio=True
		WHERE lote.id_lote = v_lote_id;
		RAISE NOTICE 'Lote % esvaziado.', v_lote_id;
	ELSE
		UPDATE soad.lote
		SET vazio=False
		WHERE lote.id_lote = v_lote_id;
		RAISE NOTICE 'Lote % não está vazio', v_lote_id;
	END IF;
END;$$;


ALTER PROCEDURE "soad"."prc_esvazia_lote"("p_lote_id" integer) OWNER TO "postgres";

--
-- TOC entry 3236 (class 0 OID 0)
-- Dependencies: 278
-- Name: PROCEDURE "prc_esvazia_lote"("p_lote_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_esvazia_lote"("p_lote_id" integer) IS 'verifica se lote pode ser esvaziado';


--
-- TOC entry 272 (class 1255 OID 50276)
-- Name: prc_esvaziar_item_lote(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_esvaziar_item_lote"("p_item_lote_id" integer)
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_item_lote_id integer := p_item_lote_id;
	v_item_lote RECORD;
	
BEGIN

	SELECT aberto, quantidade_item INTO v_item_lote 
	FROM soad.item_lote
	WHERE id_item_lote = v_item_lote_id;

	IF v_item_lote.quantidade_item = 0 THEN
		RAISE EXCEPTION 'Esse item já está vazio.';
	END IF;
	
	IF v_item_lote.aberto = False THEN
		RAISE EXCEPTION 'Não é possível esvaziar um item fechado.';
	END IF;

	UPDATE soad.item_lote
	SET motivo_retirada = motivo_retirada || '\nItem utilizado (Vazio)'
		, quantidade_item=0
		, data_retirada=now()
	WHERE item_lote.id_item_lote = v_item_lote_id;

END;
$$;


ALTER PROCEDURE "soad"."prc_esvaziar_item_lote"("p_item_lote_id" integer) OWNER TO "postgres";

--
-- TOC entry 3237 (class 0 OID 0)
-- Dependencies: 272
-- Name: PROCEDURE "prc_esvaziar_item_lote"("p_item_lote_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_esvaziar_item_lote"("p_item_lote_id" integer) IS 'marca item_lote como vazio';


--
-- TOC entry 271 (class 1255 OID 49979)
-- Name: prc_gerar_lote(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_gerar_lote"("p_id_pedido" integer)
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_id_pedido integer := p_id_pedido;
	v_id_lote integer;
	v_tipo_pedido text;
	v_quantidade real;
	v_item RECORD;

BEGIN
	-- Validacoes
	IF (SELECT pedido.situacao FROM soad.pedido WHERE id_pedido = v_id_pedido) <> 'ENCERRADO' THEN
		RAISE EXCEPTION 'O pedido precisa estar encerrado para gerar um lote.';
	END IF;
		
	BEGIN
		
		-- Identifica qual o tipo de pedido para tratar
		SELECT pedido.tipo_pedido INTO v_tipo_pedido 
		FROM soad.pedido WHERE id_pedido = v_id_pedido;
		
		-- registrar um novo lote
		IF v_tipo_pedido = 'COMPRA' THEN
			
			<<LOTE>>
			FOR v_item IN 
				SELECT 
					id_item_pedido
					, fk_mercadoria_id
					, quantidade
					, fk_unidade_medida_id
					, valor_unitario 
				FROM soad.item_pedido
				WHERE item_pedido.fk_pedido_id = v_id_pedido
			LOOP
				--RAISE EXCEPTION '%', v_item;
			
				WITH t_lote as (
					INSERT INTO soad.lote 
						(fk_mercadoria_id, fk_pedido_id, fk_unidade_medida_id, valor_unitario)
					VALUES 
						(v_item.fk_mercadoria_id, v_id_pedido, v_item.fk_unidade_medida_id, v_item.valor_unitario)
					RETURNING id_lote
					
				) SELECT id_lote INTO v_id_lote FROM t_lote;
				
				-- Caso aconteça de ser inserido um item com valor 'quebrado' vai ficar toda a quanitdade em um item_lote
				-- Ideal seria permitir que o usuário configurasse como seria feita a divisão dos item_lotes
				IF CEILING(v_item.quantidade) <> v_item.quantidade THEN -- Verifica se o valor é decimal
					v_quantidade := 1;
				ELSE
					v_quantidade := v_item.quantidade;
				END IF;
				
				<<ITEM_LOTE>>
				FOR n in 1..v_quantidade LOOP
					INSERT INTO soad.item_lote 
						(fk_lote_id, fk_item_pedido_entrada_id, quantidade_item)
					VALUES 
-- 					    se gerar um item_lote a quantidade total da mercadoria fica nele
-- 					    se gerar mais de um item_lote cada um terá a quantidade 1
						(v_id_lote, v_item.id_item_pedido, v_item.quantidade/v_quantidade);
						
					RAISE NOTICE '[Lote ID %] Cadastrado item_lote % do item_pedido (ID %)', v_id_lote, n, v_item.id_item_pedido;
					
					END LOOP ITEM_LOTE;
				
			END LOOP LOTE;

		ELSE 
			RAISE EXCEPTION 'Esse tipo de pedido não gera lote';
		END IF;
	END;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_gerar_lote"("p_id_pedido" integer) OWNER TO "postgres";

--
-- TOC entry 3238 (class 0 OID 0)
-- Dependencies: 271
-- Name: PROCEDURE "prc_gerar_lote"("p_id_pedido" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_gerar_lote"("p_id_pedido" integer) IS 'procedimento para gerar lote após a confirmação de um pedido';


--
-- TOC entry 277 (class 1255 OID 50126)
-- Name: prc_gerar_remanufatura(integer, integer, integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_gerar_remanufatura"("p_casco_id" integer, "p_insumo_id" integer, "p_quantidade" integer)
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_casco_id		 	integer		:= p_casco_id;
	v_insumo_id		 	integer		:= p_insumo_id;
	v_quantidade 	 	integer		:= p_quantidade;
	v_remanufatura_id	integer;
	v_id_item_lote 		integer;

BEGIN
	IF v_quantidade <= 0 THEN
		RAISE EXCEPTION 'Quantidade não pode ser 0';
	END IF;
	
	FOR i IN 1..v_quantidade 
	LOOP
		-- cadastra remanufatura
		BEGIN
			WITH t_remanufatura AS (
				INSERT INTO soad.remanufatura (fk_casco_id, fk_insumo_id, situacao)
				VALUES (v_casco_id, v_insumo_id, 'CADASTRADA')
				RETURNING id_remanufatura
			) 
			SELECT id_remanufatura 
			INTO v_remanufatura_id
			FROM t_remanufatura;
		END;
		
		-- Movimenta o estoque para essa remanufatura
		BEGIN
			CALL soad.prc_realizar_remanufatura(v_remanufatura_id);
		END;
		
	END LOOP;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER PROCEDURE "soad"."prc_gerar_remanufatura"("p_casco_id" integer, "p_insumo_id" integer, "p_quantidade" integer) OWNER TO "postgres";

--
-- TOC entry 268 (class 1255 OID 17241)
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
-- TOC entry 3239 (class 0 OID 0)
-- Dependencies: 268
-- Name: PROCEDURE "prc_insert_modalidade"("p_modalidade" "text"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_insert_modalidade"("p_modalidade" "text") IS 'Cadastrar modalidades de pessoas';


--
-- TOC entry 267 (class 1255 OID 49997)
-- Name: prc_insert_municipio_estado_pais("text", "text", "text", "text", "text", "text"); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_insert_municipio_estado_pais"("p_municipio_nome" "text", "p_cod_ibge" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text")
    LANGUAGE "plpgsql"
    AS $$DECLARE
	-- Pega os parametros e deixa em maiusculo
	v_municipio_nome text := upper(p_municipio_nome);
	v_cod_ibge text := p_cod_ibge;
	v_estado_nome text := upper(p_estado_nome);
	v_estado_sigla text := upper(p_estado_sigla);
	v_pais_sigla text := upper(p_pais_sigla);
	v_pais_nome text := upper(p_pais_nome);
	v_data_cadastro date := statement_timestamp();
	-- variaveis auxiliares
	v_aux integer := NULL;

BEGIN
	------ É possível inserir apenas o estado ou apenas o pais caso municipio ou municipio e estado estejam em branco -------
	
	-- Insere apenas pais OU atualiza o pais
	IF v_municipio_nome = '' AND v_estado_nome = '' AND v_pais_nome <> '' THEN
	
		INSERT INTO soad.pais (nome, sigla)
		VALUES (v_pais_nome, v_pais_sigla); 
		
	RETURN;
	
	-- Insere apenas estado
	ELSIF v_municipio_nome = '' AND v_estado_nome <> '' AND v_pais_nome <> '' THEN

		SELECT id_pais into v_aux FROM soad.pais WHERE pais.sigla = v_pais_sigla;

		INSERT INTO soad.estado (fk_pais_id, nome, sigla)
		VALUES (v_aux, v_estado_nome, v_estado_sigla);
		
	RETURN;
	
	END IF;

   -- Precisa dessa separacao por que se não tiver inserido o registro pai ainda 
   -- o postgres nao acha a chave primaria pra colocar como estrangeira no filho
   
   -------- A partir daqui tenta inserir novo pais, novo estado e nova municipio ---------
	
	-- valida parametros
	IF v_pais_nome = '' OR v_pais_sigla = '' THEN
		RAISE EXCEPTION 'É preciso informar um país.';
	ELSIF v_estado_nome = '' OR v_estado_sigla = '' THEN
		RAISE EXCEPTION 'É preciso informar um estado.';
	ELSIF v_municipio_nome = '' THEN
		RAISE EXCEPTION 'É preciso informar uma municipio';
	END IF;
	
	-- Insere municipio, estado e pais
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
		INSERT INTO soad.municipio (fk_estado_id, nome, cod_ibge)
		SELECT id_estado, v_municipio_nome, v_cod_ibge
		FROM t_estado;
	
	RETURN;
		
	-- Insere novo estado e novo municipio
	ELSIF (SELECT count(*) FROM soad.estado WHERE estado.sigla = v_estado_sigla) = 0 THEN
		
		SELECT id_pais into v_aux FROM soad.pais WHERE pais.sigla = v_pais_sigla;
	
		WITH t_estado AS (
		  INSERT INTO soad.estado (fk_pais_id, nome, sigla)
		  VALUES (v_aux, v_estado_nome, v_estado_sigla)
		  RETURNING id_estado
		)
		INSERT INTO soad.municipio (fk_estado_id, nome, cod_ibge)
		SELECT id_estado, v_municipio_nome, v_cod_ibge
		FROM t_estado;
	
	RETURN;
		
	-- Insere apenas nova municipio
	ELSIF (SELECT count(*) FROM soad.municipio WHERE municipio.nome = v_municipio_nome) = 0 THEN
		
		SELECT estado.id_estado into v_aux 
		FROM soad.estado 
		INNER JOIN soad.pais ON estado.fk_pais_id = pais.id_pais
		WHERE estado.sigla = v_estado_sigla;

		INSERT INTO soad.municipio (fk_estado_id, nome, cod_ibge)
		VALUES (v_aux, v_municipio_nome, v_cod_ibge);
		
	RETURN;
	
	END IF;
	
	RAISE NOTICE 'ERRO: Nenhuma informação foi registrada';

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_insert_municipio_estado_pais"("p_municipio_nome" "text", "p_cod_ibge" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text") OWNER TO "postgres";

--
-- TOC entry 3240 (class 0 OID 0)
-- Dependencies: 267
-- Name: PROCEDURE "prc_insert_municipio_estado_pais"("p_municipio_nome" "text", "p_cod_ibge" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_insert_municipio_estado_pais"("p_municipio_nome" "text", "p_cod_ibge" "text", "p_estado_nome" "text", "p_estado_sigla" "text", "p_pais_nome" "text", "p_pais_sigla" "text") IS 'Procedimento para cadastro de municipio e estado e pais ou municipio ou estado ou pais';


--
-- TOC entry 269 (class 1255 OID 17541)
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
-- TOC entry 3241 (class 0 OID 0)
-- Dependencies: 269
-- Name: PROCEDURE "prc_insert_or_update_unidade_medida"("p_descricao" "text", "p_abreviacao" "text"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_insert_or_update_unidade_medida"("p_descricao" "text", "p_abreviacao" "text") IS 'Cadastra unidade de medida.
Se a abreviacao ja existir irá atualizar a descrição';


--
-- TOC entry 281 (class 1255 OID 50147)
-- Name: prc_movimentar_lote(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_movimentar_lote"("p_id_pedido" integer)
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_id_pedido integer = p_id_pedido;
	v_pedido RECORD;
	v_remanufatura RECORD;
	v_item_pedido RECORD;
	v_item_lote RECORD;
	v_item_lote_id integer;
	v_lote_id integer;
	v_quantidade real;
	v_quantidade_movimentada real := 0;
	v_mercadoria RECORD;

BEGIN
	-- Localiza lote mais antigo para cada mercadoria do pedido
	-- traz todos os item_pedido do pedido a ser encerrado
	SELECT id_pedido, fk_pessoa_id, tipo_pedido INTO v_pedido FROM soad.pedido
	WHERE pedido.id_pedido = v_id_pedido
	AND pedido.situacao = 'ENCERRADO';
	
	IF v_pedido IS NULL THEN
		RAISE EXCEPTION 'Pedido (ID %) não encontrado.', v_id_pedido;
	END IF;
	
	BEGIN
		<<ITEM_PEDIDO>>
		FOR v_item_pedido IN 
			-- pega todos os item_pedido do pedido v_id_pedido
			SELECT id_item_pedido, fk_mercadoria_id, quantidade FROM soad.item_pedido
			WHERE item_pedido.fk_pedido_id = v_id_pedido
		LOOP	
 				-- valida se permite venda da mercadoria
 				SELECT id_mercadoria, permite_venda, descricao INTO v_mercadoria
				FROM soad.mercadoria 
				WHERE id_mercadoria = v_item_pedido.fk_mercadoria_id;
				
 				IF v_mercadoria.permite_venda = FALSE THEN
 					RAISE EXCEPTION 'A mercadoria % - % não permite venda.', v_mercadoria.id_mercadoria, v_mercadoria.descricao;
 				END IF;
				
				-- todo: permitir que o usuário informe qual o lote a ser utilizado
				-- pega lote mais antigo que tem a mercadoria do item_pedido
				-- Para que isso não cause erro na movimentação foi criado a trg_pedido_mercadoria_unica
				-- Idealmente deveria permitir que informe mais de uma vez o mesmo item no pedido
				SELECT lote.id_lote INTO v_lote_id 
				FROM soad.lote
				INNER JOIN soad.item_pedido 
					ON lote.fk_mercadoria_id = v_item_pedido.fk_mercadoria_id
				WHERE item_pedido.id_item_pedido = v_item_pedido.id_item_pedido
					AND lote.vazio = false
				ORDER BY lote.data_cadastro ASC LIMIT 1; -- pega só uma linha
				
				IF v_lote_id IS NULL THEN
					
					SELECT id_mercadoria, descricao INTO v_mercadoria
					FROM soad.mercadoria
					WHERE id_mercadoria = v_item_pedido.fk_mercadoria_id;
					
					RAISE EXCEPTION 
						'Não há estoque disponível da mercadoria % - %. Por favor edite ou cadastre um novo pedido.'
						, v_mercadoria.id_mercadoria, v_mercadoria.descricao;
					
				END IF;
				
				--RAISE NOTICE 'Item pedido: (%) Lote: (%)', v_item_pedido.id_item_pedido, v_lote_id;

				IF CEILING(v_item_pedido.quantidade) <> v_item_pedido.quantidade THEN -- Verifica se o valor é decimal
					v_quantidade := 1;
				ELSE
					v_quantidade := v_item_pedido.quantidade;
				END IF;

				-- v_lote_id :: lote atual
				-- v_item_lote_id :: item_lote atual

				<<ITEM_LOTE>>
				FOR v_item_lote IN
					-- pega todos os item_lote do lote escolhido
					SELECT id_item_lote, fk_lote_id, quantidade_item FROM soad.item_lote
					WHERE item_lote.fk_lote_id = v_lote_id
					AND item_lote.aberto = false
					AND item_lote.quantidade_item > 0
				LOOP
					BEGIN
						
						IF v_item_lote IS NULL THEN
							
							RAISE EXCEPTION 
								'Não há estoque disponível da mercadoria % - %. Por favor edite ou cadastre um novo pedido. (Lote ID: %)'
								, v_mercadoria.id_mercadoria, v_mercadoria.descricao, v_lote_id;
								
						END IF;
						-- todo: permitir que o usuário informe qual o item_lote a ser utilizado
						v_item_lote_id := v_item_lote.id_item_lote;
						
						--RAISE NOTICE 'Lote/Item lote: (%/%)', v_item_lote.fk_lote_id, v_item_lote.id_item_lote;
						
						IF v_item_lote.quantidade_item = 0 THEN
							RAISE NOTICE 'Item_lote % vazio.', v_item_lote.id_item_lote;
							EXIT;
						END IF;
						
						BEGIN	
							RAISE NOTICE 'Atualizando Item lote (ID %) (Mercadoria)', v_item_lote_id;
							UPDATE soad.item_lote
							SET fk_item_pedido_saida_id=v_item_pedido.id_item_pedido
								, data_retirada=NOW()
								, motivo_retirada=CONCAT('Pedido ', v_id_pedido, ' Tipo: ', v_pedido.tipo_pedido)
								, quantidade_item=0
							WHERE item_lote.id_item_lote = v_item_lote_id;
							
							v_quantidade_movimentada := v_quantidade_movimentada + 1;

						EXCEPTION WHEN OTHERS THEN
							RAISE EXCEPTION 'Não foi possível movimentar o item (ID %) do lote (ID %).', v_item_lote_id, v_item_lote.fk_lote_id;
						END;
						
						RAISE NOTICE 'Quantidade: %', v_quantidade;
						
						v_quantidade = v_quantidade - 1;
						
						RAISE NOTICE 'v_quantidade=% e v_quantidade_movimentada=%', v_quantidade, v_quantidade_movimentada;
						
						IF v_quantidade = 0 THEN
							EXIT;
						END IF;
						
					END;
				END LOOP ITEM_LOTE;
				
				
				BEGIN
					CALL soad.prc_esvazia_lote(v_lote_id);
				END;

		END LOOP ITEM_PEDIDO;
	END;
	
	-- movimenta lote das remanufaturas a serem feitas
	BEGIN
		<<REMANUFATURA>>
		FOR v_remanufatura IN 
			-- pega todas as remanufaturas do pedido v_id_pedido
			SELECT id_remanufatura FROM soad.remanufatura
			WHERE remanufatura.fk_pedido_id = v_id_pedido
			AND remanufatura.situacao = 'CADASTRADA'
		LOOP
			RAISE NOTICE 'Remanufatura: (ID %)', v_remanufatura.id_remanufatura;
			BEGIN
			
				CALL soad.prc_realizar_remanufatura(v_remanufatura.id_remanufatura);
				
				UPDATE soad.remanufatura
				SET situacao='ENCERRADA'
				WHERE id_remanufatura = v_remanufatura.id_remanufatura;
				
			END;
			
		END LOOP REMANUFATURA;
	END;

--EXCEPTION WHEN OTHERS THEN
	--RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;	

END;
$$;


ALTER PROCEDURE "soad"."prc_movimentar_lote"("p_id_pedido" integer) OWNER TO "postgres";

--
-- TOC entry 283 (class 1255 OID 58186)
-- Name: prc_movimentar_lote_teste(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_movimentar_lote_teste"("p_id_pedido" integer)
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_pedido_id integer = p_id_pedido;
	v_pedido RECORD;
	v_remanufatura RECORD;
	v_item_pedido RECORD;
	v_item_lote RECORD;
	v_item_lote_id integer;
	v_lote_id integer;
	v_quantidade real;
	v_quantidade_movimentada real := 0;
	v_mercadoria RECORD;

BEGIN
	-- Localiza lote mais antigo para cada mercadoria do pedido
	-- traz todos os item_pedido do pedido a ser encerrado
	SELECT id_pedido, fk_pessoa_id, tipo_pedido INTO v_pedido FROM soad.pedido
	WHERE pedido.id_pedido = v_pedido_id
	AND pedido.situacao = 'ENCERRADO';
	
	IF v_pedido IS NULL THEN
		RAISE EXCEPTION 'Pedido (ID %) não encontrado.', v_pedido_id;
	END IF;
	
	BEGIN
		<<ITEM_PEDIDO>>
		FOR v_item_pedido IN 
			-- pega todos os item_pedido do pedido v_pedido_id
			-- vicular item_pedido > lote
			SELECT 
				  ip.id_pedido
				, ip.id_mercadoria
				, ip.id_item_pedido
				, il.id_item_lote
				, ip.descricao
				, ip.quantidade 
				, il.id_lote
				, il.id_pedido_entrada
				, il.quantidade_item
			FROM soad.vw_item_pedido ip
			JOIN soad.vw_item_lote il 
				ON ip.id_mercadoria = il.id_mercadoria 
			WHERE ip.id_pedido = 266
				AND il.aberto = False
				AND il.vazio = False
				AND il.quantidade_item > 0
			
		LOOP	
		
				IF v_item_pedido IS NULL THEN
					
					SELECT id_mercadoria, descricao INTO v_mercadoria
					FROM soad.mercadoria
					WHERE id_mercadoria = v_item_pedido.fk_mercadoria_id;
					
					RAISE EXCEPTION 
						'Não há estoque disponível da mercadoria % - %. Por favor edite ou cadastre um novo pedido.'
						, v_mercadoria.id_mercadoria, v_mercadoria.descricao;
					
				END IF;
				
				RAISE NOTICE 'Item pedido: (%) Lote: (%)', v_item_pedido.id_item_pedido, v_lote_id;

				IF CEILING(v_item_pedido.quantidade) <> v_item_pedido.quantidade THEN -- Verifica se o valor é decimal
					v_quantidade := 1;
				ELSE
					v_quantidade := v_item_pedido.quantidade;
				END IF;

				-- v_lote_id = lote atual
				-- v_item_lote_id = item_lote atual

				<<ITEM_LOTE>>
				FOR v_item_lote IN
					-- pega todos os item_lote do lote escolhido
					SELECT id_item_lote, fk_lote_id, quantidade_item FROM soad.item_lote
					WHERE item_lote.fk_lote_id = v_lote_id
					AND item_lote.aberto = false
					AND item_lote.quantidade_item > 0
				LOOP
					BEGIN
						
						IF v_item_lote IS NULL THEN
							
							RAISE EXCEPTION 
								'Não há estoque disponível da mercadoria % - %. Por favor edite ou cadastre um novo pedido. (Lote ID: %)'
								, v_mercadoria.id_mercadoria, v_mercadoria.descricao, v_lote_id;
								
						END IF;
						-- todo: permitir que o usuário informe qual o item_lote a ser utilizado
						v_item_lote_id := v_item_lote.id_item_lote;
						
						--RAISE NOTICE 'Lote/Item lote: (%/%)', v_item_lote.fk_lote_id, v_item_lote.id_item_lote;
						
						IF v_item_lote.quantidade_item = 0 THEN
							RAISE NOTICE 'Item_lote % vazio.', v_item_lote.id_item_lote;
							EXIT;
						END IF;
						
						BEGIN	
							RAISE NOTICE 'Atualizando Item lote (ID %) (Mercadoria)', v_item_lote_id;
							UPDATE soad.item_lote
							SET fk_item_pedido_saida_id=v_item_pedido.id_item_pedido
								, data_retirada=NOW()
								, motivo_retirada=CONCAT('Pedido ', v_pedido_id, ' Tipo: ', v_pedido.tipo_pedido)
								, quantidade_item=0
							WHERE item_lote.id_item_lote = v_item_lote_id;
							
							v_quantidade_movimentada := v_quantidade_movimentada + 1;

						EXCEPTION WHEN OTHERS THEN
							RAISE EXCEPTION 'Não foi possível movimentar o item (ID %) do lote (ID %).', v_item_lote_id, v_item_lote.fk_lote_id;
						END;
						
						RAISE NOTICE 'Quantidade: %', v_quantidade;
						
						v_quantidade = v_quantidade - 1;
						
						RAISE NOTICE 'v_quantidade=% e v_quantidade_movimentada=%', v_quantidade, v_quantidade_movimentada;
						
						IF v_quantidade = 0 THEN
							EXIT;
						END IF;
						
					END;
				END LOOP ITEM_LOTE;
				
				
				BEGIN
					CALL soad.prc_esvazia_lote(v_lote_id);
				END;

		END LOOP ITEM_PEDIDO;
	END;
	
	-- movimenta lote das remanufaturas a serem feitas
	BEGIN
		<<REMANUFATURA>>
		FOR v_remanufatura IN 
			-- pega todas as remanufaturas do pedido v_pedido_id
			SELECT id_remanufatura FROM soad.remanufatura
			WHERE remanufatura.fk_pedido_id = v_pedido_id
			AND remanufatura.situacao = 'CADASTRADA'
		LOOP
			RAISE NOTICE 'Remanufatura: (ID %)', v_remanufatura.id_remanufatura;
			BEGIN	
				CALL soad.prc_realizar_remanufatura(v_remanufatura.id_remanufatura);
			END;
			
		END LOOP REMANUFATURA;
	END;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;	

END;
$$;


ALTER PROCEDURE "soad"."prc_movimentar_lote_teste"("p_id_pedido" integer) OWNER TO "postgres";

--
-- TOC entry 285 (class 1255 OID 50137)
-- Name: prc_realizar_remanufatura(integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_realizar_remanufatura"("p_id_remanufatura" integer)
    LANGUAGE "plpgsql"
    AS $$DECLARE
	v_id_remanufatura 	integer = p_id_remanufatura;
	v_id_insumo			integer;
	v_insumo			RECORD;
	v_item_lote			RECORD;
	
BEGIN
	
	IF (SELECT situacao FROM soad.remanufatura WHERE remanufatura.id_remanufatura = v_id_remanufatura) = 'REALIZADA' THEN
		RAISE EXCEPTION 'A remanufatura (%) já foi realizada.', v_id_remanufatura;
	END IF;
	
	SELECT fk_insumo_id INTO v_id_insumo 
	FROM soad.remanufatura
	WHERE remanufatura.id_remanufatura = v_id_remanufatura;
	
	-- localiza lotes que podem ser utilizados
	WITH t_item_lote as (
		SELECT item_lote.id_item_lote, item_lote.aberto, item_lote.fk_lote_id as id_lote
		FROM soad.vw_insumo
			INNER JOIN soad.lote ON vw_insumo.id_mercadoria = lote.fk_mercadoria_id
			LEFT JOIN  soad.item_lote ON lote.id_lote = item_lote.fk_lote_id
		WHERE vw_insumo.id_insumo = v_id_insumo
			AND lote.vazio = false							-- lote não pode estar vazio
			AND item_lote.fk_item_pedido_saida_id IS null 	-- item que ainda não teve saída
		ORDER BY lote.data_cadastro ASC
	)
	-- localiza primeiro item_lote que pode ser utilizado
	SELECT id_item_lote, id_lote INTO v_item_lote
	  FROM t_item_lote
	  ORDER BY t_item_lote.aberto DESC 
	LIMIT 1;
	
	IF v_item_lote.id_item_lote IS NULL THEN
		SELECT id_insumo, descricao INTO v_insumo FROM soad.vw_insumo
		WHERE id_insumo = v_id_insumo;
		RAISE EXCEPTION 'Não há estoque do insumo % - % disponível para remanufatura.', v_id_insumo, v_insumo.descricao;
	END IF;
	
	RAISE NOTICE 'Item lote a ser movimentado para remanufatura: (%)', v_item_lote.id_item_lote;
	
	-- movimenta lote
	BEGIN
	
		RAISE NOTICE 'Atualizando lote (Remanufatura)';
		
		BEGIN
			UPDATE soad.item_lote
			SET aberto=true
				, motivo_retirada='Remanufatura (operação interna)'
				, data_retirada=NOW()
			WHERE item_lote.id_item_lote = v_item_lote.id_item_lote;
		END;
		
		-- Atualiza lote se está vazio ou não
		BEGIN
			CALL soad.prc_esvazia_lote(v_item_lote.id_lote::integer);
		END;

		-- Atualiza remanufatura
		RAISE NOTICE 'Atualizando Remanufatura';
		
		BEGIN
			UPDATE soad.remanufatura
			SET situacao = 'REALIZADA'
			WHERE remanufatura.id_remanufatura = v_id_remanufatura;
		END;
		
		-- Criar relacionamento entre item_lote e remanufatura
		RAISE NOTICE 'Relacionando remanufatura e item';
		
		BEGIN
			INSERT INTO soad.item_lote_remanufatura(fk_remanufatura_id, fk_item_lote_id)
			VALUES(v_id_remanufatura, v_item_lote.id_item_lote);
		END;

		RAISE NOTICE 'Remanufatura % realizada.', v_id_remanufatura;
	END;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER PROCEDURE "soad"."prc_realizar_remanufatura"("p_id_remanufatura" integer) OWNER TO "postgres";

--
-- TOC entry 3242 (class 0 OID 0)
-- Dependencies: 285
-- Name: PROCEDURE "prc_realizar_remanufatura"("p_id_remanufatura" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_realizar_remanufatura"("p_id_remanufatura" integer) IS 'Movimenta o lote da remanufatura informada';


--
-- TOC entry 270 (class 1255 OID 25399)
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
		ON CONFLICT ON CONSTRAINT ukc_modalidade_id_pessoa_id DO NOTHING;
	ELSE
		RAISE EXCEPTION 'Pessoa não encontrada para o documento %', v_documento;
	END IF;

END;
$$;


ALTER PROCEDURE "soad"."prc_vincular_modalidade_pessoa"("p_modalidade_id" integer, "p_documento" "text") OWNER TO "postgres";

--
-- TOC entry 3243 (class 0 OID 0)
-- Dependencies: 270
-- Name: PROCEDURE "prc_vincular_modalidade_pessoa"("p_modalidade_id" integer, "p_documento" "text"); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_vincular_modalidade_pessoa"("p_modalidade_id" integer, "p_documento" "text") IS 'Vincula uma modalidade a uma pessoa';


--
-- TOC entry 301 (class 1255 OID 99178)
-- Name: prc_vincular_pedido_mercadoria(integer, integer, integer, real, real, integer); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_vincular_pedido_mercadoria"("p_pedido_id" integer, "p_mercadoria_id" integer, "p_unidade_medida_id" integer, "p_quantidade" real, "p_valor_unitario" real, "p_item_pedido_id" integer DEFAULT NULL::integer)
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_item_pedido_id	integer		:= p_item_pedido_id;
	v_pedido_id		 	integer		:= p_pedido_id;
	v_mercadoria_id 	integer		:= p_mercadoria_id;
	v_quantidade 	 	real		:= p_quantidade;
	v_valor_unitario 	real		:= p_valor_unitario;
	v_unidade_medida_id integer		:= p_unidade_medida_id;
	v_mercadoria 		RECORD;
	v_pedido			RECORD;	
	
	
BEGIN
	
	--valida se permite venda da mercadoria
	SELECT permite_venda, descricao INTO v_mercadoria
	FROM soad.mercadoria 
	WHERE id_mercadoria = v_mercadoria_id;
	
	SELECT id_pedido, tipo_pedido INTO v_pedido
	FROM soad.pedido
	WHERE id_pedido = v_pedido_id;
	
	IF v_mercadoria.permite_venda = FALSE AND v_pedido.tipo_pedido = 'VENDA' THEN
		RAISE EXCEPTION 'A mercadoria % - % não permite venda.', v_mercadoria_id, v_mercadoria.descricao;
	END IF;
	
	-- Cria ou atualiza vinculo
	IF v_item_pedido_id IS NULL THEN
		INSERT INTO soad.item_pedido (fk_pedido_id, fk_mercadoria_id, fk_unidade_medida_id, quantidade, valor_unitario)
		VALUES (v_pedido_id, v_mercadoria_id, v_unidade_medida_id, v_quantidade, v_valor_unitario);
		RAISE NOTICE 'Novo Item_pedido cadastrado';
	ELSE
		UPDATE soad.item_pedido
		SET fk_mercadoria_id=v_mercadoria_id
			, fk_unidade_medida_id=v_unidade_medida_id
			, quantidade=v_quantidade
			, valor_unitario=v_valor_unitario
		WHERE id_item_pedido = v_item_pedido_id;
		RAISE NOTICE 'Item_pedido atualizado';
	END IF;
	
	
EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;
	
END;
$$;


ALTER PROCEDURE "soad"."prc_vincular_pedido_mercadoria"("p_pedido_id" integer, "p_mercadoria_id" integer, "p_unidade_medida_id" integer, "p_quantidade" real, "p_valor_unitario" real, "p_item_pedido_id" integer) OWNER TO "postgres";

--
-- TOC entry 3244 (class 0 OID 0)
-- Dependencies: 301
-- Name: PROCEDURE "prc_vincular_pedido_mercadoria"("p_pedido_id" integer, "p_mercadoria_id" integer, "p_unidade_medida_id" integer, "p_quantidade" real, "p_valor_unitario" real, "p_item_pedido_id" integer); Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON PROCEDURE "soad"."prc_vincular_pedido_mercadoria"("p_pedido_id" integer, "p_mercadoria_id" integer, "p_unidade_medida_id" integer, "p_quantidade" real, "p_valor_unitario" real, "p_item_pedido_id" integer) IS 'vincula uma mercadoria a um pedido, não deve ser chamado diretamente, utilizar prc_cadastro_pedido';


--
-- TOC entry 276 (class 1255 OID 50136)
-- Name: prc_vincular_pedido_remanufatura(integer, integer, integer, real, real, boolean); Type: PROCEDURE; Schema: soad; Owner: postgres
--

CREATE PROCEDURE "soad"."prc_vincular_pedido_remanufatura"("p_pedido_id" integer, "p_casco_id" integer, "p_insumo_id" integer, "p_quantidade" real, "p_valor_unitario" real, "p_nova_remanufatura" boolean)
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_pedido_id		 	integer		:= p_pedido_id;
	v_casco_id		 	integer		:= p_casco_id;
	v_insumo_id			integer		:= p_insumo_id;
	v_quantidade 	 	integer		:= p_quantidade;
	v_qtd_vinculada		integer		:= 0;
	v_valor_unitario 	real		:= p_valor_unitario;
	v_nova_remanufatura boolean		:= p_nova_remanufatura; -- define se força a usar um casco que já esta remanufaturado
	v_id_remanufatura 	integer;
	v_pedido			RECORD;

BEGIN

	SELECT situacao, tipo_pedido INTO v_pedido
	FROM soad.vw_pedido 
	WHERE id_pedido = v_pedido_id;
	
	IF v_pedido.situacao <> 'CADASTRADO' THEN
		RAISE EXCEPTION 'Para vincular uma remanufatura o pedido precisa estar na situacao CADASTRADO';
	ELSIF v_pedido.tipo_pedido = 'COMPRA' THEN
		RAISE EXCEPTION 'Não é possível víncular uma remanufatura a um pedido do tipo COMPRA';
	END IF;
	
	--procurar remanufatura existente
	IF v_nova_remanufatura = false THEN
		-- procurar remanufatura e vincular com pedido
		FOR i IN 1..v_quantidade 
		LOOP
			SELECT id_remanufatura INTO v_id_remanufatura
				FROM soad.remanufatura
				WHERE remanufatura.fk_pedido_id is null
					AND remanufatura.fk_casco_id = v_casco_id
					AND remanufatura.fk_insumo_id = v_insumo_id
					AND remanufatura.situacao = 'REALIZADA'
				LIMIT 1;
				
			IF v_id_remanufatura IS NOT null THEN
					UPDATE soad.remanufatura
					SET fk_pedido_id=v_pedido_id
						, valor_unitario=v_valor_unitario
					WHERE remanufatura.id_remanufatura = v_id_remanufatura;
					
					v_qtd_vinculada = v_qtd_vinculada + 1;
					RAISE NOTICE 'Pedido vinculado a remanufatura % já existente.', v_id_remanufatura;
			END IF;
		END LOOP;	
	END IF;
	
	IF v_qtd_vinculada < v_quantidade THEN
	
		FOR i IN 1..(v_quantidade - v_qtd_vinculada)
		LOOP
			-- cadastrar nova
			INSERT INTO soad.remanufatura (fk_pedido_id, fk_casco_id, fk_insumo_id, valor_unitario, situacao)
			VALUES (v_pedido_id, v_casco_id, v_insumo_id, v_valor_unitario, 'CADASTRADA');

			RAISE NOTICE 'Nova remanufatura cadastrada.';

		END LOOP;
	END IF;

EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$$;


ALTER PROCEDURE "soad"."prc_vincular_pedido_remanufatura"("p_pedido_id" integer, "p_casco_id" integer, "p_insumo_id" integer, "p_quantidade" real, "p_valor_unitario" real, "p_nova_remanufatura" boolean) OWNER TO "postgres";

--
-- TOC entry 286 (class 1255 OID 58249)
-- Name: trg_auditoria(); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."trg_auditoria"() RETURNS "trigger"
    LANGUAGE "plpgsql"
    AS $$
DECLARE
	v_record RECORD;
	v_new RECORD;
	v_old RECORD;
	

BEGIN
		
	IF TG_OP = 'UPDATE' THEN
	-- Criar forma de peagr apenas o que está diferente
	
-- 		select * into v_old from OLD.TG_TABLE;
-- 		select * into v_new from NEW;
		
	
-- 		v_old = each(hstore(v_old));
-- 		v_new = each(hstore(v_new));

-- 		SELECT v_new.key, v_new.value INTO v_record FROM v_old
-- 		INNER JOIN v_new ON v_old.key = v_new.key
-- 		WHERE v_new.value <> v_old.value;
		
	END IF;

	INSERT INTO soad.auditoria(
		nome_tabela
		--, nome_coluna
		, operacao
		, old_value
		, new_value
		, usuario
		, data
	)
	VALUES(
		TG_TABLE_NAME
		--, nomecoluna
		, TG_OP
		, row_to_json(OLD)
		, row_to_json(NEW)
		, USER
		, NOW()
	);
	
	RETURN NEW;
END;
$$;


ALTER FUNCTION "soad"."trg_auditoria"() OWNER TO "postgres";

--
-- TOC entry 273 (class 1255 OID 50192)
-- Name: trg_chamada_metodo(); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."trg_chamada_metodo"() RETURNS "trigger"
    LANGUAGE "plpgsql"
    AS $$
    BEGIN

		IF NEW.mensagem IS NOT NULL OR NEW.retorno = '0' 
		THEN
			BEGIN
				RAISE EXCEPTION 
					'Não foi possível executar a operacao.\n Método: % \n Retorno: % \n Parametros: % \n Requisicao: ID %'
					, NEW.metodo, NEW.mensagem, NEW.params_json, NEW.id_requisicao;
			EXCEPTION WHEN OTHERS THEN
				RETURN NEW;
			END;
		ELSE
			RETURN NEW;
		END IF;

    END;
  $$;


ALTER FUNCTION "soad"."trg_chamada_metodo"() OWNER TO "postgres";

--
-- TOC entry 284 (class 1255 OID 58188)
-- Name: trg_pedido_mercadoria_unica(); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."trg_pedido_mercadoria_unica"() RETURNS "trigger"
    LANGUAGE "plpgsql"
    AS $$
    BEGIN
	
		IF (SELECT COUNT(*) FROM soad.item_pedido
			WHERE fk_pedido_id = NEW.fk_pedido_id
		   	AND fk_mercadoria_id = NEW.fk_mercadoria_id) > 0 
		THEN
			RAISE EXCEPTION 'A mesma mercadoria não pode constar duas vezes no mesmo pedido.';
		ELSE 
			RETURN NEW;
		END IF;

    END;
  $$;


ALTER FUNCTION "soad"."trg_pedido_mercadoria_unica"() OWNER TO "postgres";

--
-- TOC entry 287 (class 1255 OID 58191)
-- Name: trg_remover_lote_com_vinculo(); Type: FUNCTION; Schema: soad; Owner: postgres
--

CREATE FUNCTION "soad"."trg_remover_lote_com_vinculo"() RETURNS "trigger"
    LANGUAGE "plpgsql"
    AS $$
    BEGIN
		
		IF OLD.fk_item_pedido_saida_id IS NOT NULL THEN
			RAISE EXCEPTION 'Não é possível remover um item de lote vínculado a um pedido de saída.';
		ELSIF OLD.aberto = True THEN
			RAISE EXCEPTION 'Não é possível remover um item aberto do lote.';
		ELSIF OLD.quantidade_item = 0 THEN
			RAISE EXCEPTION 'Não é possível remover um item sem saldo.';
		ELSIF (SELECT COUNT(*) FROM soad.item_lote_remanufatura WHERE fk_item_lote_id = OLD.id_item_lote) > 0 THEN
			RAISE EXCEPTION 'Não é possível remover um item com remanufatura realizada.';
		ELSE
			RETURN NEW;
		END IF;

    END;
  $$;


ALTER FUNCTION "soad"."trg_remover_lote_com_vinculo"() OWNER TO "postgres";

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 249 (class 1259 OID 58232)
-- Name: auditoria; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."auditoria" (
    "id_auditoria" integer NOT NULL,
    "nome_tabela" "text",
    "nome_coluna" "text",
    "operacao" "text",
    "old_value" "text",
    "new_value" "text",
    "usuario" "text",
    "data" timestamp(3) without time zone
);


ALTER TABLE "soad"."auditoria" OWNER TO "postgres";

--
-- TOC entry 248 (class 1259 OID 58230)
-- Name: auditoria_id_auditoria_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."auditoria_id_auditoria_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."auditoria_id_auditoria_seq" OWNER TO "postgres";

--
-- TOC entry 3245 (class 0 OID 0)
-- Dependencies: 248
-- Name: auditoria_id_auditoria_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."auditoria_id_auditoria_seq" OWNED BY "soad"."auditoria"."id_auditoria";


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
-- TOC entry 228 (class 1259 OID 16998)
-- Name: endereco; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."endereco" (
    "id_endereco" integer NOT NULL,
    "fk_municipio_id" integer NOT NULL,
    "fk_pessoa_id" integer NOT NULL,
    "logradouro" character varying(150) NOT NULL,
    "numero" character varying(5),
    "bairro" character varying(100),
    "cep" character varying(8),
    "complemento" character varying(60),
    "tipo" character varying(20),
    CONSTRAINT "cc_endereco_tipo" CHECK (((("tipo")::"text" = 'RESIDENCIAL'::"text") OR (("tipo")::"text" = 'COMERCIAL'::"text")))
);


ALTER TABLE "soad"."endereco" OWNER TO "postgres";

--
-- TOC entry 3246 (class 0 OID 0)
-- Dependencies: 228
-- Name: COLUMN "endereco"."tipo"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."endereco"."tipo" IS 'COMERCIAL, RESIDENCIAL';


--
-- TOC entry 3247 (class 0 OID 0)
-- Dependencies: 228
-- Name: CONSTRAINT "cc_endereco_tipo" ON "endereco"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "cc_endereco_tipo" ON "soad"."endereco" IS 'Endereço pode ser comercial ou residencial';


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
-- TOC entry 3248 (class 0 OID 0)
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
-- TOC entry 3249 (class 0 OID 0)
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
-- TOC entry 3250 (class 0 OID 0)
-- Dependencies: 209
-- Name: insumo_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."insumo_id_seq" OWNED BY "soad"."insumo"."id_insumo";


--
-- TOC entry 224 (class 1259 OID 16982)
-- Name: item_lote; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."item_lote" (
    "id_item_lote" integer NOT NULL,
    "fk_lote_id" bigint NOT NULL,
    "fk_item_pedido_saida_id" bigint,
    "data_validade" "date",
    "lote_fabricante" character varying(60),
    "data_retirada" timestamp(4) with time zone,
    "motivo_retirada" character varying(300),
    "quantidade_item" real DEFAULT 1 NOT NULL,
    "fk_item_pedido_entrada_id" integer NOT NULL,
    "data_cadastro" "date" DEFAULT "now"() NOT NULL,
    "aberto" boolean DEFAULT false NOT NULL
);


ALTER TABLE "soad"."item_lote" OWNER TO "postgres";

--
-- TOC entry 3251 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN "item_lote"."fk_item_pedido_saida_id"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."item_lote"."fk_item_pedido_saida_id" IS 'ID do item_pedido de saída desse item_lote';


--
-- TOC entry 3252 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN "item_lote"."quantidade_item"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."item_lote"."quantidade_item" IS 'Quantidade de itens (unidade de medida do lote) que esse item_lote representa';


--
-- TOC entry 3253 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN "item_lote"."fk_item_pedido_entrada_id"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."item_lote"."fk_item_pedido_entrada_id" IS 'id do item_pedido que gerou o item_lote';


--
-- TOC entry 3254 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN "item_lote"."aberto"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."item_lote"."aberto" IS 'define se o item do lote foi aberto ou não (insumo)';


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
-- TOC entry 3255 (class 0 OID 0)
-- Dependencies: 223
-- Name: item_lote_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."item_lote_id_seq" OWNED BY "soad"."item_lote"."id_item_lote";


--
-- TOC entry 245 (class 1259 OID 50279)
-- Name: item_lote_remanufatura; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."item_lote_remanufatura" (
    "id_item_lote_remanufatura" integer NOT NULL,
    "fk_remanufatura_id" integer NOT NULL,
    "fk_item_lote_id" integer NOT NULL,
    "data_cadastro" "date" DEFAULT "now"() NOT NULL
);


ALTER TABLE "soad"."item_lote_remanufatura" OWNER TO "postgres";

--
-- TOC entry 3256 (class 0 OID 0)
-- Dependencies: 245
-- Name: TABLE "item_lote_remanufatura"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON TABLE "soad"."item_lote_remanufatura" IS 'relacionamento entre item_lote e remanufaturas';


--
-- TOC entry 244 (class 1259 OID 50277)
-- Name: item_lote_remanufatura_id_remanufatura_item_lote_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."item_lote_remanufatura_id_remanufatura_item_lote_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."item_lote_remanufatura_id_remanufatura_item_lote_seq" OWNER TO "postgres";

--
-- TOC entry 3257 (class 0 OID 0)
-- Dependencies: 244
-- Name: item_lote_remanufatura_id_remanufatura_item_lote_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."item_lote_remanufatura_id_remanufatura_item_lote_seq" OWNED BY "soad"."item_lote_remanufatura"."id_item_lote_remanufatura";


--
-- TOC entry 222 (class 1259 OID 16974)
-- Name: item_pedido; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."item_pedido" (
    "id_item_pedido" integer NOT NULL,
    "fk_pedido_id" integer NOT NULL,
    "fk_mercadoria_id" integer NOT NULL,
    "quantidade" integer NOT NULL,
    "valor_unitario" numeric NOT NULL,
    "fk_unidade_medida_id" integer NOT NULL
);


ALTER TABLE "soad"."item_pedido" OWNER TO "postgres";

--
-- TOC entry 3258 (class 0 OID 0)
-- Dependencies: 222
-- Name: COLUMN "item_pedido"."fk_unidade_medida_id"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."item_pedido"."fk_unidade_medida_id" IS 'unidade de medida do item';


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
-- TOC entry 3259 (class 0 OID 0)
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
    "data_cadastro" "date" DEFAULT "now"() NOT NULL,
    "vazio" boolean DEFAULT false NOT NULL,
    "observacao" character varying(300),
    "fk_mercadoria_id" integer NOT NULL,
    "valor_unitario" numeric NOT NULL,
    "fk_unidade_medida_id" integer NOT NULL
);


ALTER TABLE "soad"."lote" OWNER TO "postgres";

--
-- TOC entry 3260 (class 0 OID 0)
-- Dependencies: 226
-- Name: COLUMN "lote"."fk_pedido_id"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."lote"."fk_pedido_id" IS 'ID do pedido de entrada da mercadoria';


--
-- TOC entry 3261 (class 0 OID 0)
-- Dependencies: 226
-- Name: COLUMN "lote"."fk_mercadoria_id"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."lote"."fk_mercadoria_id" IS 'mercadoria a qual o lote representa';


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
-- TOC entry 3262 (class 0 OID 0)
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
    "descricao" character varying(120) NOT NULL,
    "marca" character varying(80),
    "ativo" boolean DEFAULT true NOT NULL,
    "data_cadastro" "date" DEFAULT "now"() NOT NULL,
    "permite_venda" boolean DEFAULT true NOT NULL,
    "valor_venda" numeric(6,0)
);


ALTER TABLE "soad"."mercadoria" OWNER TO "postgres";

--
-- TOC entry 3263 (class 0 OID 0)
-- Dependencies: 206
-- Name: COLUMN "mercadoria"."permite_venda"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."mercadoria"."permite_venda" IS 'define se é permitida a venda dessa mercadoria';


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
-- TOC entry 3264 (class 0 OID 0)
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
-- TOC entry 3265 (class 0 OID 0)
-- Dependencies: 213
-- Name: modalidade_pessoa_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."modalidade_pessoa_id_seq" OWNED BY "soad"."modalidade_pessoa"."id_modalidade_pessoa";


--
-- TOC entry 230 (class 1259 OID 17006)
-- Name: municipio; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."municipio" (
    "id_municipio" integer NOT NULL,
    "fk_estado_id" integer NOT NULL,
    "nome" character varying(120) NOT NULL,
    "cod_ibge" character varying(6)
);


ALTER TABLE "soad"."municipio" OWNER TO "postgres";

--
-- TOC entry 229 (class 1259 OID 17004)
-- Name: municipio_id_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."municipio_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."municipio_id_seq" OWNER TO "postgres";

--
-- TOC entry 3266 (class 0 OID 0)
-- Dependencies: 229
-- Name: municipio_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."municipio_id_seq" OWNED BY "soad"."municipio"."id_municipio";


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
-- TOC entry 3267 (class 0 OID 0)
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
    "tipo_pedido" character varying(10) NOT NULL,
    "data_cadastro" timestamp(4) with time zone DEFAULT "now"() NOT NULL,
    "observacao" character varying(300),
    "situacao" character varying(10) NOT NULL,
    CONSTRAINT "cc_pedido_situacao" CHECK (((("situacao")::"text" = 'CADASTRADO'::"text") OR (("situacao")::"text" = 'ENCERRADO'::"text") OR (("situacao")::"text" = 'CANCELADO'::"text") OR (("situacao")::"text" = 'ESTORNADO'::"text"))),
    CONSTRAINT "cc_pedido_tipo_pedido" CHECK (((("tipo_pedido")::"text" = 'COMPRA'::"text") OR (("tipo_pedido")::"text" = 'VENDA'::"text")))
);


ALTER TABLE "soad"."pedido" OWNER TO "postgres";

--
-- TOC entry 3268 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN "pedido"."tipo_pedido"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."pedido"."tipo_pedido" IS 'COMPRA ou VENDA';


--
-- TOC entry 3269 (class 0 OID 0)
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
-- TOC entry 3270 (class 0 OID 0)
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
    "data_cadastro" "date" DEFAULT "now"() NOT NULL,
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
    "data_cadastro" time(4) with time zone DEFAULT "now"() NOT NULL,
    "rg" character varying(9)
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
-- TOC entry 3271 (class 0 OID 0)
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
-- TOC entry 3272 (class 0 OID 0)
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
    "data_cadastro" timestamp(4) with time zone DEFAULT "now"() NOT NULL
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
-- TOC entry 3273 (class 0 OID 0)
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
-- TOC entry 3274 (class 0 OID 0)
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
    "fk_pedido_id" integer,
    "fk_casco_id" integer NOT NULL,
    "valor_unitario" numeric(6,4),
    "data_cadastro" "date" DEFAULT "now"() NOT NULL,
    "fk_insumo_id" integer,
    "situacao" "text" DEFAULT 'CADASTRADA'::"text" NOT NULL,
    CONSTRAINT "cc_remanufatura_situacao" CHECK ((("situacao" = 'CADASTRADA'::"text") OR ("situacao" = 'REALIZADA'::"text") OR ("situacao" = 'ENCERRADA'::"text")))
);


ALTER TABLE "soad"."remanufatura" OWNER TO "postgres";

--
-- TOC entry 3275 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN "remanufatura"."situacao"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON COLUMN "soad"."remanufatura"."situacao" IS 'CADASTRADA ou REALIZADA';


--
-- TOC entry 3276 (class 0 OID 0)
-- Dependencies: 220
-- Name: CONSTRAINT "cc_remanufatura_situacao" ON "remanufatura"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "cc_remanufatura_situacao" ON "soad"."remanufatura" IS 'CADASTRADA :: Não foi feita a remanufatura
REALIZADA :: Foi feita a remanufatura
ENCERRADA :: Foi feita e teve saida em um pedido';


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
-- TOC entry 3277 (class 0 OID 0)
-- Dependencies: 219
-- Name: remanufatura_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."remanufatura_id_seq" OWNED BY "soad"."remanufatura"."id_remanufatura";


--
-- TOC entry 237 (class 1259 OID 41779)
-- Name: requisicao; Type: TABLE; Schema: soad; Owner: postgres
--

CREATE TABLE "soad"."requisicao" (
    "metodo" "text" NOT NULL,
    "params_json" "json" NOT NULL,
    "id_requisicao" integer NOT NULL,
    "retorno" "text",
    "data_requisicao" "date" DEFAULT "now"() NOT NULL,
    "usuario" "text" DEFAULT CURRENT_USER NOT NULL,
    "mensagem" "text"
);


ALTER TABLE "soad"."requisicao" OWNER TO "postgres";

--
-- TOC entry 238 (class 1259 OID 41785)
-- Name: requisicoes_id_requisicao_seq; Type: SEQUENCE; Schema: soad; Owner: postgres
--

CREATE SEQUENCE "soad"."requisicoes_id_requisicao_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "soad"."requisicoes_id_requisicao_seq" OWNER TO "postgres";

--
-- TOC entry 3278 (class 0 OID 0)
-- Dependencies: 238
-- Name: requisicoes_id_requisicao_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."requisicoes_id_requisicao_seq" OWNED BY "soad"."requisicao"."id_requisicao";


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
-- TOC entry 3279 (class 0 OID 0)
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
-- TOC entry 3280 (class 0 OID 0)
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
-- TOC entry 3281 (class 0 OID 0)
-- Dependencies: 211
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: soad; Owner: postgres
--

ALTER SEQUENCE "soad"."usuario_id_seq" OWNED BY "soad"."usuario"."id_usuario";


--
-- TOC entry 240 (class 1259 OID 50117)
-- Name: vw_casco; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_casco" AS
 SELECT "mercadoria"."id_mercadoria",
    "mercadoria"."descricao",
    "mercadoria"."marca",
    "mercadoria"."ativo",
    "casco"."id_casco",
    "casco"."fk_insumo_id",
    "casco"."quantidade_insumo"
   FROM ("soad"."mercadoria"
     JOIN "soad"."casco" ON (("mercadoria"."id_mercadoria" = "casco"."fk_mercadoria_id")));


ALTER TABLE "soad"."vw_casco" OWNER TO "postgres";

--
-- TOC entry 235 (class 1259 OID 17203)
-- Name: vw_dicionario_dados; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_dicionario_dados" AS
 SELECT "columns"."table_name",
    "columns"."column_name",
    "columns"."is_nullable",
    "columns"."data_type"
   FROM "information_schema"."columns"
  WHERE (("columns"."table_schema")::"text" = 'soad'::"text");


ALTER TABLE "soad"."vw_dicionario_dados" OWNER TO "postgres";

--
-- TOC entry 250 (class 1259 OID 90931)
-- Name: vw_municipio; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_municipio" AS
 SELECT "municipio"."id_municipio",
    "municipio"."nome" AS "municipio",
    "estado"."id_estado",
    "estado"."nome" AS "estado",
    "estado"."sigla" AS "sigla_uf",
    "pais"."id_pais",
    "pais"."nome" AS "pais"
   FROM (("soad"."municipio"
     JOIN "soad"."estado" ON (("municipio"."fk_estado_id" = "estado"."id_estado")))
     JOIN "soad"."pais" ON (("estado"."fk_pais_id" = "pais"."id_pais")));


ALTER TABLE "soad"."vw_municipio" OWNER TO "postgres";

--
-- TOC entry 252 (class 1259 OID 90941)
-- Name: vw_endereco; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_endereco" AS
 SELECT "endereco"."id_endereco",
    "endereco"."fk_pessoa_id" AS "id_pessoa",
    "endereco"."logradouro",
    "endereco"."numero",
    "endereco"."bairro",
    "endereco"."cep",
    "endereco"."complemento",
    "endereco"."tipo",
    "vw_municipio"."id_municipio",
    "vw_municipio"."municipio",
    "vw_municipio"."id_estado",
    "vw_municipio"."estado",
    "vw_municipio"."sigla_uf",
    "vw_municipio"."id_pais",
    "vw_municipio"."pais"
   FROM ("soad"."endereco"
     LEFT JOIN "soad"."vw_municipio" ON (("vw_municipio"."id_municipio" = "endereco"."fk_municipio_id")));


ALTER TABLE "soad"."vw_endereco" OWNER TO "postgres";

--
-- TOC entry 251 (class 1259 OID 90935)
-- Name: vw_estado; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_estado" AS
 SELECT "estado"."id_estado",
    "estado"."nome" AS "estado",
    "estado"."sigla" AS "sigla_uf",
    "pais"."id_pais",
    "pais"."nome" AS "pais"
   FROM ("soad"."estado"
     JOIN "soad"."pais" ON (("estado"."fk_pais_id" = "pais"."id_pais")));


ALTER TABLE "soad"."vw_estado" OWNER TO "postgres";

--
-- TOC entry 243 (class 1259 OID 50255)
-- Name: vw_insumo; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_insumo" AS
 SELECT "mercadoria"."id_mercadoria",
    "mercadoria"."descricao",
    "mercadoria"."marca",
    "mercadoria"."ativo",
    "insumo"."id_insumo",
    "insumo"."quantidade_embalagem",
    "insumo"."fk_unidade_medida_id"
   FROM ("soad"."mercadoria"
     JOIN "soad"."insumo" ON (("mercadoria"."id_mercadoria" = "insumo"."fk_mercadoria_id")));


ALTER TABLE "soad"."vw_insumo" OWNER TO "postgres";

--
-- TOC entry 239 (class 1259 OID 50108)
-- Name: vw_mercadoria; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_mercadoria" AS
 SELECT "mercadoria"."id_mercadoria",
    "mercadoria"."descricao",
    "mercadoria"."marca",
    "mercadoria"."ativo",
        CASE
            WHEN ("casco"."fk_mercadoria_id" IS NOT NULL) THEN 'Casco'::"text"
            WHEN ("insumo"."fk_mercadoria_id" IS NOT NULL) THEN 'Insumo'::"text"
            ELSE 'Mercadoria'::"text"
        END AS "tipo_mercadoria",
    "mercadoria"."data_cadastro",
    "mercadoria"."permite_venda",
    "mercadoria"."valor_venda"
   FROM (("soad"."mercadoria"
     LEFT JOIN "soad"."casco" ON (("mercadoria"."id_mercadoria" = "casco"."fk_mercadoria_id")))
     LEFT JOIN "soad"."insumo" ON (("mercadoria"."id_mercadoria" = "insumo"."fk_mercadoria_id")));


ALTER TABLE "soad"."vw_mercadoria" OWNER TO "postgres";

--
-- TOC entry 236 (class 1259 OID 25426)
-- Name: vw_pessoa; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_pessoa" AS
SELECT
    NULL::integer AS "id_pessoa",
    NULL::character varying(100) AS "nome",
    NULL::character varying(100) AS "email",
    NULL::character varying(20) AS "telefone",
    NULL::"text" AS "documento",
    NULL::character varying(20) AS "inscricao_estadual",
    NULL::character varying(150) AS "fantasia",
    NULL::"text" AS "modalidade";


ALTER TABLE "soad"."vw_pessoa" OWNER TO "postgres";

--
-- TOC entry 241 (class 1259 OID 50168)
-- Name: vw_item_pedido; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_item_pedido" AS
 SELECT "pedido"."id_pedido",
    "pedido"."data_entrega",
    "pedido"."tipo_pedido",
    "pedido"."data_cadastro",
    "pedido"."observacao",
    "pedido"."situacao",
    "item_pedido"."id_item_pedido",
    "vw_mercadoria"."id_mercadoria",
    "vw_mercadoria"."descricao",
    "vw_mercadoria"."marca",
    "item_pedido"."quantidade",
    "item_pedido"."valor_unitario",
    "unidade_medida"."id_unidade_medida",
    "unidade_medida"."abreviacao" AS "unidade_medida",
    "vw_pessoa"."id_pessoa",
    "vw_pessoa"."nome",
    "vw_pessoa"."documento",
    "vw_pessoa"."fantasia" AS "nome_fantasia"
   FROM (((("soad"."pedido"
     JOIN "soad"."item_pedido" ON (("pedido"."id_pedido" = "item_pedido"."fk_pedido_id")))
     JOIN "soad"."vw_pessoa" ON (("pedido"."fk_pessoa_id" = "vw_pessoa"."id_pessoa")))
     JOIN "soad"."vw_mercadoria" ON (("item_pedido"."fk_mercadoria_id" = "vw_mercadoria"."id_mercadoria")))
     JOIN "soad"."unidade_medida" ON (("item_pedido"."fk_unidade_medida_id" = "unidade_medida"."id_unidade_medida")))
  ORDER BY "pedido"."data_cadastro" DESC;


ALTER TABLE "soad"."vw_item_pedido" OWNER TO "postgres";

--
-- TOC entry 242 (class 1259 OID 50243)
-- Name: vw_pedido; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_pedido" AS
 SELECT "pedido"."id_pedido",
    "pedido"."data_entrega",
    "pedido"."tipo_pedido",
    "pedido"."data_cadastro",
    "pedido"."observacao",
    "pedido"."situacao",
    "vw_pessoa"."id_pessoa",
    "vw_pessoa"."nome" AS "pessoa",
    "vw_pessoa"."email",
    "vw_pessoa"."telefone",
    "vw_pessoa"."documento",
    "vw_pessoa"."inscricao_estadual",
    "vw_pessoa"."fantasia"
   FROM ("soad"."pedido"
     JOIN "soad"."vw_pessoa" ON (("pedido"."fk_pessoa_id" = "vw_pessoa"."id_pessoa")))
  ORDER BY "pedido"."data_cadastro" DESC;


ALTER TABLE "soad"."vw_pedido" OWNER TO "postgres";

--
-- TOC entry 247 (class 1259 OID 58178)
-- Name: vw_item_lote; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_item_lote" AS
 SELECT "lote"."id_lote",
    "lote"."data_cadastro",
    "lote"."valor_unitario",
    "lote"."vazio",
    "lote"."observacao",
    "item_lote"."quantidade_item",
    "item_lote"."data_retirada",
    "item_lote"."data_validade",
    "item_lote"."id_item_lote",
    "item_lote"."lote_fabricante",
    "item_lote"."motivo_retirada",
    "item_lote"."aberto",
    "vw_mercadoria"."id_mercadoria",
    "vw_mercadoria"."descricao",
    "vw_mercadoria"."marca",
    "vw_mercadoria"."tipo_mercadoria",
    "unidade_medida"."id_unidade_medida",
    "unidade_medida"."abreviacao" AS "unidade_medida",
    "pedido_entrada"."id_pedido" AS "id_pedido_entrada",
    "pedido_entrada"."data_entrega" AS "data_entrega_pedido_entrada",
    "pedido_entrada"."data_cadastro" AS "data_pedido_entrada",
    "pedido_entrada"."observacao" AS "observacao_pedido_entrada",
    "pedido_entrada"."situacao" AS "situacao_pedido_entrada",
    "pedido_entrada"."pessoa" AS "nome_pessoa_entrada",
    "pedido_entrada"."documento" AS "documento_pessoa_entrada",
    "pedido_saida"."id_pedido" AS "id_pedido_saida",
    "pedido_saida"."data_entrega" AS "data_entrega_pedido_saida",
    "pedido_saida"."data_cadastro" AS "data_pedido_saida",
    "pedido_saida"."observacao" AS "observacao_pedido_saida",
    "pedido_saida"."situacao" AS "situacao_pedido_saida"
   FROM ((((("soad"."lote"
     JOIN "soad"."item_lote" ON (("lote"."id_lote" = "item_lote"."fk_lote_id")))
     JOIN "soad"."vw_mercadoria" ON (("lote"."fk_mercadoria_id" = "vw_mercadoria"."id_mercadoria")))
     JOIN "soad"."unidade_medida" ON (("lote"."fk_unidade_medida_id" = "unidade_medida"."id_unidade_medida")))
     JOIN "soad"."vw_pedido" "pedido_entrada" ON (("lote"."fk_pedido_id" = "pedido_entrada"."id_pedido")))
     LEFT JOIN "soad"."vw_item_pedido" "pedido_saida" ON (("item_lote"."fk_item_pedido_saida_id" = "pedido_saida"."id_item_pedido")))
  ORDER BY "lote"."data_cadastro" DESC;


ALTER TABLE "soad"."vw_item_lote" OWNER TO "postgres";

--
-- TOC entry 253 (class 1259 OID 99159)
-- Name: vw_pedido_compra; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_pedido_compra" AS
 SELECT "vw_pedido"."id_pedido",
    "vw_pedido"."data_entrega",
    "vw_pedido"."tipo_pedido",
    "vw_pedido"."data_cadastro",
    "vw_pedido"."observacao",
    "vw_pedido"."situacao",
    "vw_pedido"."id_pessoa",
    "vw_pedido"."pessoa",
    "vw_pedido"."email",
    "vw_pedido"."telefone",
    "vw_pedido"."documento",
    "vw_pedido"."inscricao_estadual",
    "vw_pedido"."fantasia"
   FROM "soad"."vw_pedido"
  WHERE (("vw_pedido"."tipo_pedido")::"text" = 'COMPRA'::"text")
  ORDER BY "vw_pedido"."id_pedido" DESC;


ALTER TABLE "soad"."vw_pedido_compra" OWNER TO "postgres";

--
-- TOC entry 254 (class 1259 OID 99163)
-- Name: vw_pedido_venda; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_pedido_venda" AS
 SELECT "vw_pedido"."id_pedido",
    "vw_pedido"."data_entrega",
    "vw_pedido"."tipo_pedido",
    "vw_pedido"."data_cadastro",
    "vw_pedido"."observacao",
    "vw_pedido"."situacao",
    "vw_pedido"."id_pessoa",
    "vw_pedido"."pessoa",
    "vw_pedido"."email",
    "vw_pedido"."telefone",
    "vw_pedido"."documento",
    "vw_pedido"."inscricao_estadual",
    "vw_pedido"."fantasia"
   FROM "soad"."vw_pedido"
  WHERE (("vw_pedido"."tipo_pedido")::"text" = 'VENDA'::"text")
  ORDER BY "vw_pedido"."id_pedido" DESC;


ALTER TABLE "soad"."vw_pedido_venda" OWNER TO "postgres";

--
-- TOC entry 246 (class 1259 OID 58163)
-- Name: vw_remanufatura; Type: VIEW; Schema: soad; Owner: postgres
--

CREATE VIEW "soad"."vw_remanufatura" AS
 SELECT "vw_pedido"."id_pedido",
    "vw_pedido"."data_entrega",
    "vw_pedido"."tipo_pedido",
    "vw_pedido"."data_cadastro",
    "vw_pedido"."observacao",
    "vw_pedido"."situacao" AS "situacao_pedido",
    "vw_pedido"."id_pessoa",
    "vw_pedido"."pessoa",
    "vw_pedido"."documento",
    "remanufatura"."id_remanufatura",
    "remanufatura"."valor_unitario",
    "vw_casco"."id_casco",
    "vw_casco"."descricao" AS "casco",
    "vw_insumo"."id_insumo",
    "vw_insumo"."descricao" AS "insumo",
    "remanufatura"."situacao" AS "situacao_remanufatura",
    "item_rem"."fk_item_lote_id" AS "id_item_lote"
   FROM (((("soad"."remanufatura"
     JOIN "soad"."vw_pedido" ON (("vw_pedido"."id_pedido" = "remanufatura"."fk_pedido_id")))
     JOIN "soad"."vw_casco" ON (("vw_casco"."id_casco" = "remanufatura"."fk_casco_id")))
     JOIN "soad"."vw_insumo" ON (("vw_insumo"."id_insumo" = "remanufatura"."fk_insumo_id")))
     LEFT JOIN "soad"."item_lote_remanufatura" "item_rem" ON (("item_rem"."fk_remanufatura_id" = "remanufatura"."id_remanufatura")))
  ORDER BY "vw_pedido"."data_cadastro";


ALTER TABLE "soad"."vw_remanufatura" OWNER TO "postgres";

--
-- TOC entry 3282 (class 0 OID 0)
-- Dependencies: 246
-- Name: VIEW "vw_remanufatura"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON VIEW "soad"."vw_remanufatura" IS 'relacao pedido e remanufatura';


--
-- TOC entry 2951 (class 2604 OID 58235)
-- Name: auditoria id_auditoria; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."auditoria" ALTER COLUMN "id_auditoria" SET DEFAULT "nextval"('"soad"."auditoria_id_auditoria_seq"'::"regclass");


--
-- TOC entry 2920 (class 2604 OID 16919)
-- Name: casco id_casco; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco" ALTER COLUMN "id_casco" SET DEFAULT "nextval"('"soad"."toner_id_seq"'::"regclass");


--
-- TOC entry 2941 (class 2604 OID 17001)
-- Name: endereco id_endereco; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco" ALTER COLUMN "id_endereco" SET DEFAULT "nextval"('"soad"."endereco_id_seq"'::"regclass");


--
-- TOC entry 2944 (class 2604 OID 17017)
-- Name: estado id_estado; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado" ALTER COLUMN "id_estado" SET DEFAULT "nextval"('"soad"."estado_id_seq"'::"regclass");


--
-- TOC entry 2921 (class 2604 OID 16927)
-- Name: insumo id_insumo; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo" ALTER COLUMN "id_insumo" SET DEFAULT "nextval"('"soad"."insumo_id_seq"'::"regclass");


--
-- TOC entry 2934 (class 2604 OID 16985)
-- Name: item_lote id_item_lote; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote" ALTER COLUMN "id_item_lote" SET DEFAULT "nextval"('"soad"."item_lote_id_seq"'::"regclass");


--
-- TOC entry 2949 (class 2604 OID 50282)
-- Name: item_lote_remanufatura id_item_lote_remanufatura; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote_remanufatura" ALTER COLUMN "id_item_lote_remanufatura" SET DEFAULT "nextval"('"soad"."item_lote_remanufatura_id_remanufatura_item_lote_seq"'::"regclass");


--
-- TOC entry 2933 (class 2604 OID 16977)
-- Name: item_pedido id_item_pedido; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido" ALTER COLUMN "id_item_pedido" SET DEFAULT "nextval"('"soad"."item_pedido_id_seq"'::"regclass");


--
-- TOC entry 2938 (class 2604 OID 16993)
-- Name: lote id_lote; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote" ALTER COLUMN "id_lote" SET DEFAULT "nextval"('"soad"."lote_id_seq"'::"regclass");


--
-- TOC entry 2916 (class 2604 OID 16909)
-- Name: mercadoria id_mercadoria; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."mercadoria" ALTER COLUMN "id_mercadoria" SET DEFAULT "nextval"('"soad"."produto_id_seq"'::"regclass");


--
-- TOC entry 2911 (class 2604 OID 16883)
-- Name: modalidade id_modalidade; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade" ALTER COLUMN "id_modalidade" SET DEFAULT "nextval"('"soad"."modalidade_id_seq"'::"regclass");


--
-- TOC entry 2923 (class 2604 OID 16943)
-- Name: modalidade_pessoa id_modalidade_pessoa; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa" ALTER COLUMN "id_modalidade_pessoa" SET DEFAULT "nextval"('"soad"."modalidade_pessoa_id_seq"'::"regclass");


--
-- TOC entry 2943 (class 2604 OID 17009)
-- Name: municipio id_municipio; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."municipio" ALTER COLUMN "id_municipio" SET DEFAULT "nextval"('"soad"."municipio_id_seq"'::"regclass");


--
-- TOC entry 2945 (class 2604 OID 17025)
-- Name: pais id_pais; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais" ALTER COLUMN "id_pais" SET DEFAULT "nextval"('"soad"."pais_id_seq"'::"regclass");


--
-- TOC entry 2925 (class 2604 OID 16961)
-- Name: pedido id_pedido; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido" ALTER COLUMN "id_pedido" SET DEFAULT "nextval"('"soad"."pedido_id_seq"'::"regclass");


--
-- TOC entry 2914 (class 2604 OID 16901)
-- Name: pessoa id_pessoa; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa" ALTER COLUMN "id_pessoa" SET DEFAULT "nextval"('"soad"."pessoa_id_seq"'::"regclass");


--
-- TOC entry 2909 (class 2604 OID 16873)
-- Name: pessoa_fisica id_pessoa_fisica; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica" ALTER COLUMN "id_pessoa_fisica" SET DEFAULT "nextval"('"soad"."pessoa_fisica_id_seq"'::"regclass");


--
-- TOC entry 2912 (class 2604 OID 16891)
-- Name: pessoa_juridica id_pessoa_juridica; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica" ALTER COLUMN "id_pessoa_juridica" SET DEFAULT "nextval"('"soad"."pessoa_juridica_id_seq"'::"regclass");


--
-- TOC entry 2929 (class 2604 OID 16969)
-- Name: remanufatura id_remanufatura; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura" ALTER COLUMN "id_remanufatura" SET DEFAULT "nextval"('"soad"."remanufatura_id_seq"'::"regclass");


--
-- TOC entry 2946 (class 2604 OID 41787)
-- Name: requisicao id_requisicao; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."requisicao" ALTER COLUMN "id_requisicao" SET DEFAULT "nextval"('"soad"."requisicoes_id_requisicao_seq"'::"regclass");


--
-- TOC entry 2924 (class 2604 OID 16951)
-- Name: unidade_medida id_unidade_medida; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida" ALTER COLUMN "id_unidade_medida" SET DEFAULT "nextval"('"soad"."unidade_medida_id_seq"'::"regclass");


--
-- TOC entry 2922 (class 2604 OID 16935)
-- Name: usuario id_usuario; Type: DEFAULT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario" ALTER COLUMN "id_usuario" SET DEFAULT "nextval"('"soad"."usuario_id_seq"'::"regclass");


--
-- TOC entry 3032 (class 2606 OID 58240)
-- Name: auditoria auditoria_pkey; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."auditoria"
    ADD CONSTRAINT "auditoria_pkey" PRIMARY KEY ("id_auditoria");


--
-- TOC entry 3009 (class 2606 OID 17003)
-- Name: endereco pkc_id_endereco; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "pkc_id_endereco" PRIMARY KEY ("id_endereco");


--
-- TOC entry 3017 (class 2606 OID 17019)
-- Name: estado pkc_id_estado; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "pkc_id_estado" PRIMARY KEY ("id_estado");


--
-- TOC entry 2981 (class 2606 OID 16929)
-- Name: insumo pkc_id_insumo; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "pkc_id_insumo" PRIMARY KEY ("id_insumo");


--
-- TOC entry 3003 (class 2606 OID 16987)
-- Name: item_lote pkc_id_item_lote; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "pkc_id_item_lote" PRIMARY KEY ("id_item_lote");


--
-- TOC entry 2999 (class 2606 OID 16979)
-- Name: item_pedido pkc_id_item_pedido; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "pkc_id_item_pedido" PRIMARY KEY ("id_item_pedido");


--
-- TOC entry 3007 (class 2606 OID 16995)
-- Name: lote pkc_id_lote; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "pkc_id_lote" PRIMARY KEY ("id_lote");


--
-- TOC entry 2975 (class 2606 OID 16911)
-- Name: mercadoria pkc_id_mercadoria; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."mercadoria"
    ADD CONSTRAINT "pkc_id_mercadoria" PRIMARY KEY ("id_mercadoria");


--
-- TOC entry 2961 (class 2606 OID 16885)
-- Name: modalidade pkc_id_modalidade; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade"
    ADD CONSTRAINT "pkc_id_modalidade" PRIMARY KEY ("id_modalidade");


--
-- TOC entry 2985 (class 2606 OID 16945)
-- Name: modalidade_pessoa pkc_id_modalidade_pessoa; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "pkc_id_modalidade_pessoa" PRIMARY KEY ("id_modalidade_pessoa");


--
-- TOC entry 3011 (class 2606 OID 17011)
-- Name: municipio pkc_id_municipio; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."municipio"
    ADD CONSTRAINT "pkc_id_municipio" PRIMARY KEY ("id_municipio");


--
-- TOC entry 3021 (class 2606 OID 17027)
-- Name: pais pkc_id_pais; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais"
    ADD CONSTRAINT "pkc_id_pais" PRIMARY KEY ("id_pais");


--
-- TOC entry 2993 (class 2606 OID 16963)
-- Name: pedido pkc_id_pedido; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido"
    ADD CONSTRAINT "pkc_id_pedido" PRIMARY KEY ("id_pedido");


--
-- TOC entry 2973 (class 2606 OID 16903)
-- Name: pessoa pkc_id_pessoa; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa"
    ADD CONSTRAINT "pkc_id_pessoa" PRIMARY KEY ("id_pessoa");


--
-- TOC entry 2953 (class 2606 OID 16875)
-- Name: pessoa_fisica pkc_id_pessoa_fisica; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "pkc_id_pessoa_fisica" PRIMARY KEY ("id_pessoa_fisica");


--
-- TOC entry 2965 (class 2606 OID 16893)
-- Name: pessoa_juridica pkc_id_pessoa_juridica; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "pkc_id_pessoa_juridica" PRIMARY KEY ("id_pessoa_juridica");


--
-- TOC entry 2996 (class 2606 OID 16971)
-- Name: remanufatura pkc_id_remanufatura; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "pkc_id_remanufatura" PRIMARY KEY ("id_remanufatura");


--
-- TOC entry 3028 (class 2606 OID 50284)
-- Name: item_lote_remanufatura pkc_id_remanufatura_item_lote; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote_remanufatura"
    ADD CONSTRAINT "pkc_id_remanufatura_item_lote" PRIMARY KEY ("id_item_lote_remanufatura");


--
-- TOC entry 3025 (class 2606 OID 41795)
-- Name: requisicao pkc_id_requisicao; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."requisicao"
    ADD CONSTRAINT "pkc_id_requisicao" PRIMARY KEY ("id_requisicao");


--
-- TOC entry 2979 (class 2606 OID 16921)
-- Name: casco pkc_id_toner; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "pkc_id_toner" PRIMARY KEY ("id_casco");


--
-- TOC entry 2989 (class 2606 OID 16953)
-- Name: unidade_medida pkc_id_unidade_medida; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida"
    ADD CONSTRAINT "pkc_id_unidade_medida" PRIMARY KEY ("id_unidade_medida");


--
-- TOC entry 2983 (class 2606 OID 16937)
-- Name: usuario pkc_id_usuario; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario"
    ADD CONSTRAINT "pkc_id_usuario" PRIMARY KEY ("id_usuario");


--
-- TOC entry 3019 (class 2606 OID 17557)
-- Name: estado ukc_estado_sigla_fk_pais_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "ukc_estado_sigla_fk_pais_id" UNIQUE ("sigla") INCLUDE ("fk_pais_id");


--
-- TOC entry 3283 (class 0 OID 0)
-- Dependencies: 3019
-- Name: CONSTRAINT "ukc_estado_sigla_fk_pais_id" ON "estado"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "ukc_estado_sigla_fk_pais_id" ON "soad"."estado" IS 'Cada estado deve ser unico no pais';


--
-- TOC entry 2977 (class 2606 OID 25432)
-- Name: mercadoria ukc_mercadoria_descricao; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."mercadoria"
    ADD CONSTRAINT "ukc_mercadoria_descricao" UNIQUE ("descricao");


--
-- TOC entry 2963 (class 2606 OID 17571)
-- Name: modalidade ukc_modalidade_descricao; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade"
    ADD CONSTRAINT "ukc_modalidade_descricao" UNIQUE ("descricao");


--
-- TOC entry 2987 (class 2606 OID 90950)
-- Name: modalidade_pessoa ukc_modalidade_id_pessoa_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "ukc_modalidade_id_pessoa_id" UNIQUE ("fk_pessoa_id", "fk_modalidade_id");


--
-- TOC entry 3013 (class 2606 OID 50005)
-- Name: municipio ukc_municipio_cod_ibge; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."municipio"
    ADD CONSTRAINT "ukc_municipio_cod_ibge" UNIQUE ("cod_ibge");


--
-- TOC entry 3015 (class 2606 OID 17566)
-- Name: municipio ukc_municipio_nome_fk_estado_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."municipio"
    ADD CONSTRAINT "ukc_municipio_nome_fk_estado_id" UNIQUE ("nome", "fk_estado_id");


--
-- TOC entry 3284 (class 0 OID 0)
-- Dependencies: 3015
-- Name: CONSTRAINT "ukc_municipio_nome_fk_estado_id" ON "municipio"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "ukc_municipio_nome_fk_estado_id" ON "soad"."municipio" IS 'Cada cidade deve ser única no estado';


--
-- TOC entry 3023 (class 2606 OID 17553)
-- Name: pais ukc_pais_sigla; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pais"
    ADD CONSTRAINT "ukc_pais_sigla" UNIQUE ("sigla");


--
-- TOC entry 2955 (class 2606 OID 90966)
-- Name: pessoa_fisica ukc_pessoa_fisica_cpf; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "ukc_pessoa_fisica_cpf" UNIQUE ("cpf");


--
-- TOC entry 2957 (class 2606 OID 90961)
-- Name: pessoa_fisica ukc_pessoa_fisica_cpf_fk_pessoa_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "ukc_pessoa_fisica_cpf_fk_pessoa_id" UNIQUE ("fk_pessoa_id", "cpf");


--
-- TOC entry 2959 (class 2606 OID 17581)
-- Name: pessoa_fisica ukc_pessoa_fisica_fk_pessoa_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "ukc_pessoa_fisica_fk_pessoa_id" UNIQUE ("fk_pessoa_id");


--
-- TOC entry 2967 (class 2606 OID 17579)
-- Name: pessoa_juridica ukc_pessoa_juridica_cnpj; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "ukc_pessoa_juridica_cnpj" UNIQUE ("cnpj");


--
-- TOC entry 3285 (class 0 OID 0)
-- Dependencies: 2967
-- Name: CONSTRAINT "ukc_pessoa_juridica_cnpj" ON "pessoa_juridica"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "ukc_pessoa_juridica_cnpj" ON "soad"."pessoa_juridica" IS 'cnpj deve ser unico';


--
-- TOC entry 2969 (class 2606 OID 90959)
-- Name: pessoa_juridica ukc_pessoa_juridica_cnpj_fk_pessoa_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "ukc_pessoa_juridica_cnpj_fk_pessoa_id" UNIQUE ("fk_pessoa_id", "cnpj");


--
-- TOC entry 2971 (class 2606 OID 17583)
-- Name: pessoa_juridica ukc_pessoa_juridica_fk_pessoa_id; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "ukc_pessoa_juridica_fk_pessoa_id" UNIQUE ("fk_pessoa_id");


--
-- TOC entry 3030 (class 2606 OID 50297)
-- Name: item_lote_remanufatura ukc_remanufatura_item_lote; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote_remanufatura"
    ADD CONSTRAINT "ukc_remanufatura_item_lote" UNIQUE ("fk_remanufatura_id", "fk_item_lote_id");


--
-- TOC entry 2991 (class 2606 OID 17569)
-- Name: unidade_medida ukc_unidade_medida_abreviacao; Type: CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."unidade_medida"
    ADD CONSTRAINT "ukc_unidade_medida_abreviacao" UNIQUE ("abreviacao");


--
-- TOC entry 3000 (class 1259 OID 50012)
-- Name: fki_fkc_item_lote_item_pedido_entrada_id; Type: INDEX; Schema: soad; Owner: postgres
--

CREATE INDEX "fki_fkc_item_lote_item_pedido_entrada_id" ON "soad"."item_lote" USING "btree" ("fk_item_pedido_entrada_id");


--
-- TOC entry 3001 (class 1259 OID 49988)
-- Name: fki_fkc_item_lote_item_pedido_id; Type: INDEX; Schema: soad; Owner: postgres
--

CREATE INDEX "fki_fkc_item_lote_item_pedido_id" ON "soad"."item_lote" USING "btree" ("fk_item_pedido_saida_id");


--
-- TOC entry 2997 (class 1259 OID 58298)
-- Name: fki_fkc_item_pedido_unidade_medida_id; Type: INDEX; Schema: soad; Owner: postgres
--

CREATE INDEX "fki_fkc_item_pedido_unidade_medida_id" ON "soad"."item_pedido" USING "btree" ("fk_unidade_medida_id");


--
-- TOC entry 3004 (class 1259 OID 58292)
-- Name: fki_fkc_lote_unidade_medida_id; Type: INDEX; Schema: soad; Owner: postgres
--

CREATE INDEX "fki_fkc_lote_unidade_medida_id" ON "soad"."lote" USING "btree" ("fk_unidade_medida_id");


--
-- TOC entry 3005 (class 1259 OID 49994)
-- Name: fki_fkc_mercadoria_id; Type: INDEX; Schema: soad; Owner: postgres
--

CREATE INDEX "fki_fkc_mercadoria_id" ON "soad"."lote" USING "btree" ("fk_mercadoria_id");


--
-- TOC entry 2994 (class 1259 OID 58223)
-- Name: fki_fkc_remanufatura_insumo_id; Type: INDEX; Schema: soad; Owner: postgres
--

CREATE INDEX "fki_fkc_remanufatura_insumo_id" ON "soad"."remanufatura" USING "btree" ("fk_insumo_id");


--
-- TOC entry 3026 (class 1259 OID 50295)
-- Name: fki_fkc_remanufatura_item_lote_item_lote_id; Type: INDEX; Schema: soad; Owner: postgres
--

CREATE INDEX "fki_fkc_remanufatura_item_lote_item_lote_id" ON "soad"."item_lote_remanufatura" USING "btree" ("fk_item_lote_id");


--
-- TOC entry 3207 (class 2618 OID 25429)
-- Name: vw_pessoa _RETURN; Type: RULE; Schema: soad; Owner: postgres
--

CREATE OR REPLACE VIEW "soad"."vw_pessoa" AS
 SELECT "pessoa"."id_pessoa",
    "pessoa"."nome",
    "pessoa"."email",
    "pessoa"."telefone",
        CASE
            WHEN ("pessoa_fisica"."cpf" IS NOT NULL) THEN ("pessoa_fisica"."cpf")::"text"
            WHEN ("pessoa_juridica"."cnpj" IS NOT NULL) THEN ("pessoa_juridica"."cnpj")::"text"
            ELSE NULL::"text"
        END AS "documento",
    "pessoa"."inscricao_estadual",
    "pessoa_juridica"."fantasia",
    "concat"('', ' ') AS "modalidade"
   FROM ((("soad"."pessoa"
     LEFT JOIN "soad"."pessoa_fisica" ON (("pessoa"."id_pessoa" = "pessoa_fisica"."fk_pessoa_id")))
     LEFT JOIN "soad"."pessoa_juridica" ON (("pessoa"."id_pessoa" = "pessoa_juridica"."fk_pessoa_id")))
     LEFT JOIN "soad"."modalidade_pessoa" ON (("pessoa"."id_pessoa" = "modalidade_pessoa"."fk_pessoa_id")))
  GROUP BY "pessoa"."id_pessoa",
        CASE
            WHEN ("pessoa_fisica"."cpf" IS NOT NULL) THEN ("pessoa_fisica"."cpf")::"text"
            WHEN ("pessoa_juridica"."cnpj" IS NOT NULL) THEN ("pessoa_juridica"."cnpj")::"text"
            ELSE NULL::"text"
        END, "pessoa_juridica"."fantasia";


--
-- TOC entry 3072 (class 2620 OID 58250)
-- Name: remanufatura trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."remanufatura" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3064 (class 2620 OID 58251)
-- Name: pessoa trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."pessoa" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3061 (class 2620 OID 58252)
-- Name: pessoa_fisica trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."pessoa_fisica" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3076 (class 2620 OID 58253)
-- Name: item_lote trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."item_lote" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3065 (class 2620 OID 58254)
-- Name: mercadoria trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."mercadoria" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3071 (class 2620 OID 58255)
-- Name: pedido trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."pedido" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3062 (class 2620 OID 58256)
-- Name: modalidade trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."modalidade" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3067 (class 2620 OID 58257)
-- Name: insumo trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."insumo" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3068 (class 2620 OID 58258)
-- Name: usuario trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."usuario" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3069 (class 2620 OID 58259)
-- Name: modalidade_pessoa trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."modalidade_pessoa" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3070 (class 2620 OID 58260)
-- Name: unidade_medida trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."unidade_medida" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3066 (class 2620 OID 58261)
-- Name: casco trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."casco" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3079 (class 2620 OID 58262)
-- Name: municipio trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."municipio" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3074 (class 2620 OID 58263)
-- Name: item_pedido trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."item_pedido" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3080 (class 2620 OID 58264)
-- Name: estado trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."estado" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3081 (class 2620 OID 58265)
-- Name: pais trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."pais" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3084 (class 2620 OID 58266)
-- Name: item_lote_remanufatura trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."item_lote_remanufatura" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3078 (class 2620 OID 58267)
-- Name: endereco trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."endereco" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3077 (class 2620 OID 58269)
-- Name: lote trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."lote" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3063 (class 2620 OID 58270)
-- Name: pessoa_juridica trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."pessoa_juridica" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3082 (class 2620 OID 58271)
-- Name: requisicao trg_auditoria; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_auditoria" AFTER INSERT OR DELETE OR UPDATE ON "soad"."requisicao" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_auditoria"();


--
-- TOC entry 3083 (class 2620 OID 50195)
-- Name: requisicao trg_chamada_metodo; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_chamada_metodo" AFTER INSERT OR UPDATE ON "soad"."requisicao" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_chamada_metodo"();

ALTER TABLE "soad"."requisicao" DISABLE TRIGGER "trg_chamada_metodo";


--
-- TOC entry 3073 (class 2620 OID 58189)
-- Name: item_pedido trg_pedido_mercadoria_unica; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_pedido_mercadoria_unica" BEFORE INSERT OR UPDATE ON "soad"."item_pedido" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_pedido_mercadoria_unica"();


--
-- TOC entry 3286 (class 0 OID 0)
-- Dependencies: 3073
-- Name: TRIGGER "trg_pedido_mercadoria_unica" ON "item_pedido"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON TRIGGER "trg_pedido_mercadoria_unica" ON "soad"."item_pedido" IS 'Não permite mercadorias duplicadas';


--
-- TOC entry 3075 (class 2620 OID 58192)
-- Name: item_lote trg_remover_lote_com_vinculo; Type: TRIGGER; Schema: soad; Owner: postgres
--

CREATE TRIGGER "trg_remover_lote_com_vinculo" AFTER DELETE ON "soad"."item_lote" FOR EACH ROW EXECUTE PROCEDURE "soad"."trg_remover_lote_com_vinculo"();


--
-- TOC entry 3287 (class 0 OID 0)
-- Dependencies: 3075
-- Name: TRIGGER "trg_remover_lote_com_vinculo" ON "item_lote"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON TRIGGER "trg_remover_lote_com_vinculo" ON "soad"."item_lote" IS 'Não permite remover item_lote com vinculo a pedido de saida';


--
-- TOC entry 3055 (class 2606 OID 17268)
-- Name: endereco fkc_endereco_municipio_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "fkc_endereco_municipio_id" FOREIGN KEY ("fk_municipio_id") REFERENCES "soad"."municipio"("id_municipio");


--
-- TOC entry 3056 (class 2606 OID 17277)
-- Name: endereco fkc_endereco_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."endereco"
    ADD CONSTRAINT "fkc_endereco_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa");


--
-- TOC entry 3058 (class 2606 OID 17357)
-- Name: estado fkc_estado_pais_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."estado"
    ADD CONSTRAINT "fkc_estado_pais_id" FOREIGN KEY ("fk_pais_id") REFERENCES "soad"."pais"("id_pais");


--
-- TOC entry 3038 (class 2606 OID 17377)
-- Name: insumo fkc_insumo_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "fkc_insumo_mercadoria_id" FOREIGN KEY ("fk_mercadoria_id") REFERENCES "soad"."mercadoria"("id_mercadoria") ON DELETE CASCADE;


--
-- TOC entry 3037 (class 2606 OID 17386)
-- Name: insumo fkc_insumo_unidade_medida_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."insumo"
    ADD CONSTRAINT "fkc_insumo_unidade_medida_id" FOREIGN KEY ("fk_unidade_medida_id") REFERENCES "soad"."unidade_medida"("id_unidade_medida");


--
-- TOC entry 3049 (class 2606 OID 50007)
-- Name: item_lote fkc_item_lote_item_pedido_entrada_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "fkc_item_lote_item_pedido_entrada_id" FOREIGN KEY ("fk_item_pedido_entrada_id") REFERENCES "soad"."item_pedido"("id_item_pedido");


--
-- TOC entry 3288 (class 0 OID 0)
-- Dependencies: 3049
-- Name: CONSTRAINT "fkc_item_lote_item_pedido_entrada_id" ON "item_lote"; Type: COMMENT; Schema: soad; Owner: postgres
--

COMMENT ON CONSTRAINT "fkc_item_lote_item_pedido_entrada_id" ON "soad"."item_lote" IS 'id do item_pedido que grou o item_lote';


--
-- TOC entry 3051 (class 2606 OID 58208)
-- Name: item_lote fkc_item_lote_item_pedido_saida_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "fkc_item_lote_item_pedido_saida_id" FOREIGN KEY ("fk_item_pedido_saida_id") REFERENCES "soad"."item_pedido"("id_item_pedido") DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3050 (class 2606 OID 17105)
-- Name: item_lote fkc_item_lote_lote_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote"
    ADD CONSTRAINT "fkc_item_lote_lote_id" FOREIGN KEY ("fk_lote_id") REFERENCES "soad"."lote"("id_lote");


--
-- TOC entry 3047 (class 2606 OID 17408)
-- Name: item_pedido fkc_item_pedido_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "fkc_item_pedido_mercadoria_id" FOREIGN KEY ("fk_mercadoria_id") REFERENCES "soad"."mercadoria"("id_mercadoria");


--
-- TOC entry 3046 (class 2606 OID 17399)
-- Name: item_pedido fkc_item_pedido_pedido_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "fkc_item_pedido_pedido_id" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 3048 (class 2606 OID 58293)
-- Name: item_pedido fkc_item_pedido_unidade_medida_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_pedido"
    ADD CONSTRAINT "fkc_item_pedido_unidade_medida_id" FOREIGN KEY ("fk_unidade_medida_id") REFERENCES "soad"."unidade_medida"("id_unidade_medida");


--
-- TOC entry 3053 (class 2606 OID 17417)
-- Name: lote fkc_lote_pedido_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "fkc_lote_pedido_id" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido");


--
-- TOC entry 3054 (class 2606 OID 58287)
-- Name: lote fkc_lote_unidade_medida_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "fkc_lote_unidade_medida_id" FOREIGN KEY ("fk_unidade_medida_id") REFERENCES "soad"."unidade_medida"("id_unidade_medida");


--
-- TOC entry 3052 (class 2606 OID 49989)
-- Name: lote fkc_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."lote"
    ADD CONSTRAINT "fkc_mercadoria_id" FOREIGN KEY ("fk_mercadoria_id") REFERENCES "soad"."mercadoria"("id_mercadoria");


--
-- TOC entry 3041 (class 2606 OID 17256)
-- Name: modalidade_pessoa fkc_modalidade_pessoa_modalidade_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "fkc_modalidade_pessoa_modalidade_id" FOREIGN KEY ("fk_modalidade_id") REFERENCES "soad"."modalidade"("id_modalidade") ON DELETE SET NULL;


--
-- TOC entry 3040 (class 2606 OID 17247)
-- Name: modalidade_pessoa fkc_modalidade_pessoa_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."modalidade_pessoa"
    ADD CONSTRAINT "fkc_modalidade_pessoa_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE SET NULL;


--
-- TOC entry 3057 (class 2606 OID 17291)
-- Name: municipio fkc_municipio_estado_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."municipio"
    ADD CONSTRAINT "fkc_municipio_estado_id" FOREIGN KEY ("fk_estado_id") REFERENCES "soad"."estado"("id_estado");


--
-- TOC entry 3042 (class 2606 OID 17450)
-- Name: pedido fkc_pedido_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pedido"
    ADD CONSTRAINT "fkc_pedido_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa");


--
-- TOC entry 3033 (class 2606 OID 17463)
-- Name: pessoa_fisica fkc_pessoa_fisica_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_fisica"
    ADD CONSTRAINT "fkc_pessoa_fisica_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3034 (class 2606 OID 17483)
-- Name: pessoa_juridica fkc_pessoa_juridica_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."pessoa_juridica"
    ADD CONSTRAINT "fkc_pessoa_juridica_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3044 (class 2606 OID 17514)
-- Name: remanufatura fkc_remanufatura_casco_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "fkc_remanufatura_casco_id" FOREIGN KEY ("fk_casco_id") REFERENCES "soad"."casco"("id_casco");


--
-- TOC entry 3045 (class 2606 OID 58218)
-- Name: remanufatura fkc_remanufatura_insumo_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "fkc_remanufatura_insumo_id" FOREIGN KEY ("fk_insumo_id") REFERENCES "soad"."insumo"("id_insumo");


--
-- TOC entry 3059 (class 2606 OID 50290)
-- Name: item_lote_remanufatura fkc_remanufatura_item_lote_item_lote_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote_remanufatura"
    ADD CONSTRAINT "fkc_remanufatura_item_lote_item_lote_id" FOREIGN KEY ("fk_item_lote_id") REFERENCES "soad"."item_lote"("id_item_lote");


--
-- TOC entry 3060 (class 2606 OID 50299)
-- Name: item_lote_remanufatura fkc_remanufatura_item_lote_remanufatura_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."item_lote_remanufatura"
    ADD CONSTRAINT "fkc_remanufatura_item_lote_remanufatura_id" FOREIGN KEY ("fk_remanufatura_id") REFERENCES "soad"."remanufatura"("id_remanufatura");


--
-- TOC entry 3043 (class 2606 OID 58213)
-- Name: remanufatura fkc_remanufatura_pedido_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."remanufatura"
    ADD CONSTRAINT "fkc_remanufatura_pedido_id" FOREIGN KEY ("fk_pedido_id") REFERENCES "soad"."pedido"("id_pedido") DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3036 (class 2606 OID 17304)
-- Name: casco fkc_toner_insumo_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "fkc_toner_insumo_id" FOREIGN KEY ("fk_insumo_id") REFERENCES "soad"."insumo"("id_insumo") ON DELETE CASCADE;


--
-- TOC entry 3035 (class 2606 OID 17313)
-- Name: casco fkc_toner_mercadoria_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."casco"
    ADD CONSTRAINT "fkc_toner_mercadoria_id" FOREIGN KEY ("fk_mercadoria_id") REFERENCES "soad"."mercadoria"("id_mercadoria") ON DELETE CASCADE;


--
-- TOC entry 3039 (class 2606 OID 17531)
-- Name: usuario fkc_usuario_pessoa_id; Type: FK CONSTRAINT; Schema: soad; Owner: postgres
--

ALTER TABLE ONLY "soad"."usuario"
    ADD CONSTRAINT "fkc_usuario_pessoa_id" FOREIGN KEY ("fk_pessoa_id") REFERENCES "soad"."pessoa"("id_pessoa") ON DELETE CASCADE;


-- Completed on 2019-09-07 18:28:03

--
-- PostgreSQL database dump complete
--

