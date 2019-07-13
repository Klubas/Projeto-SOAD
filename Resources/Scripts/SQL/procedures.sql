-- PROCEDURE: public.inserepessoa(text, text, text)

-- DROP PROCEDURE public.inserepessoa(text, text, text);

-- CALL soad.inserepessoa(p_nome=>'lucas', p_email=>'lucas@gmail.com', p_telefone=>'4299823030');

CREATE OR REPLACE PROCEDURE soad.insert_pessoa(
	p_nome text,
	p_email text,
	p_telefone text)
LANGUAGE 'plpgsql'

AS $BODY$
BEGIN
INSERT INTO "soad".pessoa (nome, email, telefone, data_cadastro)
 VALUES ($1, $2, $3, statement_timestamp());
END;
$BODY$;

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