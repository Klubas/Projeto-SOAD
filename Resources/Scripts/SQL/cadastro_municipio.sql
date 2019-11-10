-- FUNCTION: soad.prc_insert_municipio_estado_pais(text, text, text, text, text, text)

 DROP FUNCTION soad.prc_insert_municipio_estado_pais(text, text, text, text, text, text);

CREATE OR REPLACE FUNCTION soad.prc_insert_municipio_estado_pais(
	p_municipio_nome text,
	p_estado_nome text,
	p_estado_sigla text,
	p_pais_nome text,
	p_pais_sigla text,
	p_cod_ibge text DEFAULT NULL::text)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$DECLARE
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
		RAISE EXCEPTION 'É preciso informar um municipio';
	ELSIF v_cod_ibge is null then
		RAISE EXCEPTION 'É preciso informar o código do município';
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
$BODY$;

ALTER FUNCTION soad.prc_insert_municipio_estado_pais(text, text, text, text, text, text)
    OWNER TO soadmin;

COMMENT ON FUNCTION soad.prc_insert_municipio_estado_pais(text, text, text, text, text, text)
    IS 'Procedimento para cadastro de municipio e estado e pais ou municipio ou estado ou pais';
