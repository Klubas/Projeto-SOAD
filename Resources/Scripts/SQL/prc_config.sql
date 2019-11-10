-- FUNCTION: soad.prc_configuracao_definicoes_iniciais()

-- DROP FUNCTION soad.prc_configuracao_definicoes_iniciais();

CREATE OR REPLACE FUNCTION soad.prc_configuracao_definicoes_iniciais(
	)
    RETURNS integer
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$

BEGIN
	DO
		$do$
		BEGIN
		   IF NOT EXISTS (
			  SELECT
			  FROM   pg_catalog.pg_roles
			  WHERE  rolname = 'soadmin') THEN

			  CREATE ROLE soadmin LOGIN PASSWORD 'soad2019';

		   END IF;
		   grant all privileges on database postgres to soadmin;
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
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Distrito Federal', 'DF', 'Brasil', 'BR');
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
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Rio de Janeiro', 'RJ', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Rio Grande do Norte', 'RN', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Rio Grande do Sul', 'RS', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Rondônia', 'RO', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Roraima', 'RR', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Santa Catarina', 'SC', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'São Paulo', 'SP', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Sergipe', 'SE', 'Brasil', 'BR');
		PERFORM soad.prc_insert_municipio_estado_pais('', 'Tocantins', 'TO', 'Brasil', 'BR');

	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro dos estados.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;

	END;

	-- Cadastra municipios
	RAISE NOTICE 'Cadastrando municipios...';
	BEGIN
		PERFORM soad.prc_insert_municipio_estado_pais('Ponta Grossa', 'Paraná', 'PR', 'Brasil', 'BR', '4119905');
		PERFORM soad.prc_insert_municipio_estado_pais('Curitiba', 'Paraná', 'PR', 'Brasil', 'BR', '4106902');
		PERFORM soad.prc_insert_municipio_estado_pais('Castro', 'Paraná', 'PR', 'Brasil', 'BR', '4104907');

	EXCEPTION WHEN OTHERS THEN
		RAISE NOTICE 'Não foi possível realizar o cadastro das municipios.';
		RAISE NOTICE '% %', SQLERRM, SQLSTATE;

	END;

	-- Cadastro VIP Cartuchos
	PERFORM soad.fnc_chamada_de_metodo(
		p_json_params=>'{"metodo": "fnc_cadastro_pessoa", "schema": "soad", "params": {
			"nome": "JOCIANE F. DA SILVA - INFORMÁTICA", "telefone": "4232240660", "documento": "12141655000169", "inscricao_estadual": "90524475-23", "fantasia": "COMÉRCIO DE EQUIPAMENTOS E SUPRIMENTOS DE INFORMÁTICA"
			, "endereco": [{"pessoa_id": "", "id_municipio": 1, "municipio": null, "logradouro": "R. Dr. Paula Xavier", "numero": "1486", "bairro": "Centro", "cep": "84010270", "complemento": "Sala 01", "tipo": "COMERCIAL", "id_endereco": "", "pais": null, "sigla_uf": null}]
			, "modalidade": []}
		}'
	);

	RETURN 0;
END;
$BODY$;

ALTER FUNCTION soad.prc_configuracao_definicoes_iniciais()
    OWNER TO soadmin;

COMMENT ON FUNCTION soad.prc_configuracao_definicoes_iniciais()
    IS 'Algumas configurações iniciais para o uso do sistema';
