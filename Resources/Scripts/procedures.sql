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

