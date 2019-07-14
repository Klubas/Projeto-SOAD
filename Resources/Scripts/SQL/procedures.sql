-- PROCEDURE: public.inserepessoa(text, text, text)

-- DROP PROCEDURE public.inserepessoa(text, text, text);

-- CALL soad.inserepessoa(p_nome=>'lucas', p_email=>'lucas@gmail.com', p_telefone=>'4299823030');

CREATE PROCEDURE "soad"."prc_insert_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text", "p_fantasia" "text")
    LANGUAGE "plpgsql"
    AS $BODY$
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
	--RAISE NOTICE ''ERRO OCORREU'';
	RAISE EXCEPTION ''% %'', SQLERRM, SQLSTATE;
END;
$BODY$;


ALTER PROCEDURE "soad"."prc_insert_pessoa"("p_nome" "text", "p_email" "text", "p_telefone" "text", "p_documento" "text", "p_inscricao_estadual" "text", "p_fantasia" "text") OWNER TO "postgres";

SET default_tablespace = '';

SET default_with_oids = false;

--- Exemplo inserir em 3 tabelas
WITH Y AS (
  INSERT INTO A (foo)
  VALUES ('abc')
  RETURNING id
), x as (
  INSERT INTO B (a_id, bar)
  SELECT id, 'def'
  FROM Y
  RETURNING id
)
INSERT INTO C (b_id, baz)
SELECT id, 'ghi'
FROM X;

select *
from soad.pessoa