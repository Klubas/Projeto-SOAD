DO
$do$
DECLARE
   _sql text;
BEGIN

   SELECT
          string_agg(format('DROP %s %s;'
                          , CASE WHEN proisagg THEN 'AGGREGATE' ELSE 'FUNCTION' END
                          , oid::regprocedure)
                   , E'\n')
   INTO _sql
   FROM   pg_proc
   WHERE  pronamespace = 'soad'::regnamespace  -- schema name here!
   AND (oid::regprocedure)::text  like 'soad.prc_%'
   or (oid::regprocedure)::text  like 'soad.fnc_%';

   IF _sql IS NOT NULL THEN
      RAISE NOTICE '%', _sql;  -- debug / check first
      EXECUTE _sql;         -- uncomment payload once you are sure
   ELSE
      RAISE NOTICE 'No fuctions found in schema %', quote_ident(_schema);
   END IF;
END
$do$  LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION soad.prc_cancelar_pedido(p_pedido_id integer)
    RETURNS integer
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_pedido_id integer := p_pedido_id;
	v_situacao_pedido text;
	v_remanufatura record;
	v_situacao text;
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

	BEGIN
		<<REMANUFATURA>>
		FOR v_remanufatura IN
			-- pega todas as remanufaturas do pedido v_id_pedido
			SELECT id_remanufatura, situacao FROM soad.remanufatura
			WHERE remanufatura.fk_pedido_id = v_pedido_id
			AND (remanufatura.situacao = 'CADASTRADA' OR remanufatura.situacao = 'ENCERRADA')
		LOOP
			RAISE NOTICE 'Remanufatura: (ID %)', v_remanufatura.id_remanufatura;
			BEGIN

				IF v_remanufatura.situacao = 'CADASTRADA' THEN
					v_situacao := 'CANCELADA';
				ELSIF v_remanufatura.situacao = 'ENCERRADA' THEN
					v_situacao := 'REALIZADA';
				END IF;

				UPDATE soad.remanufatura
				SET situacao=v_situacao
				WHERE id_remanufatura = v_remanufatura.id_remanufatura;

			END;

		END LOOP REMANUFATURA;

		BEGIN
			IF v_remanufatura IS NOT NULL THEN
			    PERFORM soad.prc_desvincular_remanufaturas_pedido(v_pedido_id);
			END IF;
		END;

	END;

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_cancelar_pedido(p_pedido_id integer) OWNER TO soadmin;

--
-- TOC entry 3509 (class 0 OID 0)
-- Dependencies: 286
-- Name: PROCEDURE prc_cancelar_pedido(p_pedido_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_cancelar_pedido(p_pedido_id integer) IS 'cancelamento de pedido, só pode cancelar se não tiver encerrado';


--
-- TOC entry 287 (class 1255 OID 17586)
-- Name: prc_configuracao_definicoes_iniciais(); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_configuracao_definicoes_iniciais()
    RETURNS integer
    LANGUAGE plpgsql
    AS $_$

BEGIN
	DO
		$do$
		BEGIN
		   IF NOT EXISTS (
			  SELECT
			  FROM   pg_catalog.pg_roles
			  WHERE  rolname = 'soadmin') THEN

			  CREATE ROLE soadmin LOGIN PASSWORD 'soad2019';
			  grant all privileges on database postgres to soadmin;
		   END IF;
	END $do$;


	-- Cadastra Unidade de medida
	RAISE NOTICE 'Cadastrando unidades de medida...';
	BEGIN
		PERFORM soad.prc_insert_or_update_unidade_medida('unidade', 'un');
		PERFORM soad.prc_insert_or_update_unidade_medida('KILOGRAMA', 'kg');
        PERFORM soad.prc_insert_or_update_unidade_medida('GRAMA', 'g');
		PERFORM soad.prc_insert_or_update_unidade_medida('LITRO', 'l');
		PERFORM soad.prc_insert_or_update_unidade_medida('MILILITRO', 'ml');

	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das unidades de medida.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;

	END;

	-- Cadastra Modalidades
	RAISE NOTICE 'Cadastrando modalidades';
	BEGIN
		PERFORM soad.prc_insert_modalidade('Cliente'); -- 1
		PERFORM soad.prc_insert_modalidade('Fornecedor'); -- 2

	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das modalidades.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;

	END;

	-- Cadastra paises
	RAISE NOTICE 'Cadastrando paises...';
	BEGIN
		PERFORM soad.prc_insert_municipio_estado_pais('', '', '', 'Brasil', 'BR');

	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro dos paises.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;

	END;

	-- Cadastra estados
	RAISE NOTICE 'Cadastrando estados...';
	BEGIN
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Acre', 'AC', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Alagoas', 'AL', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Amapá', 'AP', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Amazonas', 'AM', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Bahia', 'BA', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Ceará', 'CE', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('Brasília', 'Distrito Federal', 'DF', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Espírito Santo', 'ES', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Goiás', 'GO', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Maranhão', 'MA', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Mato Grosso', 'MT', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Mato Grosso do Sul', 'MS', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Minas Gerais', 'MG', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Pará', 'PA', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Paraíba', 'PB', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Paraná', 'PR', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Pernambuco', 'PE', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Piauí', 'PI', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('Rio de Janeiro', 'Rio de Janeiro', 'RJ', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Rio Grande do Norte', 'RN', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Rio Grande do Sul', 'RS', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Rondônia', 'RO', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Roraima', 'RR', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Santa Catarina', 'SC', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('São Paulo', 'São Paulo', 'SP', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Sergipe', 'SE', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Tocantins', 'TO', 'Brasil', 'BR');

	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro dos estados.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;

	END;

	-- Cadastra municipios
	RAISE NOTICE 'Cadastrando municipios...';
	BEGIN
		PERFORM soad.prc_insert_municipio_estado_pais('Ponta Grossa', 'Paraná', 'PR', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('Curitiba', 'Paraná', 'PR', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('Castro', 'Paraná', 'PR', 'Brasil', 'BR');

	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das municipios.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;

	END;

	-- Cadastra pessoa
	RAISE NOTICE 'Cadastrando pessoas...';
	BEGIN
		PERFORM soad.prc_insert_pessoa('VIP Cartuchos', '', '4232240660', '00000000000000', '', 'VIP Cartuchos');
		PERFORM soad.prc_insert_pessoa('EMPRESA TESTE 1', '', '4232240660', '99998899999999', '', 'EMPRESA TESTE 1');
		PERFORM soad.prc_insert_pessoa('Lucas Klüber', 'lucas.kluber@gmail.com', '42999823030', '10841793930', '', '');
		PERFORM soad.prc_insert_pessoa('PESSOA TESTE 1', '', '', '00000100000', '', '');

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
			PERFORM soad.prc_vincular_modalidade_pessoa(v_aux_id, '99999999999999');

			-- Clientes
			SELECT modalidade.id_modalidade INTO v_aux_id FROM soad.modalidade WHERE modalidade.descricao = 'CLIENTE';
			PERFORM soad.prc_vincular_modalidade_pessoa(v_aux_id, '00000000000');

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

			PERFORM soad.prc_insert_endereco(v_pessoa_id, v_municipio_id, 'Rua Comandante Paulo Pinheiro Schimdt', '354', 'Uvaranas', '84031029', '');

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

            PERFORM soad.prc_insert_produto('Produto 1', 'Marca 1', v_unidade_medida_id, 'PRODUTO');

            -- Insumo
            SELECT unidade_medida.id_unidade_medida INTO v_unidade_medida_id FROM soad.unidade_medida
			WHERE unidade_medida.abreviacao = 'ml';

            PERFORM soad.prc_insert_produto('Insumo 3', 'HP', '107', 'INSUMO', CAST(v_unidade_medida_id AS text), '276');

			-- Casco
			SELECT min(insumo.id_insumo) INTO v_insumo_id FROM soad.insumo;

            PERFORM soad.prc_insert_produto('Casco 1', 'HP', '276', 'CASCO', CAST(v_insumo_id AS text), '20');

		EXCEPTION WHEN OTHERS THEN
			RAISE NOTICE 'Não foi possível cadastrar os produtos.';
			RAISE NOTICE '% %', SQLERRM, SQLSTATE;

        END;
    END;

END;
$_$;


ALTER FUNCTION soad.prc_configuracao_definicoes_iniciais() OWNER TO soadmin;

--
-- TOC entry 3510 (class 0 OID 0)
-- Dependencies: 287
-- Name: PROCEDURE prc_configuracao_definicoes_iniciais(); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_configuracao_definicoes_iniciais() IS 'Algumas configurações iniciais para o uso do sistema';


--
-- TOC entry 288 (class 1255 OID 17588)
-- Name: prc_configuracao_gerador_trigger(); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_configuracao_gerador_trigger()
    RETURNS integer
    LANGUAGE plpgsql
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

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_configuracao_gerador_trigger() OWNER TO soadmin;

--
-- TOC entry 289 (class 1255 OID 17589)
-- Name: prc_delete_mercadoria(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_delete_mercadoria(p_mercadoria_id integer)
    RETURNS integer
    LANGUAGE plpgsql
    AS $$
BEGIN

-- delete insumo
	BEGIN
 		DELETE FROM soad.insumo
		WHERE fk_mercadoria_id = p_mercadoria_id;
	EXCEPTION WHEN OTHERS THEN
		RAISE EXCEPTION 'O Insumo possui vínculos e não pode ser excluido.';
	END;

-- delete casco
	BEGIN
		DELETE FROM soad.casco
		WHERE fk_mercadoria_id = p_mercadoria_id;
	EXCEPTION WHEN OTHERS THEN
		RAISE EXCEPTION 'O casco possui vínculos e não pode ser excluido.';
	END;

-- delete pessoa
	BEGIN
		DELETE FROM soad.mercadoria
		WHERE id_mercadoria = p_mercadoria_id;
	EXCEPTION WHEN OTHERS THEN
		RAISE EXCEPTION 'A mercadoria possui vínculos e não pode ser excluida.';
	END;



RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_delete_mercadoria(p_mercadoria_id integer) OWNER TO soadmin;

--
-- TOC entry 3511 (class 0 OID 0)
-- Dependencies: 289
-- Name: PROCEDURE prc_delete_mercadoria(p_mercadoria_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_delete_mercadoria(p_mercadoria_id integer) IS 'apaga a mercadoria';


--
-- TOC entry 290 (class 1255 OID 17590)
-- Name: prc_delete_pessoa(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_delete_pessoa(p_pessoa_id integer)
    RETURNS integer
    LANGUAGE plpgsql
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

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_delete_pessoa(p_pessoa_id integer) OWNER TO soadmin;

--
-- TOC entry 3512 (class 0 OID 0)
-- Dependencies: 290
-- Name: PROCEDURE prc_delete_pessoa(p_pessoa_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_delete_pessoa(p_pessoa_id integer) IS 'apaga a pessoa e seus vinculos';


--
-- TOC entry 291 (class 1255 OID 17591)
-- Name: prc_delete_remanufatura(json); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_delete_remanufatura(p_remanufatura_id json)
    RETURNS integer
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_json json := p_remanufatura_id;
	v_remanufatura_id integer;

BEGIN

	FOR v_remanufatura_id IN
		SELECT value::integer
		FROM json_array_elements_text(v_json)
	LOOP
		BEGIN
			DELETE FROM soad.remanufatura
			WHERE id_remanufatura = v_remanufatura_id
			AND situacao = 'CADASTRADA';
		EXCEPTION WHEN OTHERS THEN
			RAISE EXCEPTION 'Não foi possível remover a remanufatura (ID %).', v_remanufatura_id;
		END;

	END LOOP;



RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_delete_remanufatura(p_remanufatura_id json) OWNER TO soadmin;

--
-- TOC entry 292 (class 1255 OID 17592)
-- Name: prc_desvincular_remanufaturas_pedido(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_desvincular_remanufaturas_pedido(p_pedido_id integer)
    RETURNS integer
    LANGUAGE plpgsql
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

		ELSIF t_item.situacao = 'REALIZADA' OR t_item.situacao = 'CANCELADA' THEN

			UPDATE soad.remanufatura
			SET fk_pedido_id = NULL
				, valor_unitario = 0
			WHERE id_remanufatura = t_item.id_remanufatura;

		ELSIF t_item.situacao = 'ENCERRADA' THEN
			RAISE NOTICE 'Desvinculando remanufatura encerrada.';
			UPDATE soad.remanufatura
			SET fk_pedido_id = NULL
				, situacao = 'REALIZADA'
				, valor_unitario = 0
			WHERE id_remanufatura = t_item.id_remanufatura;

		ELSE
			RAISE EXCEPTION 'ALERTA: Remanufatura vinculada SITUACAO: %', t_item.situacao;

		END IF;
	END LOOP REMANUFATURA;



RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_desvincular_remanufaturas_pedido(p_pedido_id integer) OWNER TO soadmin;

--
-- TOC entry 293 (class 1255 OID 17593)
-- Name: prc_encerrar_pedido(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_encerrar_pedido(p_pedido_id integer)
    RETURNS integer
    LANGUAGE plpgsql
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
		PERFORM soad.prc_gerar_lote(v_pedido_id);
	ELSIF v_tipo_pedido = 'VENDA' THEN
		-- Vincular lotes existentes a um pedido de venda
		PERFORM soad.prc_movimentar_lote(v_pedido_id);
	ELSE
		RAISE EXCEPTION 'O lote desse pedido não pode ser alterado';
	END IF;

	-- todo: Registra Log
--EXCEPTION WHEN OTHERS THEN
	--RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_encerrar_pedido(p_pedido_id integer) OWNER TO soadmin;

--
-- TOC entry 3513 (class 0 OID 0)
-- Dependencies: 293
-- Name: PROCEDURE prc_encerrar_pedido(p_pedido_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_encerrar_pedido(p_pedido_id integer) IS 'Procedimento para encerrar pedido. Pedidos encerrados não podem ser alterados.';


--
-- TOC entry 294 (class 1255 OID 17594)
-- Name: prc_estornar_pedido(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_estornar_pedido(p_pedido_id integer)
    RETURNS integer
    LANGUAGE plpgsql
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
			PERFORM soad.prc_desvincular_remanufaturas_pedido(p_pedido_id=>v_pedido_id);

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
					PERFORM soad.prc_esvazia_lote(t_item.id_lote);
				END;

			END LOOP;

		ELSE
			RAISE EXCEPTION 'Esse tipo de pedido não pode ser estornado.';
		END IF;
	END;

	RAISE NOTICE 'Pedido estornado com sucesso.';
	-- todo: Registra log

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_estornar_pedido(p_pedido_id integer) OWNER TO soadmin;

--
-- TOC entry 3514 (class 0 OID 0)
-- Dependencies: 294
-- Name: PROCEDURE prc_estornar_pedido(p_pedido_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_estornar_pedido(p_pedido_id integer) IS 'Estorna o encerramento do pedido, desfazendo as movimentações';


--
-- TOC entry 295 (class 1255 OID 17596)
-- Name: prc_esvazia_lote(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_esvazia_lote(p_lote_id integer)
    RETURNS integer
    LANGUAGE plpgsql
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
	RETURN 0;
END;$$;


ALTER FUNCTION soad.prc_esvazia_lote(p_lote_id integer) OWNER TO soadmin;

--
-- TOC entry 3515 (class 0 OID 0)
-- Dependencies: 295
-- Name: PROCEDURE prc_esvazia_lote(p_lote_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_esvazia_lote(p_lote_id integer) IS 'verifica se lote pode ser esvaziado';


--
-- TOC entry 296 (class 1255 OID 17597)
-- Name: prc_esvaziar_item_lote(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_esvaziar_item_lote(p_item_lote_id integer)
    RETURNS integer
    LANGUAGE plpgsql
    AS $$DECLARE
	v_item_lote_id integer := p_item_lote_id;
	v_item_lote RECORD;

BEGIN

	SELECT id_item_lote, aberto, quantidade_item INTO v_item_lote
	FROM soad.item_lote
	WHERE id_item_lote = v_item_lote_id;

	IF v_item_lote IS NULL THEN
		RAISE EXCEPTION 'Item (%) não encontrado.', v_item_lote_id;
	END IF;

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

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_esvaziar_item_lote(p_item_lote_id integer) OWNER TO soadmin;

--
-- TOC entry 3516 (class 0 OID 0)
-- Dependencies: 296
-- Name: PROCEDURE prc_esvaziar_item_lote(p_item_lote_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_esvaziar_item_lote(p_item_lote_id integer) IS 'marca item_lote como vazio';


--
-- TOC entry 297 (class 1255 OID 17598)
-- Name: prc_gerar_lote(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_gerar_lote(p_id_pedido integer)
    RETURNS integer
    LANGUAGE plpgsql
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

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_gerar_lote(p_id_pedido integer) OWNER TO soadmin;

--
-- TOC entry 3517 (class 0 OID 0)
-- Dependencies: 297
-- Name: PROCEDURE prc_gerar_lote(p_id_pedido integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_gerar_lote(p_id_pedido integer) IS 'procedimento para gerar lote após a confirmação de um pedido';


--
-- TOC entry 298 (class 1255 OID 17599)
-- Name: prc_insert_modalidade(text); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_insert_modalidade(p_modalidade text)
    RETURNS integer
    LANGUAGE plpgsql
    AS $$DECLARE
	v_modalidade text := upper(p_modalidade);

BEGIN
	INSERT INTO soad.modalidade (descricao)
	VALUES (v_modalidade);
RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_insert_modalidade(p_modalidade text) OWNER TO soadmin;

--
-- TOC entry 3518 (class 0 OID 0)
-- Dependencies: 298
-- Name: PROCEDURE prc_insert_modalidade(p_modalidade text); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_insert_modalidade(p_modalidade text) IS 'Cadastrar modalidades de pessoas';


--
-- TOC entry 299 (class 1255 OID 17600)
-- Name: prc_insert_municipio_estado_pais(text, text, text, text, text, text); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_insert_municipio_estado_pais(p_municipio_nome text, p_cod_ibge text, p_estado_nome text, p_estado_sigla text, p_pais_nome text, p_pais_sigla text)
    RETURNS integer
    LANGUAGE plpgsql
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

	RETURN -1;

	-- Insere apenas estado
	ELSIF v_municipio_nome = '' AND v_estado_nome <> '' AND v_pais_nome <> '' THEN

		SELECT id_pais into v_aux FROM soad.pais WHERE pais.sigla = v_pais_sigla;

		INSERT INTO soad.estado (fk_pais_id, nome, sigla)
		VALUES (v_aux, v_estado_nome, v_estado_sigla);

	RETURN -1;

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

	RETURN -1;

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

	RETURN -1;

	-- Insere apenas nova municipio
	ELSIF (SELECT count(*) FROM soad.municipio WHERE municipio.nome = v_municipio_nome) = 0 THEN

		SELECT estado.id_estado into v_aux
		FROM soad.estado
		INNER JOIN soad.pais ON estado.fk_pais_id = pais.id_pais
		WHERE estado.sigla = v_estado_sigla;

		INSERT INTO soad.municipio (fk_estado_id, nome, cod_ibge)
		VALUES (v_aux, v_municipio_nome, v_cod_ibge);

	RETURN -1;

	END IF;

	RAISE NOTICE 'ERRO: Nenhuma informação foi registrada';



RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_insert_municipio_estado_pais(p_municipio_nome text, p_cod_ibge text, p_estado_nome text, p_estado_sigla text, p_pais_nome text, p_pais_sigla text) OWNER TO soadmin;

--
-- TOC entry 3519 (class 0 OID 0)
-- Dependencies: 299
-- Name: PROCEDURE prc_insert_municipio_estado_pais(p_municipio_nome text, p_cod_ibge text, p_estado_nome text, p_estado_sigla text, p_pais_nome text, p_pais_sigla text); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_insert_municipio_estado_pais(p_municipio_nome text, p_cod_ibge text, p_estado_nome text, p_estado_sigla text, p_pais_nome text, p_pais_sigla text) IS 'Procedimento para cadastro de municipio e estado e pais ou municipio ou estado ou pais';


--
-- TOC entry 300 (class 1255 OID 17601)
-- Name: prc_insert_or_update_unidade_medida(text, text); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_insert_or_update_unidade_medida(p_descricao text, p_abreviacao text)
    RETURNS integer
    LANGUAGE plpgsql
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
RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_insert_or_update_unidade_medida(p_descricao text, p_abreviacao text) OWNER TO soadmin;

--
-- TOC entry 3520 (class 0 OID 0)
-- Dependencies: 300
-- Name: PROCEDURE prc_insert_or_update_unidade_medida(p_descricao text, p_abreviacao text); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_insert_or_update_unidade_medida(p_descricao text, p_abreviacao text) IS 'Cadastra unidade de medida.
Se a abreviacao ja existir irá atualizar a descrição';


--
-- TOC entry 301 (class 1255 OID 17602)
-- Name: prc_movimentar_lote(integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_movimentar_lote(p_id_pedido integer)
    RETURNS integer
    LANGUAGE plpgsql
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
	v_aux RECORD;

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
					PERFORM soad.prc_esvazia_lote(v_lote_id);
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

				SELECT * INTO v_aux FROM soad.fnc_realizar_remanufatura(v_remanufatura.id_remanufatura);

				UPDATE soad.remanufatura
				SET situacao='ENCERRADA'
				WHERE id_remanufatura = v_remanufatura.id_remanufatura;

			END;

		END LOOP REMANUFATURA;
	END;

--EXCEPTION WHEN OTHERS THEN
	--RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_movimentar_lote(p_id_pedido integer) OWNER TO soadmin;

--
-- TOC entry 302 (class 1255 OID 17604)
-- Name: prc_vincular_modalidade_pessoa(integer, text); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_vincular_modalidade_pessoa(p_modalidade_id integer, p_documento text)
    RETURNS integer
    LANGUAGE plpgsql
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

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_vincular_modalidade_pessoa(p_modalidade_id integer, p_documento text) OWNER TO soadmin;

--
-- TOC entry 3521 (class 0 OID 0)
-- Dependencies: 302
-- Name: PROCEDURE prc_vincular_modalidade_pessoa(p_modalidade_id integer, p_documento text); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_vincular_modalidade_pessoa(p_modalidade_id integer, p_documento text) IS 'Vincula uma modalidade a uma pessoa';


--
-- TOC entry 303 (class 1255 OID 17605)
-- Name: prc_vincular_pedido_mercadoria(integer, integer, integer, real, real, integer); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_vincular_pedido_mercadoria(p_pedido_id integer, p_mercadoria_id integer, p_unidade_medida_id integer, p_quantidade real, p_valor_unitario real, p_item_pedido_id integer DEFAULT NULL::integer)
    RETURNS integer
    LANGUAGE plpgsql
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
	SELECT permite_venda, ativo, codigo, descricao INTO v_mercadoria
	FROM soad.mercadoria
	WHERE id_mercadoria = v_mercadoria_id;

	SELECT id_pedido, tipo_pedido INTO v_pedido
	FROM soad.pedido
	WHERE id_pedido = v_pedido_id;

	IF v_mercadoria.permite_venda = FALSE AND v_pedido.tipo_pedido = 'VENDA' THEN
		RAISE EXCEPTION 'A mercadoria % - % não permite venda.', v_mercadoria.codigo, v_mercadoria.descricao;
	ELSIF v_mercadoria.ativo = FALSE THEN
		RAISE EXCEPTION 'A mercadoria % - % não está ativa e não pode ser utilizada.', v_mercadoria.codigo, v_mercadoria.descricao;
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

RETURN 0;
END;
$$;


ALTER FUNCTION soad.prc_vincular_pedido_mercadoria(p_pedido_id integer, p_mercadoria_id integer, p_unidade_medida_id integer, p_quantidade real, p_valor_unitario real, p_item_pedido_id integer) OWNER TO soadmin;

--
-- TOC entry 3522 (class 0 OID 0)
-- Dependencies: 303
-- Name: PROCEDURE prc_vincular_pedido_mercadoria(p_pedido_id integer, p_mercadoria_id integer, p_unidade_medida_id integer, p_quantidade real, p_valor_unitario real, p_item_pedido_id integer); Type: COMMENT; Schema: soad; Owner: soadmin
--

COMMENT ON FUNCTION soad.prc_vincular_pedido_mercadoria(p_pedido_id integer, p_mercadoria_id integer, p_unidade_medida_id integer, p_quantidade real, p_valor_unitario real, p_item_pedido_id integer) IS 'vincula uma mercadoria a um pedido, não deve ser chamado diretamente, utilizar prc_cadastro_pedido';


--
-- TOC entry 304 (class 1255 OID 17606)
-- Name: prc_vincular_pedido_remanufatura(integer, integer, integer, real, real, boolean); Type: PROCEDURE; Schema: soad; Owner: soadmin
--

CREATE OR REPLACE FUNCTION soad.prc_vincular_pedido_remanufatura(p_pedido_id integer, p_casco_id integer, p_insumo_id integer, p_quantidade real, p_valor_unitario real, p_nova_remanufatura boolean)
    RETURNS integer
    LANGUAGE plpgsql
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
		RAISE EXCEPTION 'Para vincular uma remanufatura o pedido precisa estar na situação CADASTRADO.';
	END IF;

	IF v_pedido.tipo_pedido = 'COMPRA' THEN
		RAISE EXCEPTION 'Não é possível víncular uma remanufatura a um pedido do tipo COMPRA.';
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

RETURN 0;
END;
$$;

-- FUNCTIONS

ALTER FUNCTION soad.prc_vincular_pedido_remanufatura(p_pedido_id integer, p_casco_id integer, p_insumo_id integer, p_quantidade real, p_valor_unitario real, p_nova_remanufatura boolean) OWNER TO soadmin;

-- FUNCTION: soad.fnc_realizar_remanufatura(integer, boolean)

-- DROP FUNCTION soad.fnc_realizar_remanufatura(integer, boolean);

CREATE OR REPLACE FUNCTION soad.fnc_realizar_remanufatura(
	p_remanufatura_id integer,
	p_simular boolean DEFAULT false,
	OUT p_item_lote_id integer)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$DECLARE
	v_remanufatura_id 	integer = p_remanufatura_id;
	v_insumo_id			integer;
	v_insumo			RECORD;
	v_item_lote			RECORD;

BEGIN

	IF (SELECT id_remanufatura FROM soad.remanufatura WHERE remanufatura.id_remanufatura = v_remanufatura_id) IS NULL THEN
		RAISE EXCEPTION 'A remanufatura (%) não existe.', v_remanufatura_id;
	END IF;

	IF p_simular is False THEN
		IF (SELECT situacao FROM soad.remanufatura WHERE remanufatura.id_remanufatura = v_remanufatura_id) <> 'CADASTRADA' THEN
			RAISE EXCEPTION 'A remanufatura (%) já foi realizada.', v_remanufatura_id;
		END IF;
	END IF;

	SELECT fk_insumo_id INTO v_insumo_id
	FROM soad.remanufatura
	WHERE remanufatura.id_remanufatura = v_remanufatura_id;

	-- localiza lotes que podem ser utilizados
	WITH t_item_lote as (
		SELECT item_lote.id_item_lote, item_lote.aberto, item_lote.fk_lote_id as id_lote
		FROM soad.vw_insumo
			INNER JOIN soad.lote ON vw_insumo.id_mercadoria = lote.fk_mercadoria_id
			LEFT JOIN  soad.item_lote ON lote.id_lote = item_lote.fk_lote_id
		WHERE vw_insumo.id_insumo = v_insumo_id
			AND lote.vazio = false							-- lote não pode estar vazio
			AND item_lote.fk_item_pedido_saida_id IS null 	-- item que ainda não teve saída
			AND item_lote.quantidade_item > 0
		ORDER BY lote.data_cadastro ASC
	)

	-- localiza primeiro item_lote que pode ser utilizado
	SELECT id_item_lote, id_lote INTO v_item_lote
	  FROM t_item_lote
	  ORDER BY t_item_lote.aberto DESC
	LIMIT 1;

	IF v_item_lote.id_item_lote IS NULL THEN
		SELECT id_insumo, descricao INTO v_insumo FROM soad.vw_insumo
		WHERE id_insumo = v_insumo_id;
		RAISE EXCEPTION 'Não há estoque do insumo % - % disponível para remanufatura.', v_insumo_id, v_insumo.descricao;
	END IF;

	p_item_lote_id := v_item_lote.id_item_lote;
	RAISE NOTICE 'Item lote a ser movimentado para remanufatura: (%)', p_item_lote_id;

	IF p_simular is True THEN
		RETURN;
	END IF;

	-- movimenta lote
	BEGIN

		RAISE NOTICE 'Atualizando lote (Remanufatura)';

		BEGIN
			UPDATE soad.item_lote
			SET aberto=true
				, motivo_abertura='Remanufatura (operação interna)'
				, data_abertura=NOW()
			WHERE item_lote.id_item_lote = v_item_lote.id_item_lote;
		END;

		-- Atualiza lote se está vazio ou não
		BEGIN
			PERFORM soad.prc_esvazia_lote(v_item_lote.id_lote::integer);
		END;

		-- Atualiza remanufatura
		RAISE NOTICE 'Atualizando Remanufatura';

		BEGIN
			UPDATE soad.remanufatura
			SET situacao = 'REALIZADA'
				, codigo=LPAD(TO_CHAR(NOW()::DATE, 'yymmdd') || v_remanufatura_id, 15, '0')
			WHERE remanufatura.id_remanufatura = v_remanufatura_id;
		END;

		-- Criar relacionamento entre item_lote e remanufatura
		RAISE NOTICE 'Relacionando remanufatura e item';

		BEGIN
			INSERT INTO soad.item_lote_remanufatura(fk_remanufatura_id, fk_item_lote_id)
			VALUES(v_remanufatura_id, v_item_lote.id_item_lote);
		END;

		RAISE NOTICE 'Remanufatura % realizada.', v_remanufatura_id;
	END;

	RETURN;



END;
$BODY$;

ALTER FUNCTION soad.fnc_realizar_remanufatura(integer, boolean)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_relatorio_municipios(character varying, character varying, character varying)

-- DROP FUNCTION soad.fnc_relatorio_municipios(character varying, character varying, character varying);

CREATE OR REPLACE FUNCTION soad.fnc_relatorio_municipios(
	p_pais character varying,
	p_estado character varying,
	p_municipio character varying)
    RETURNS TABLE(municipio_id integer, municipio character varying, estado_id integer, estado character varying, pais_id integer, pais character varying)
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
    ROWS 1000
AS $BODY$begin
	return query select t_municipio.id_municipio, t_municipio.municipio, t_municipio.id_estado, t_municipio.estado, t_municipio.id_pais, t_municipio.pais
					from soad.vw_municipio as t_municipio
						where 1=1
						and t_municipio.municipio like p_municipio
						and t_municipio.estado like p_estado
						and t_municipio.pais   like p_pais;
end;
$BODY$;

ALTER FUNCTION soad.fnc_relatorio_municipios(character varying, character varying, character varying)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_insert_update_pessoa(text, text, text, text, text, text, text)

-- DROP FUNCTION soad.fnc_insert_update_pessoa(text, text, text, text, text, text, text);

CREATE OR REPLACE FUNCTION soad.fnc_insert_update_pessoa(
	p_nome text,
	p_email text,
	p_telefone text,
	p_documento text,
	p_inscricao_estadual text DEFAULT 'ISENTO'::text,
	p_fantasia text DEFAULT NULL::text,
	p_pessoa_id text DEFAULT NULL::text,
	OUT pessoa_id integer)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
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


END;
$BODY$;

ALTER FUNCTION soad.fnc_insert_update_pessoa(text, text, text, text, text, text, text)
    OWNER TO soadmin;
-- FUNCTION: soad.fnc_insert_update_mercadoria(text, text, text, boolean, boolean, numeric, text, numeric, integer, integer, integer, boolean)

-- DROP FUNCTION soad.fnc_insert_update_mercadoria(text, text, text, boolean, boolean, numeric, text, numeric, integer, integer, integer, boolean);

CREATE OR REPLACE FUNCTION soad.fnc_insert_update_mercadoria(
	p_codigo text,
	p_descricao text,
	p_marca text,
	p_ativo boolean DEFAULT true,
	p_permite_venda boolean DEFAULT NULL::boolean,
	p_valor_venda numeric DEFAULT (
	0)::numeric,
	p_tipo text DEFAULT 'PRODUTO'::text,
	p_quantidade numeric DEFAULT (
	0)::numeric,
	p_insumo_id integer DEFAULT NULL::integer,
	p_unidade_medida_id integer DEFAULT NULL::integer,
	p_mercadoria_id integer DEFAULT NULL::integer,
	p_colorido boolean DEFAULT false,
	OUT mercadoria_id integer)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
DECLARE
	v_mercadoria_id integer				:= p_mercadoria_id;
	-- mercadoria
	v_codigo text						:= upper(p_codigo);
	v_descricao text 					:= upper(p_descricao);
	v_marca text 						:= upper(p_marca);
	v_ativo boolean						:= p_ativo;
	v_permite_venda boolean				:= p_permite_venda;
	v_valor_venda	numeric				:= p_valor_venda;
	v_tipo text 						:= upper(p_tipo);

	v_quantidade numeric				:= p_quantidade;
	v_insumo_id integer					:= p_insumo_id;
	v_unidade_medida_id integer 		:= p_unidade_medida_id;
	v_colorido boolean					:= p_colorido;

	v_acao text := 'INSERT';

BEGIN

	IF v_mercadoria_id IS NOT NULL THEN
		v_acao := 'UPDATE';
	END IF;

	IF v_permite_venda IS NULL THEN
		IF 	  v_tipo = 'MERCADORIA'	THEN v_permite_venda := True;
		ELSIF v_tipo 'CASCO' 		THEN v_permite_venda := False;
		ELSIF v_tipo 'INSUMO' 		THEN v_permite_venda := False;
		END IF;
	END IF;

	-- Inserir produto/mercadoria
	IF v_acao = 'INSERT' THEN

		WITH t_mercadoria AS (
			INSERT INTO soad.mercadoria (descricao, marca, ativo, permite_venda, valor_venda, codigo)
			VALUES (v_descricao, v_marca, v_ativo, v_permite_venda, v_valor_venda, v_codigo)
			RETURNING id_mercadoria
		)

		SELECT id_mercadoria
		INTO v_mercadoria_id
		FROM t_mercadoria;

	ELSIF v_acao = 'UPDATE' THEN

		UPDATE soad.mercadoria
		SET descricao=v_descricao
			, marca=v_marca
			, ativo=v_ativo
			, permite_venda=v_permite_venda
			, valor_venda=v_valor_venda
			, codigo=v_codigo
		WHERE id_mercadoria = v_mercadoria_id;

	END IF;

	-- Variável de retorno
	mercadoria_id := v_mercadoria_id;

	-- Inserir insumo
	IF v_tipo = 'INSUMO' THEN

        IF v_quantidade IS NULL
			OR v_unidade_medida_id IS NULL
		THEN
			RAISE EXCEPTION 'Valores não podem ser nulos qtd=% unidade=%', v_quantidade, v_unidade_medida;
		END IF;

		IF v_acao = 'INSERT' THEN

			INSERT INTO soad.insumo (fk_mercadoria_id, quantidade_embalagem, fk_unidade_medida_id, colorido)
			VALUES (v_mercadoria_id, v_quantidade, v_unidade_medida_id, v_colorido);

		ELSIF v_acao = 'UPDATE' THEN

			UPDATE soad.insumo
			SET quantidade_embalagem=v_quantidade
				, fk_unidade_medida_id=v_unidade_medida_id
				, colorido=v_colorido
			WHERE fk_mercadoria_id=v_mercadoria_id;

		END IF;

	-- Inserir casco
	ELSIF v_tipo = 'CASCO' THEN
		IF v_unidade_medida_id IS NULL
			OR v_insumo_id IS NULL
			OR v_quantidade IS NULL
		THEN
			RAISE EXCEPTION 'Valores não podem ser nulos unidade=% insumo=% quantidade=%', v_unidade_medida_id, v_insumo_id, v_quantidade;
		END IF;

		IF v_acao = 'INSERT' THEN

			INSERT INTO soad.casco (fk_mercadoria_id, fk_insumo_id, quantidade_insumo, fk_unidade_medida_insumo)
			VALUES (v_mercadoria_id, v_insumo_id, v_quantidade, v_unidade_medida_id);

		ELSIF v_acao = 'UPDATE' THEN

			UPDATE soad.casco
			SET fk_insumo_id=v_insumo_id
				, quantidade_insumo=v_quantidade
				, fk_unidade_medida_insumo=v_unidade_medida_id
			WHERE fk_mercadoria_id = v_mercadoria_id;

		END IF;

	ELSIF v_tipo = 'MERCADORIA' THEN RETURN;
	ELSE RAISE EXCEPTION 'Tipo de mercadoria inválida: %', v_tipo;
	END IF;

	RETURN;



END;
$BODY$;

ALTER FUNCTION soad.fnc_insert_update_mercadoria(text, text, text, boolean, boolean, numeric, text, numeric, integer, integer, integer, boolean)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_insert_update_endereco(integer, integer, text, text, text, text, text, text, integer)

-- DROP FUNCTION soad.fnc_insert_update_endereco(integer, integer, text, text, text, text, text, text, integer);

CREATE OR REPLACE FUNCTION soad.fnc_insert_update_endereco(
	p_pessoa_id integer,
	p_municipio_id integer,
	p_logradouro text,
	p_numero text,
	p_bairro text,
	p_cep text,
	p_complemento text,
	p_tipo text,
	p_endereco_id integer DEFAULT NULL::integer,
	OUT endereco_id integer)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
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



END;
$BODY$;

ALTER FUNCTION soad.fnc_insert_update_endereco(integer, integer, text, text, text, text, text, text, integer)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_insert_pedido(text, integer, text, date, integer)

-- DROP FUNCTION soad.fnc_insert_pedido(text, integer, text, date, integer);

CREATE OR REPLACE FUNCTION soad.fnc_insert_pedido(
	p_tipo_pedido text,
	p_pessoa_id integer,
	p_observacao text,
	p_data_entrega date,
	p_pedido_id integer DEFAULT NULL::integer)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
DECLARE
	-- Pedido
	v_pedido_id		integer	:= p_pedido_id; -- Vai receber o id do pedido gravado

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
	IF v_pedido_id IS NULL THEN
		BEGIN
			WITH t_pedido as (
				INSERT INTO soad.pedido (fk_pessoa_id, tipo_pedido, situacao, data_cadastro, observacao)
				VALUES (v_pessoa_id, v_tipo_pedido ,'CADASTRADO', v_data_cadastro, v_observacao)
				RETURNING id_pedido
			)
				SELECT id_pedido INTO v_pedido_id
				FROM t_pedido;

			RETURN v_pedido_id;
		END;


	-- Edita pedido
	ELSE
		BEGIN
			WITH t_pedido as (
				UPDATE soad.pedido
				SET fk_pessoa_id=v_pessoa_id
					, observacao=v_observacao
				WHERE id_pedido = v_pedido_id
				RETURNING id_pedido
			)
				SELECT id_pedido INTO v_pedido_id
				FROM t_pedido;

			RETURN v_pedido_id;
		END;
	END IF;



END;
$BODY$;

ALTER FUNCTION soad.fnc_insert_pedido(text, integer, text, date, integer)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_get_pessoa(integer)

-- DROP FUNCTION soad.fnc_get_pessoa(integer);

CREATE OR REPLACE FUNCTION soad.fnc_get_pessoa(
	p_pessoa_id integer,
	OUT json_pessoa json)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$DECLARE
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
$BODY$;

ALTER FUNCTION soad.fnc_get_pessoa(integer)
    OWNER TO soadmin;

COMMENT ON FUNCTION soad.fnc_get_pessoa(integer)
    IS 'traz informações da pessoa, endereços e modalidades';

-- FUNCTION: soad.fnc_get_pedido(integer)

-- DROP FUNCTION soad.fnc_get_pedido(integer);

CREATE OR REPLACE FUNCTION soad.fnc_get_pedido(
	p_pedido_id integer,
	OUT json_pedido json)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
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
			, quantidade_remanufatura as quantidade
			, valor_unitario
			, casco_id
			, casco
			, insumo_id
			, insumo
			, 'REMANUFATURA' as tipo
		FROM soad.vw_remanufatura_pedido
		WHERE id_pedido = v_pedido_id
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
$BODY$;

ALTER FUNCTION soad.fnc_get_pedido(integer)
    OWNER TO soadmin;

COMMENT ON FUNCTION soad.fnc_get_pedido(integer)
    IS 'retorna json com pedido e os itens';

-- FUNCTION: soad.fnc_get_mercadoria(integer)

-- DROP FUNCTION soad.fnc_get_mercadoria(integer);

CREATE OR REPLACE FUNCTION soad.fnc_get_mercadoria(
	p_mercadoria_id integer,
	OUT json_mercadoria json)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$DECLARE

	v_mercadoria_id integer = p_mercadoria_id;

	v_tipo text;
	v_mercadoria RECORD;

BEGIN

	-- Identifica tipo
	SELECT UPPER(tipo_mercadoria) INTO v_tipo
	FROM soad.vw_mercadoria
	WHERE id_mercadoria = v_mercadoria_id;

	IF v_tipo = 'MERCADORIA' THEN
		SELECT id_mercadoria
		, descricao
		, marca
		, ativo
		, tipo_mercadoria AS tipo
		, permite_venda
		, valor_venda
		, codigo
		, data_cadastro
	FROM soad.vw_mercadoria
	INTO v_mercadoria
	WHERE id_mercadoria = v_mercadoria_id;

	ELSIF v_tipo = 'INSUMO' THEN

		SELECT id_mercadoria
			, descricao
			, marca
			, ativo
			, v_tipo as tipo
			, permite_venda
			, id_insumo
			, quantidade_embalagem
			, id_unidade_medida as unidade_medida_id
			, codigo
			, valor_venda
			, colorido
			, data_cadastro
		FROM soad.vw_insumo
		INTO v_mercadoria
		WHERE id_mercadoria = v_mercadoria_id;

	ELSIF v_tipo = 'CASCO' THEN

		SELECT id_mercadoria
			, descricao
			, marca
			, ativo
			, v_tipo as tipo
			, permite_venda
			, id_casco
			, id_insumo as insumo_id
			, quantidade_insumo
			, codigo
			, valor_venda
			, id_unidade_medida as unidade_medida_id
			, data_cadastro
		FROM soad.vw_casco
		INTO v_mercadoria
		WHERE id_mercadoria = v_mercadoria_id;

	END IF;

	json_mercadoria := row_to_json(v_mercadoria);

	RETURN;

END;
$BODY$;

ALTER FUNCTION soad.fnc_get_mercadoria(integer)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_get_item_lote_remanufatura(integer)

-- DROP FUNCTION soad.fnc_get_item_lote_remanufatura(integer);

CREATE OR REPLACE FUNCTION soad.fnc_get_item_lote_remanufatura(
	p_remanufatura_id integer,
	OUT p_item_lote_id json)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
DECLARE
	v_remanufatura_id integer := p_remanufatura_id;
	v_item_lote_id integer;

BEGIN

	SELECT vr.id_item_lote
	INTO v_item_lote_id
	FROM soad.vw_remanufatura vr
	WHERE vr.id_remanufatura = v_remanufatura_id;

	p_item_lote_id = v_item_lote_id;

	RETURN;

END;
$BODY$;

ALTER FUNCTION soad.fnc_get_item_lote_remanufatura(integer)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_gerar_remanufatura(integer, integer, integer, boolean)

-- DROP FUNCTION soad.fnc_gerar_remanufatura(integer, integer, integer, boolean);

CREATE OR REPLACE FUNCTION soad.fnc_gerar_remanufatura(
	p_casco_id integer,
	p_insumo_id integer,
	p_quantidade integer,
	p_realizar boolean DEFAULT true,
	OUT remanufaturas_ids integer[])
    RETURNS integer[]
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$DECLARE
	v_casco_id		 	integer		:= p_casco_id;
	v_insumo_id		 	integer		:= p_insumo_id;
	v_quantidade 	 	integer		:= p_quantidade;
	v_remanufatura_id	integer;
	v_id_item_lote 		integer;
	v_realizar			boolean		:= p_realizar;

BEGIN

	remanufaturas_ids := NULL;

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
		IF v_realizar IS TRUE THEN
			BEGIN
				SELECT * FROM soad.fnc_realizar_remanufatura(v_remanufatura_id);
			END;
		END IF;

		remanufaturas_ids = remanufaturas_ids || v_remanufatura_id;

	END LOOP;

	RETURN;



END;
$BODY$;

ALTER FUNCTION soad.fnc_gerar_remanufatura(integer, integer, integer, boolean)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_chamada_de_metodo(json)

-- DROP FUNCTION soad.fnc_chamada_de_metodo(json);

CREATE OR REPLACE FUNCTION soad.fnc_chamada_de_metodo(
	p_json_params json DEFAULT NULL::json,
	OUT p_retorno integer,
	OUT p_retorno_json json)
    RETURNS record
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
DECLARE

	v_metodo		text 	:= p_json_params::json->'metodo';
	v_json_params	json	:= p_json_params::json->'params';
	v_json 			json	:= p_json_params;

	v_id_requisicao integer	:= NULL;
	v_params_temp	text	:= NULL;
	v_params		text	:= NULL;
	v_retorno		integer := NULL;
	v_retorno_record record;
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

	--EXCEPTION WHEN OTHERS THEN
		--RAISE EXCEPTION 'Método/Parâmetros não podem ser nulos. % %', SQLERRM, SQLSTATE;
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

					sql_query := 'SELECT * FROM ' || sql_query;

					EXECUTE sql_query;

					v_retorno := 100;

				ELSIF v_tipo = 'fnc' THEN

					sql_query := 'SELECT * FROM ' || sql_query;

					BEGIN
						EXECUTE sql_query INTO v_retorno_record;

						p_retorno_json := to_json(v_retorno_record);

						BEGIN
							v_retorno := v_retorno_record::integer;
							EXCEPTION WHEN OTHERS THEN
								RAISE NOTICE 'ERRO';
						END;

					END;

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

	EXCEPTION WHEN OTHERS THEN
	RAISE EXCEPTION '% %', SQLERRM, SQLSTATE;

END;
$BODY$;

ALTER FUNCTION soad.fnc_chamada_de_metodo(json)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_cadastro_pessoa(text, text, text, text, text, text, text, json, json)

-- DROP FUNCTION soad.fnc_cadastro_pessoa(text, text, text, text, text, text, text, json, json);

CREATE OR REPLACE FUNCTION soad.fnc_cadastro_pessoa(
	p_nome text,
	p_documento text,
	p_email text DEFAULT NULL::text,
	p_telefone text DEFAULT NULL::text,
	p_inscricao_estadual text DEFAULT 'ISENTO'::text,
	p_fantasia text DEFAULT NULL::text,
	p_pessoa_id text DEFAULT NULL::text,
	p_endereco json DEFAULT NULL::json,
	p_modalidade json DEFAULT NULL::json,
	OUT pessoa_id integer)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
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
				PERFORM soad.prc_vincular_modalidade_pessoa(
					v_modalidade_id::integer
					, v_documento::text
				);
			END;

		END LOOP;

		EXCEPTION WHEN no_data_found THEN
			RAISE NOTICE 'Sem modalidades.';
	END;

	RETURN;




END;
$BODY$;

ALTER FUNCTION soad.fnc_cadastro_pessoa(text, text, text, text, text, text, text, json, json)
    OWNER TO soadmin;

-- FUNCTION: soad.fnc_cadastro_pedido(text, integer, text, date, json, integer)

-- DROP FUNCTION soad.fnc_cadastro_pedido(text, integer, text, date, json, integer);

CREATE OR REPLACE FUNCTION soad.fnc_cadastro_pedido(
	p_tipo_pedido text,
	p_pessoa_id integer,
	p_observacao text DEFAULT NULL::text,
	p_data_entrega date DEFAULT NULL::date,
	p_itens json DEFAULT NULL::json,
	p_pedido_id integer DEFAULT NULL::integer,
	OUT pedido_id integer)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
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

		IF v_tipo_pedido = 'VENDA' THEN
			PERFORM soad.prc_desvincular_remanufaturas_pedido(p_pedido_id=>v_pedido_id);
		END IF;

		-- Remove os itens do pedido
		RAISE NOTICE 'Removendo item %', v_item_pedido_id;
		DELETE FROM soad.item_pedido
		WHERE item_pedido.fk_pedido_id = v_pedido_id;

	END IF;

	-- Cadastra/edita pedido
	BEGIN
		v_pedido_id := soad.fnc_insert_pedido(v_tipo_pedido, v_pessoa_id, v_observacao, v_data_entrega, v_pedido_id);
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

					PERFORM soad.prc_vincular_pedido_remanufatura(v_pedido_id, v_casco_id, v_insumo_id, v_quantidade, v_valor_unitario, v_nova_remanufatura);

				END;

			ELSIF v_tipo_item = 'MERCADORIA' THEN
				v_mercadoria_id  	:= v_json_temp::json->'mercadoria_id';
				v_unidade_medida_id	:= v_json_temp::json->'unidade_medida_id';
				v_item_pedido_id	:= v_json_temp::json->'item_pedido_id';

				v_item_pedido_id := (
					CASE
						WHEN v_item_pedido_id > 0 THEN v_item_pedido_id::integer
						ELSE NULL
					END
				);


				BEGIN

					PERFORM soad.prc_vincular_pedido_mercadoria(v_pedido_id, v_mercadoria_id, v_unidade_medida_id, v_quantidade, v_valor_unitario);
					--PERFORM soad.prc_vincular_pedido_mercadoria(v_pedido_id, v_mercadoria_id, v_unidade_medida_id, v_quantidade, v_valor_unitario, v_item_pedido_id);

				END;

			ELSE
				RAISE EXCEPTION 'Tipo de item (%) inválido.', v_tipo_item;

			END IF;

		END LOOP;
	END;

	pedido_id := v_pedido_id;
	RETURN;

END;
$BODY$;

ALTER FUNCTION soad.fnc_cadastro_pedido(text, integer, text, date, json, integer)
    OWNER TO soadmin;

COMMENT ON FUNCTION soad.fnc_cadastro_pedido(text, integer, text, date, json, integer)
    IS 'Cadastra e atualiza informações do pedido';

-- FUNCTION: soad.fnc_buscar_registro(text, text, text, text, text)

-- DROP FUNCTION soad.fnc_buscar_registro(text, text, text, text, text);

CREATE OR REPLACE FUNCTION soad.fnc_buscar_registro(
	p_tabela text,
	p_coluna text DEFAULT ''::text,
	p_valor text DEFAULT ''::text,
	p_operador text DEFAULT '='::text,
	p_filtro text DEFAULT NULL::text)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
DECLARE
	v_schema text := 'soad';
	v_tabela text := p_tabela;
	v_coluna text := p_coluna;
	v_valor text := upper(p_valor);
	v_operador text := p_operador;
	v_filtro text = p_filtro;

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
		SELECT c.column_name::text
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
	sql_query := 'SELECT ' || v_colunas || ' FROM ' || v_schema || '.' || v_tabela || ' WHERE 1=1';

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
		sql_query := sql_query || ' AND ' || v_coluna  || ' ' || v_operador || ' ' || v_valor || '::' || v_tipo;

	END IF;

	-- Se tiver filtro extra vai adicionar aqui
	IF v_filtro IS NOT NULL THEN

		sql_query := sql_query || ' AND ' || v_filtro;

	END IF;

	sql_query := sql_query || ';';

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

END;
$BODY$;

ALTER FUNCTION soad.fnc_buscar_registro(text, text, text, text, text)
    OWNER TO soadmin;
