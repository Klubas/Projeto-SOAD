--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4
-- Dumped by pg_dump version 11.3

-- Started on 2019-10-17 01:11:34

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
-- TOC entry 3250 (class 0 OID 116197)
-- Dependencies: 197
-- Data for Name: auditoria; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.auditoria (id_auditoria, nome_tabela, nome_coluna, operacao, old_value, new_value, usuario, data) FROM stdin;
21108	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "7", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2482,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:15:59.762
21109	remanufatura	\N	INSERT	\N	{"id_remanufatura":1215,"fk_pedido_id":null,"fk_casco_id":7,"valor_unitario":null,"data_cadastro":"2019-09-28","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-09-28 13:15:59.762
21110	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "7", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2482,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "7", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2482,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:15:59.762
21111	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1215, "simular": true},"id_requisicao":2483,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:15:59.764
21112	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1215, "simular": true},"id_requisicao":2483,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1215, "simular": true},"id_requisicao":2483,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:15:59.764
21113	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1215},"id_requisicao":2484,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:16:25.928
21114	item_lote	\N	UPDATE	{"id_item_lote":5179,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5179,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-09-28","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-09-28 13:16:25.928
21115	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-09-28 13:16:25.928
21116	remanufatura	\N	UPDATE	{"id_remanufatura":1215,"fk_pedido_id":null,"fk_casco_id":7,"valor_unitario":null,"data_cadastro":"2019-09-28","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1215,"fk_pedido_id":null,"fk_casco_id":7,"valor_unitario":null,"data_cadastro":"2019-09-28","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001909281215"}	soadmin	2019-09-28 13:16:25.928
21117	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":251,"fk_remanufatura_id":1215,"fk_item_lote_id":5179,"data_cadastro":"2019-09-28"}	soadmin	2019-09-28 13:16:25.928
21118	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1215},"id_requisicao":2484,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1215},"id_requisicao":2484,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:16:25.928
21119	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1215", "simular": true},"id_requisicao":2485,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:16:25.964
21120	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1215", "simular": true},"id_requisicao":2485,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1215", "simular": true},"id_requisicao":2485,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:16:25.964
21121	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5179"},"id_requisicao":2486,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:16:35.102
21122	item_lote	\N	UPDATE	{"id_item_lote":5179,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-09-28","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5179,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-09-28T13:16:35.1023-03:00","motivo_retirada":null,"quantidade_item":0,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-09-28","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-09-28 13:16:35.102
21123	requisicao	\N	UPDATE	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5179"},"id_requisicao":2486,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5179"},"id_requisicao":2486,"retorno":"100","data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:16:35.102
21130	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]},"id_requisicao":2490,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:27:49.511
21131	pessoa	\N	UPDATE	{"id_pessoa":312,"nome":"A C PEREIRA - INFORMATICA EIRELI","email":null,"telefone":null,"data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	{"id_pessoa":312,"nome":"A C PEREIRA - INFORMATICA EIRELI","email":null,"telefone":null,"data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	soadmin	2019-10-02 22:27:49.511
21132	pessoa_juridica	\N	UPDATE	{"id_pessoa_juridica":154,"fk_pessoa_id":312,"cnpj":"02526512000111","fantasia":"PEREIRA & CONCEIÇÃO - INFORMÁTICA","data_cadastro":"2019-09-19T02:38:34.1097-03:00"}	{"id_pessoa_juridica":154,"fk_pessoa_id":312,"cnpj":"02526512000111","fantasia":"PEREIRA & CONCEIÇÃO - INFORMÁTICA","data_cadastro":"2019-09-19T02:38:34.1097-03:00"}	soadmin	2019-10-02 22:27:49.511
21133	endereco	\N	UPDATE	{"id_endereco":57,"fk_municipio_id":34,"fk_pessoa_id":312,"logradouro":"RUA ABELIO BENATTI","numero":"00000","bairro":"JARDIM SOL","cep":"84072000","complemento":"","tipo":"COMERCIAL"}	{"id_endereco":57,"fk_municipio_id":34,"fk_pessoa_id":312,"logradouro":"RUA ABELIO BENATTI","numero":"00000","bairro":"JARDIM SOL","cep":"84072000","complemento":"","tipo":"COMERCIAL"}	soadmin	2019-10-02 22:27:49.511
21134	modalidade_pessoa	\N	DELETE	{"id_modalidade_pessoa":165,"fk_pessoa_id":312,"fk_modalidade_id":57}	\N	soadmin	2019-10-02 22:27:49.511
21135	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":175,"fk_pessoa_id":312,"fk_modalidade_id":57}	soadmin	2019-10-02 22:27:49.511
21136	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":176,"fk_pessoa_id":312,"fk_modalidade_id":58}	soadmin	2019-10-02 22:27:49.511
21137	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]},"id_requisicao":2490,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]},"id_requisicao":2490,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:27:49.511
21138	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57]},"id_requisicao":2491,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:27:54.85
21139	pessoa	\N	UPDATE	{"id_pessoa":312,"nome":"A C PEREIRA - INFORMATICA EIRELI","email":null,"telefone":null,"data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	{"id_pessoa":312,"nome":"A C PEREIRA - INFORMATICA EIRELI","email":null,"telefone":null,"data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	soadmin	2019-10-02 22:27:54.85
21140	pessoa_juridica	\N	UPDATE	{"id_pessoa_juridica":154,"fk_pessoa_id":312,"cnpj":"02526512000111","fantasia":"PEREIRA & CONCEIÇÃO - INFORMÁTICA","data_cadastro":"2019-09-19T02:38:34.1097-03:00"}	{"id_pessoa_juridica":154,"fk_pessoa_id":312,"cnpj":"02526512000111","fantasia":"PEREIRA & CONCEIÇÃO - INFORMÁTICA","data_cadastro":"2019-09-19T02:38:34.1097-03:00"}	soadmin	2019-10-02 22:27:54.85
21141	endereco	\N	UPDATE	{"id_endereco":57,"fk_municipio_id":34,"fk_pessoa_id":312,"logradouro":"RUA ABELIO BENATTI","numero":"00000","bairro":"JARDIM SOL","cep":"84072000","complemento":"","tipo":"COMERCIAL"}	{"id_endereco":57,"fk_municipio_id":34,"fk_pessoa_id":312,"logradouro":"RUA ABELIO BENATTI","numero":"00000","bairro":"JARDIM SOL","cep":"84072000","complemento":"","tipo":"COMERCIAL"}	soadmin	2019-10-02 22:27:54.85
21142	modalidade_pessoa	\N	DELETE	{"id_modalidade_pessoa":175,"fk_pessoa_id":312,"fk_modalidade_id":57}	\N	soadmin	2019-10-02 22:27:54.85
21143	modalidade_pessoa	\N	DELETE	{"id_modalidade_pessoa":176,"fk_pessoa_id":312,"fk_modalidade_id":58}	\N	soadmin	2019-10-02 22:27:54.85
21144	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":177,"fk_pessoa_id":312,"fk_modalidade_id":57}	soadmin	2019-10-02 22:27:54.85
21145	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57]},"id_requisicao":2491,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57]},"id_requisicao":2491,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:27:54.85
21146	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "Rua Padre jos\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\u00fassia", "cep": "84031029", "complemento": "Pr\\u00f3ximo ao mercadinho do seu z\\u00e9", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]},"id_requisicao":2492,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:50:51.339
21147	pessoa	\N	INSERT	\N	{"id_pessoa":321,"nome":"Idomar Augusto","email":"idomar@uepg.br","telefone":"42999823030","data_cadastro":"2019-10-02","inscricao_estadual":"ISENTO"}	soadmin	2019-10-02 22:50:51.339
21148	pessoa_fisica	\N	INSERT	\N	{"id_pessoa_fisica":71,"fk_pessoa_id":321,"cpf":"11111111111","data_cadastro":"22:50:51.3388-03","rg":null}	soadmin	2019-10-02 22:50:51.339
21149	endereco	\N	INSERT	\N	{"id_endereco":66,"fk_municipio_id":34,"fk_pessoa_id":321,"logradouro":"Rua Padre jos\\\\u00e9 da Silva","numero":"123","bairro":"Jardim Nova R\\\\u00fassia","cep":"84031029","complemento":"Pr\\\\u00f3ximo ao mercadinho do seu z\\\\u00e9","tipo":"COMERCIAL"}	soadmin	2019-10-02 22:50:51.339
21150	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":178,"fk_pessoa_id":321,"fk_modalidade_id":57}	soadmin	2019-10-02 22:50:51.339
21151	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "Rua Padre jos\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\u00fassia", "cep": "84031029", "complemento": "Pr\\u00f3ximo ao mercadinho do seu z\\u00e9", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]},"id_requisicao":2492,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "Rua Padre jos\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\u00fassia", "cep": "84031029", "complemento": "Pr\\u00f3ximo ao mercadinho do seu z\\u00e9", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]},"id_requisicao":2492,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:50:51.339
21152	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "pessoa_id": "321", "endereco": [{"pessoa_id": "321", "id_municipio": 34, "logradouro": "Rua Padre jos\\\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\\\u00fassia", "cep": "84031029", "complemento": "Pr\\\\u00f3ximo ao mercadinho do seu z\\\\u00e9", "tipo": "COMERCIAL", "id_endereco": "66"}], "modalidade": [57]},"id_requisicao":2493,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:50:58.613
21153	pessoa	\N	UPDATE	{"id_pessoa":321,"nome":"Idomar Augusto","email":"idomar@uepg.br","telefone":"42999823030","data_cadastro":"2019-10-02","inscricao_estadual":"ISENTO"}	{"id_pessoa":321,"nome":"Idomar Augusto","email":"idomar@uepg.br","telefone":"42999823030","data_cadastro":"2019-10-02","inscricao_estadual":"ISENTO"}	soadmin	2019-10-02 22:50:58.613
21154	endereco	\N	UPDATE	{"id_endereco":66,"fk_municipio_id":34,"fk_pessoa_id":321,"logradouro":"Rua Padre jos\\\\u00e9 da Silva","numero":"123","bairro":"Jardim Nova R\\\\u00fassia","cep":"84031029","complemento":"Pr\\\\u00f3ximo ao mercadinho do seu z\\\\u00e9","tipo":"COMERCIAL"}	{"id_endereco":66,"fk_municipio_id":34,"fk_pessoa_id":321,"logradouro":"Rua Padre jos\\\\\\\\u00e9 da Silva","numero":"123","bairro":"Jardim Nova R\\\\\\\\u00fassia","cep":"84031029","complemento":"Pr\\\\\\\\u00f3ximo ao mercadinho do seu z\\\\\\\\u00e9","tipo":"COMERCIAL"}	soadmin	2019-10-02 22:50:58.613
21155	modalidade_pessoa	\N	DELETE	{"id_modalidade_pessoa":178,"fk_pessoa_id":321,"fk_modalidade_id":57}	\N	soadmin	2019-10-02 22:50:58.613
21156	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":179,"fk_pessoa_id":321,"fk_modalidade_id":57}	soadmin	2019-10-02 22:50:58.613
21157	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "pessoa_id": "321", "endereco": [{"pessoa_id": "321", "id_municipio": 34, "logradouro": "Rua Padre jos\\\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\\\u00fassia", "cep": "84031029", "complemento": "Pr\\\\u00f3ximo ao mercadinho do seu z\\\\u00e9", "tipo": "COMERCIAL", "id_endereco": "66"}], "modalidade": [57]},"id_requisicao":2493,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "pessoa_id": "321", "endereco": [{"pessoa_id": "321", "id_municipio": 34, "logradouro": "Rua Padre jos\\\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\\\u00fassia", "cep": "84031029", "complemento": "Pr\\\\u00f3ximo ao mercadinho do seu z\\\\u00e9", "tipo": "COMERCIAL", "id_endereco": "66"}], "modalidade": [57]},"id_requisicao":2493,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:50:58.613
21158	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2494,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:54:32.211
21159	pedido	\N	INSERT	\N	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"CADASTRADO"}	soadmin	2019-10-02 22:54:32.211
21160	item_pedido	\N	INSERT	\N	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-02 22:54:32.211
21161	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2494,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2494,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:54:32.211
21162	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2495,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:55:25.442
21163	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"CADASTRADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ENCERRADO"}	soadmin	2019-10-02 22:55:25.442
21164	lote	\N	INSERT	\N	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-02 22:55:25.442
21165	item_lote	\N	INSERT	\N	{"id_item_lote":5262,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21166	item_lote	\N	INSERT	\N	{"id_item_lote":5263,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21167	item_lote	\N	INSERT	\N	{"id_item_lote":5264,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21168	item_lote	\N	INSERT	\N	{"id_item_lote":5265,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21169	item_lote	\N	INSERT	\N	{"id_item_lote":5266,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21170	item_lote	\N	INSERT	\N	{"id_item_lote":5267,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21171	item_lote	\N	INSERT	\N	{"id_item_lote":5268,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21172	item_lote	\N	INSERT	\N	{"id_item_lote":5269,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21173	item_lote	\N	INSERT	\N	{"id_item_lote":5270,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21174	item_lote	\N	INSERT	\N	{"id_item_lote":5271,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21175	item_lote	\N	INSERT	\N	{"id_item_lote":5272,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21176	item_lote	\N	INSERT	\N	{"id_item_lote":5273,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21177	item_lote	\N	INSERT	\N	{"id_item_lote":5274,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21178	item_lote	\N	INSERT	\N	{"id_item_lote":5275,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21179	item_lote	\N	INSERT	\N	{"id_item_lote":5276,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21180	item_lote	\N	INSERT	\N	{"id_item_lote":5277,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21181	item_lote	\N	INSERT	\N	{"id_item_lote":5278,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21182	item_lote	\N	INSERT	\N	{"id_item_lote":5279,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21183	item_lote	\N	INSERT	\N	{"id_item_lote":5280,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21184	item_lote	\N	INSERT	\N	{"id_item_lote":5281,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21185	item_lote	\N	INSERT	\N	{"id_item_lote":5282,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21186	item_lote	\N	INSERT	\N	{"id_item_lote":5283,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21187	item_lote	\N	INSERT	\N	{"id_item_lote":5284,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21188	item_lote	\N	INSERT	\N	{"id_item_lote":5285,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21189	item_lote	\N	INSERT	\N	{"id_item_lote":5286,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21190	item_lote	\N	INSERT	\N	{"id_item_lote":5287,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21191	item_lote	\N	INSERT	\N	{"id_item_lote":5288,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21192	item_lote	\N	INSERT	\N	{"id_item_lote":5289,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21193	item_lote	\N	INSERT	\N	{"id_item_lote":5290,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21194	item_lote	\N	INSERT	\N	{"id_item_lote":5291,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21195	item_lote	\N	INSERT	\N	{"id_item_lote":5292,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21196	item_lote	\N	INSERT	\N	{"id_item_lote":5293,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21197	item_lote	\N	INSERT	\N	{"id_item_lote":5294,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21198	item_lote	\N	INSERT	\N	{"id_item_lote":5295,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21199	item_lote	\N	INSERT	\N	{"id_item_lote":5296,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21200	item_lote	\N	INSERT	\N	{"id_item_lote":5297,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21201	item_lote	\N	INSERT	\N	{"id_item_lote":5298,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21202	item_lote	\N	INSERT	\N	{"id_item_lote":5299,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21203	item_lote	\N	INSERT	\N	{"id_item_lote":5300,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21204	item_lote	\N	INSERT	\N	{"id_item_lote":5301,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21205	item_lote	\N	INSERT	\N	{"id_item_lote":5302,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21206	item_lote	\N	INSERT	\N	{"id_item_lote":5303,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21207	item_lote	\N	INSERT	\N	{"id_item_lote":5304,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21208	item_lote	\N	INSERT	\N	{"id_item_lote":5305,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21209	item_lote	\N	INSERT	\N	{"id_item_lote":5306,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21210	item_lote	\N	INSERT	\N	{"id_item_lote":5307,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21211	item_lote	\N	INSERT	\N	{"id_item_lote":5308,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21212	item_lote	\N	INSERT	\N	{"id_item_lote":5309,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21213	item_lote	\N	INSERT	\N	{"id_item_lote":5310,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21214	item_lote	\N	INSERT	\N	{"id_item_lote":5311,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:55:25.442
21215	requisicao	\N	UPDATE	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2495,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2495,"retorno":"100","data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:55:25.442
21216	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pessoa_id": 321, "tipo_pedido": "VENDA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 5, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2496,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:56:42.981
21217	pedido	\N	INSERT	\N	{"id_pedido":449,"fk_pessoa_id":321,"data_entrega":null,"tipo_pedido":"VENDA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"CADASTRADO"}	soadmin	2019-10-02 22:56:42.981
21218	item_pedido	\N	INSERT	\N	{"id_item_pedido":496,"fk_pedido_id":449,"fk_mercadoria_id":51,"quantidade":5,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-02 22:56:42.981
21219	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pessoa_id": 321, "tipo_pedido": "VENDA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 5, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2496,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pessoa_id": 321, "tipo_pedido": "VENDA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 5, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2496,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:56:42.981
21220	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2497,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:56:47.456
21221	pedido	\N	UPDATE	{"id_pedido":449,"fk_pessoa_id":321,"data_entrega":null,"tipo_pedido":"VENDA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"CADASTRADO"}	{"id_pedido":449,"fk_pessoa_id":321,"data_entrega":null,"tipo_pedido":"VENDA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ENCERRADO"}	soadmin	2019-10-02 22:56:47.456
21222	item_lote	\N	UPDATE	{"id_item_lote":5262,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5262,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:56:47.456
21223	item_lote	\N	UPDATE	{"id_item_lote":5263,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5263,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:56:47.456
21224	item_lote	\N	UPDATE	{"id_item_lote":5264,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5264,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:56:47.456
21225	item_lote	\N	UPDATE	{"id_item_lote":5265,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5265,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:56:47.456
21226	item_lote	\N	UPDATE	{"id_item_lote":5266,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5266,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-02 22:56:47.456
21227	lote	\N	UPDATE	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-02 22:56:47.456
21228	requisicao	\N	UPDATE	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2497,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2497,"retorno":"100","data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 22:56:47.456
21229	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "8", "insumo_id": "15", "quantidade": "1", "realizar": false},"id_requisicao":2498,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:10:24.327
21230	remanufatura	\N	INSERT	\N	{"id_remanufatura":1216,"fk_pedido_id":null,"fk_casco_id":8,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":15,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:10:24.327
21231	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "8", "insumo_id": "15", "quantidade": "1", "realizar": false},"id_requisicao":2498,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "8", "insumo_id": "15", "quantidade": "1", "realizar": false},"id_requisicao":2498,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:10:24.327
21233	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "8", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2500,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:10:40.589
21234	remanufatura	\N	INSERT	\N	{"id_remanufatura":1217,"fk_pedido_id":null,"fk_casco_id":8,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:10:40.589
21235	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "8", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2500,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "8", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2500,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:10:40.589
21236	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1217, "simular": true},"id_requisicao":2501,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:10:40.591
21237	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1217, "simular": true},"id_requisicao":2501,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1217, "simular": true},"id_requisicao":2501,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:10:40.591
21238	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[1217]"},"id_requisicao":2502,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:11:58.108
21239	remanufatura	\N	DELETE	{"id_remanufatura":1217,"fk_pedido_id":null,"fk_casco_id":8,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	\N	soadmin	2019-10-02 23:11:58.108
21240	requisicao	\N	UPDATE	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[1217]"},"id_requisicao":2502,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[1217]"},"id_requisicao":2502,"retorno":"100","data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:11:58.108
21241	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2503,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:34.971
21242	remanufatura	\N	INSERT	\N	{"id_remanufatura":1218,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:12:34.971
21243	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2503,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2503,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:34.971
21244	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1218, "simular": true},"id_requisicao":2504,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:34.973
21245	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1218, "simular": true},"id_requisicao":2504,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1218, "simular": true},"id_requisicao":2504,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:34.973
21246	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false},"id_requisicao":2505,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:38.307
21247	remanufatura	\N	INSERT	\N	{"id_remanufatura":1219,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:12:38.307
21248	remanufatura	\N	INSERT	\N	{"id_remanufatura":1220,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:12:38.307
21249	remanufatura	\N	INSERT	\N	{"id_remanufatura":1221,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:12:38.307
21250	remanufatura	\N	INSERT	\N	{"id_remanufatura":1222,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:12:38.307
21251	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false},"id_requisicao":2505,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false},"id_requisicao":2505,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:38.307
21252	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1219, "simular": true},"id_requisicao":2506,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:38.31
21253	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1219, "simular": true},"id_requisicao":2506,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1219, "simular": true},"id_requisicao":2506,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:38.31
21254	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1218},"id_requisicao":2507,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.091
21255	item_lote	\N	UPDATE	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:12:52.091
21256	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-10-02 23:12:52.091
21257	remanufatura	\N	UPDATE	{"id_remanufatura":1218,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1218,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001910021218"}	soadmin	2019-10-02 23:12:52.091
21258	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":252,"fk_remanufatura_id":1218,"fk_item_lote_id":5180,"data_cadastro":"2019-10-02"}	soadmin	2019-10-02 23:12:52.091
21259	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1218},"id_requisicao":2507,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1218},"id_requisicao":2507,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.091
21260	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1218", "simular": true},"id_requisicao":2508,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.115
21261	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1218", "simular": true},"id_requisicao":2508,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1218", "simular": true},"id_requisicao":2508,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.115
21262	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1219},"id_requisicao":2509,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.137
21263	item_lote	\N	UPDATE	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:12:52.137
21264	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-10-02 23:12:52.137
21265	remanufatura	\N	UPDATE	{"id_remanufatura":1219,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1219,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001910021219"}	soadmin	2019-10-02 23:12:52.137
21266	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":253,"fk_remanufatura_id":1219,"fk_item_lote_id":5180,"data_cadastro":"2019-10-02"}	soadmin	2019-10-02 23:12:52.137
21267	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1219},"id_requisicao":2509,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1219},"id_requisicao":2509,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.137
21268	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1219", "simular": true},"id_requisicao":2510,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.147
21269	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1219", "simular": true},"id_requisicao":2510,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1219", "simular": true},"id_requisicao":2510,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.147
21270	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1220},"id_requisicao":2511,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.167
21271	item_lote	\N	UPDATE	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:12:52.167
21272	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-10-02 23:12:52.167
21273	remanufatura	\N	UPDATE	{"id_remanufatura":1220,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1220,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001910021220"}	soadmin	2019-10-02 23:12:52.167
21274	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":254,"fk_remanufatura_id":1220,"fk_item_lote_id":5180,"data_cadastro":"2019-10-02"}	soadmin	2019-10-02 23:12:52.167
21275	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1220},"id_requisicao":2511,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1220},"id_requisicao":2511,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.167
21276	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1220", "simular": true},"id_requisicao":2512,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.176
21277	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1220", "simular": true},"id_requisicao":2512,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1220", "simular": true},"id_requisicao":2512,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.176
21278	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1221},"id_requisicao":2513,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.197
21279	item_lote	\N	UPDATE	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:12:52.197
21280	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-10-02 23:12:52.197
21281	remanufatura	\N	UPDATE	{"id_remanufatura":1221,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1221,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001910021221"}	soadmin	2019-10-02 23:12:52.197
21282	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":255,"fk_remanufatura_id":1221,"fk_item_lote_id":5180,"data_cadastro":"2019-10-02"}	soadmin	2019-10-02 23:12:52.197
21283	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1221},"id_requisicao":2513,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1221},"id_requisicao":2513,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.197
21284	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1221", "simular": true},"id_requisicao":2514,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.207
21285	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1221", "simular": true},"id_requisicao":2514,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1221", "simular": true},"id_requisicao":2514,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.207
21286	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1222},"id_requisicao":2515,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.227
21287	item_lote	\N	UPDATE	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:12:52.227
21288	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-10-02 23:12:52.227
21289	remanufatura	\N	UPDATE	{"id_remanufatura":1222,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1222,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001910021222"}	soadmin	2019-10-02 23:12:52.227
21290	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":256,"fk_remanufatura_id":1222,"fk_item_lote_id":5180,"data_cadastro":"2019-10-02"}	soadmin	2019-10-02 23:12:52.227
21291	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1222},"id_requisicao":2515,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1222},"id_requisicao":2515,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.227
21292	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1222", "simular": true},"id_requisicao":2516,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.237
21293	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1222", "simular": true},"id_requisicao":2516,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1222", "simular": true},"id_requisicao":2516,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:12:52.237
21294	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5180"},"id_requisicao":2517,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:13:15.159
21295	item_lote	\N	UPDATE	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5180,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T23:13:15.1589-03:00","motivo_retirada":null,"quantidade_item":0,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:13:15.159
21296	requisicao	\N	UPDATE	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5180"},"id_requisicao":2517,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5180"},"id_requisicao":2517,"retorno":"100","data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:13:15.159
21297	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false},"id_requisicao":2518,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:14:01.559
21298	remanufatura	\N	INSERT	\N	{"id_remanufatura":1223,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:14:01.559
21299	remanufatura	\N	INSERT	\N	{"id_remanufatura":1224,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:14:01.559
21300	remanufatura	\N	INSERT	\N	{"id_remanufatura":1225,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:14:01.559
21301	remanufatura	\N	INSERT	\N	{"id_remanufatura":1226,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:14:01.559
21302	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false},"id_requisicao":2518,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false},"id_requisicao":2518,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:14:01.559
21303	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1223, "simular": true},"id_requisicao":2519,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:14:01.561
21304	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1223, "simular": true},"id_requisicao":2519,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1223, "simular": true},"id_requisicao":2519,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:14:01.561
21305	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[1224, 1225, 1226]"},"id_requisicao":2520,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:18:53.226
21306	remanufatura	\N	DELETE	{"id_remanufatura":1224,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	\N	soadmin	2019-10-02 23:18:53.226
21307	remanufatura	\N	DELETE	{"id_remanufatura":1225,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	\N	soadmin	2019-10-02 23:18:53.226
21308	remanufatura	\N	DELETE	{"id_remanufatura":1226,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	\N	soadmin	2019-10-02 23:18:53.226
21309	requisicao	\N	UPDATE	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[1224, 1225, 1226]"},"id_requisicao":2520,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[1224, 1225, 1226]"},"id_requisicao":2520,"retorno":"100","data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:18:53.226
21310	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1223},"id_requisicao":2521,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:19:00.657
21311	item_lote	\N	UPDATE	{"id_item_lote":5181,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5181,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:19:00.657
21312	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-10-02 23:19:00.657
21313	remanufatura	\N	UPDATE	{"id_remanufatura":1223,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1223,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001910021223"}	soadmin	2019-10-02 23:19:00.657
21314	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":257,"fk_remanufatura_id":1223,"fk_item_lote_id":5181,"data_cadastro":"2019-10-02"}	soadmin	2019-10-02 23:19:00.657
21315	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1223},"id_requisicao":2521,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1223},"id_requisicao":2521,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:19:00.657
21316	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1223", "simular": true},"id_requisicao":2522,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:19:00.668
21317	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1223", "simular": true},"id_requisicao":2522,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1223", "simular": true},"id_requisicao":2522,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:19:00.668
21318	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "14", "quantidade": "1", "realizar": false},"id_requisicao":2523,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:19:22.428
21319	remanufatura	\N	INSERT	\N	{"id_remanufatura":1227,"fk_pedido_id":null,"fk_casco_id":5,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":14,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:19:22.428
21320	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "14", "quantidade": "1", "realizar": false},"id_requisicao":2523,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "5", "insumo_id": "14", "quantidade": "1", "realizar": false},"id_requisicao":2523,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:19:22.428
21322	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2525,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:19.508
21323	remanufatura	\N	INSERT	\N	{"id_remanufatura":1228,"fk_pedido_id":null,"fk_casco_id":9,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-02 23:22:19.508
21324	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2525,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2525,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:19.508
21325	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1228, "simular": true},"id_requisicao":2526,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:19.544
21326	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1228, "simular": true},"id_requisicao":2526,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1228, "simular": true},"id_requisicao":2526,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:19.544
21327	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1228},"id_requisicao":2527,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:26.434
21328	item_lote	\N	UPDATE	{"id_item_lote":5181,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5181,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:22:26.434
21329	lote	\N	UPDATE	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	{"id_lote":207,"fk_pedido_id":447,"data_cadastro":"2019-09-19","vazio":false,"observacao":null,"fk_mercadoria_id":35,"valor_unitario":45,"fk_unidade_medida_id":276}	soadmin	2019-10-02 23:22:26.434
21330	remanufatura	\N	UPDATE	{"id_remanufatura":1228,"fk_pedido_id":null,"fk_casco_id":9,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	{"id_remanufatura":1228,"fk_pedido_id":null,"fk_casco_id":9,"valor_unitario":null,"data_cadastro":"2019-10-02","fk_insumo_id":10,"situacao":"REALIZADA","codigo":"000001910021228"}	soadmin	2019-10-02 23:22:26.434
21331	item_lote_remanufatura	\N	INSERT	\N	{"id_item_lote_remanufatura":258,"fk_remanufatura_id":1228,"fk_item_lote_id":5181,"data_cadastro":"2019-10-02"}	soadmin	2019-10-02 23:22:26.434
21332	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1228},"id_requisicao":2527,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1228},"id_requisicao":2527,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:26.434
21333	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1228", "simular": true},"id_requisicao":2528,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:26.446
21334	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1228", "simular": true},"id_requisicao":2528,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": "1228", "simular": true},"id_requisicao":2528,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:26.446
21335	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5181"},"id_requisicao":2529,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:54.948
21336	item_lote	\N	UPDATE	{"id_item_lote":5181,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	{"id_item_lote":5181,"fk_lote_id":207,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T23:22:54.9478-03:00","motivo_retirada":null,"quantidade_item":0,"fk_item_pedido_entrada_id":491,"data_cadastro":"2019-09-19","aberto":true,"data_abertura":"2019-10-02","motivo_abertura":"Remanufatura (operação interna)"}	soadmin	2019-10-02 23:22:54.948
21337	requisicao	\N	UPDATE	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5181"},"id_requisicao":2529,"retorno":null,"data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_esvaziar_item_lote","params_json":{"item_lote_id": "5181"},"id_requisicao":2529,"retorno":"100","data_requisicao":"2019-10-02","usuario":"soadmin","mensagem":null}	soadmin	2019-10-02 23:22:54.948
21338	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2530,"retorno":null,"data_requisicao":"2019-10-09","usuario":"soadmin","mensagem":null}	soadmin	2019-10-09 00:00:30.261
21339	pedido	\N	UPDATE	{"id_pedido":449,"fk_pessoa_id":321,"data_entrega":null,"tipo_pedido":"VENDA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ENCERRADO"}	{"id_pedido":449,"fk_pessoa_id":321,"data_entrega":null,"tipo_pedido":"VENDA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ESTORNADO"}	soadmin	2019-10-09 00:00:30.261
21340	item_lote	\N	UPDATE	{"id_item_lote":5262,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5262,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-09 00:00:30.261
21341	lote	\N	UPDATE	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-09 00:00:30.261
21342	item_lote	\N	UPDATE	{"id_item_lote":5263,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5263,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-09 00:00:30.261
21343	lote	\N	UPDATE	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-09 00:00:30.261
21344	item_lote	\N	UPDATE	{"id_item_lote":5264,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5264,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-09 00:00:30.261
21345	lote	\N	UPDATE	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-09 00:00:30.261
21346	item_lote	\N	UPDATE	{"id_item_lote":5265,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5265,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-09 00:00:30.261
21347	lote	\N	UPDATE	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-09 00:00:30.261
21348	item_lote	\N	UPDATE	{"id_item_lote":5266,"fk_lote_id":211,"fk_item_pedido_saida_id":496,"data_validade":null,"lote_fabricante":null,"data_retirada":"2019-10-02T22:56:47.456-03:00","motivo_retirada":"Pedido 449 Tipo: VENDA","quantidade_item":0,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	{"id_item_lote":5266,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-09 00:00:30.261
21349	lote	\N	UPDATE	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-09 00:00:30.261
21350	requisicao	\N	UPDATE	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2530,"retorno":null,"data_requisicao":"2019-10-09","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2530,"retorno":"100","data_requisicao":"2019-10-09","usuario":"soadmin","mensagem":null}	soadmin	2019-10-09 00:00:30.261
21351	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "FUNDEPAR/COL\\u00c9GIO ESTADUAL JOS\\u00c9 ELIAS DA ROCHA/FUNDO ROTATIVO", "telefone": "4232241451", "documento": "77741312000180", "inscricao_estadual": "ISENTO", "pessoa_id": "311", "endereco": [{"pessoa_id": "311", "id_municipio": 34, "logradouro": "RUA RICARDO WAGNER", "numero": "200", "bairro": "OLARIAS", "cep": "84035220", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "56"}], "modalidade": [57, 58]},"id_requisicao":2531,"retorno":null,"data_requisicao":"2019-10-09","usuario":"soadmin","mensagem":null}	soadmin	2019-10-09 01:08:00.038
21352	pessoa	\N	UPDATE	{"id_pessoa":311,"nome":"FUNDEPAR/COLÉGIO ESTADUAL JOSÉ ELIAS DA ROCHA/FUNDO ROTATIVO","email":null,"telefone":"4232241451","data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	{"id_pessoa":311,"nome":"FUNDEPAR/COLÉGIO ESTADUAL JOSÉ ELIAS DA ROCHA/FUNDO ROTATIVO","email":null,"telefone":"4232241451","data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	soadmin	2019-10-09 01:08:00.038
21353	pessoa_juridica	\N	UPDATE	{"id_pessoa_juridica":153,"fk_pessoa_id":311,"cnpj":"77741312000180","fantasia":null,"data_cadastro":"2019-09-19T02:37:07.5077-03:00"}	{"id_pessoa_juridica":153,"fk_pessoa_id":311,"cnpj":"77741312000180","fantasia":null,"data_cadastro":"2019-09-19T02:37:07.5077-03:00"}	soadmin	2019-10-09 01:08:00.038
21354	endereco	\N	UPDATE	{"id_endereco":56,"fk_municipio_id":34,"fk_pessoa_id":311,"logradouro":"RUA RICARDO WAGNER","numero":"200","bairro":"OLARIAS","cep":"84035220","complemento":"","tipo":"COMERCIAL"}	{"id_endereco":56,"fk_municipio_id":34,"fk_pessoa_id":311,"logradouro":"RUA RICARDO WAGNER","numero":"200","bairro":"OLARIAS","cep":"84035220","complemento":"","tipo":"COMERCIAL"}	soadmin	2019-10-09 01:08:00.038
21355	modalidade_pessoa	\N	DELETE	{"id_modalidade_pessoa":164,"fk_pessoa_id":311,"fk_modalidade_id":57}	\N	soadmin	2019-10-09 01:08:00.038
21356	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":180,"fk_pessoa_id":311,"fk_modalidade_id":57}	soadmin	2019-10-09 01:08:00.038
21357	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":181,"fk_pessoa_id":311,"fk_modalidade_id":58}	soadmin	2019-10-09 01:08:00.038
21358	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "FUNDEPAR/COL\\u00c9GIO ESTADUAL JOS\\u00c9 ELIAS DA ROCHA/FUNDO ROTATIVO", "telefone": "4232241451", "documento": "77741312000180", "inscricao_estadual": "ISENTO", "pessoa_id": "311", "endereco": [{"pessoa_id": "311", "id_municipio": 34, "logradouro": "RUA RICARDO WAGNER", "numero": "200", "bairro": "OLARIAS", "cep": "84035220", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "56"}], "modalidade": [57, 58]},"id_requisicao":2531,"retorno":null,"data_requisicao":"2019-10-09","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "FUNDEPAR/COL\\u00c9GIO ESTADUAL JOS\\u00c9 ELIAS DA ROCHA/FUNDO ROTATIVO", "telefone": "4232241451", "documento": "77741312000180", "inscricao_estadual": "ISENTO", "pessoa_id": "311", "endereco": [{"pessoa_id": "311", "id_municipio": 34, "logradouro": "RUA RICARDO WAGNER", "numero": "200", "bairro": "OLARIAS", "cep": "84035220", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "56"}], "modalidade": [57, 58]},"id_requisicao":2531,"retorno":null,"data_requisicao":"2019-10-09","usuario":"soadmin","mensagem":null}	soadmin	2019-10-09 01:08:00.038
21359	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]},"id_requisicao":2532,"retorno":null,"data_requisicao":"2019-10-15","usuario":"soadmin","mensagem":null}	soadmin	2019-10-15 23:24:56.545
21360	pessoa	\N	UPDATE	{"id_pessoa":312,"nome":"A C PEREIRA - INFORMATICA EIRELI","email":null,"telefone":null,"data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	{"id_pessoa":312,"nome":"A C PEREIRA - INFORMATICA EIRELI","email":null,"telefone":null,"data_cadastro":"2019-09-19","inscricao_estadual":"ISENTO"}	soadmin	2019-10-15 23:24:56.545
21361	pessoa_juridica	\N	UPDATE	{"id_pessoa_juridica":154,"fk_pessoa_id":312,"cnpj":"02526512000111","fantasia":"PEREIRA & CONCEIÇÃO - INFORMÁTICA","data_cadastro":"2019-09-19T02:38:34.1097-03:00"}	{"id_pessoa_juridica":154,"fk_pessoa_id":312,"cnpj":"02526512000111","fantasia":"PEREIRA & CONCEIÇÃO - INFORMÁTICA","data_cadastro":"2019-09-19T02:38:34.1097-03:00"}	soadmin	2019-10-15 23:24:56.545
21362	endereco	\N	UPDATE	{"id_endereco":57,"fk_municipio_id":34,"fk_pessoa_id":312,"logradouro":"RUA ABELIO BENATTI","numero":"00000","bairro":"JARDIM SOL","cep":"84072000","complemento":"","tipo":"COMERCIAL"}	{"id_endereco":57,"fk_municipio_id":34,"fk_pessoa_id":312,"logradouro":"RUA ABELIO BENATTI","numero":"00000","bairro":"JARDIM SOL","cep":"84072000","complemento":"","tipo":"COMERCIAL"}	soadmin	2019-10-15 23:24:56.545
21363	modalidade_pessoa	\N	DELETE	{"id_modalidade_pessoa":177,"fk_pessoa_id":312,"fk_modalidade_id":57}	\N	soadmin	2019-10-15 23:24:56.545
21364	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":182,"fk_pessoa_id":312,"fk_modalidade_id":57}	soadmin	2019-10-15 23:24:56.545
21365	modalidade_pessoa	\N	INSERT	\N	{"id_modalidade_pessoa":183,"fk_pessoa_id":312,"fk_modalidade_id":58}	soadmin	2019-10-15 23:24:56.545
21366	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]},"id_requisicao":2532,"retorno":null,"data_requisicao":"2019-10-15","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pessoa","params_json":{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]},"id_requisicao":2532,"retorno":null,"data_requisicao":"2019-10-15","usuario":"soadmin","mensagem":null}	soadmin	2019-10-15 23:24:56.545
21367	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2533,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 21:43:03.256
21368	remanufatura	\N	INSERT	\N	{"id_remanufatura":1229,"fk_pedido_id":null,"fk_casco_id":9,"valor_unitario":null,"data_cadastro":"2019-10-16","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-16 21:43:03.256
21369	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2533,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2533,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 21:43:03.256
21370	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1229, "simular": true},"id_requisicao":2534,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 21:43:03.365
21371	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1229, "simular": true},"id_requisicao":2534,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1229, "simular": true},"id_requisicao":2534,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 21:43:03.365
21373	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "13", "quantidade": "1", "realizar": false},"id_requisicao":2536,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:01.53
21374	remanufatura	\N	INSERT	\N	{"id_remanufatura":1230,"fk_pedido_id":null,"fk_casco_id":9,"valor_unitario":null,"data_cadastro":"2019-10-16","fk_insumo_id":13,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-16 22:17:01.53
21375	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "13", "quantidade": "1", "realizar": false},"id_requisicao":2536,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "13", "quantidade": "1", "realizar": false},"id_requisicao":2536,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:01.53
21377	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2538,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:10.14
21378	remanufatura	\N	INSERT	\N	{"id_remanufatura":1231,"fk_pedido_id":null,"fk_casco_id":9,"valor_unitario":null,"data_cadastro":"2019-10-16","fk_insumo_id":10,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-10-16 22:17:10.14
21379	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2538,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false},"id_requisicao":2538,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:10.14
21380	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1231, "simular": true},"id_requisicao":2539,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:10.142
21381	requisicao	\N	UPDATE	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1231, "simular": true},"id_requisicao":2539,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_realizar_remanufatura","params_json":{"remanufatura_id": 1231, "simular": true},"id_requisicao":2539,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:10.142
21382	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[]"},"id_requisicao":2540,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:21.943
21383	requisicao	\N	UPDATE	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[]"},"id_requisicao":2540,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_delete_remanufatura","params_json":{"remanufatura_id": "[]"},"id_requisicao":2540,"retorno":"100","data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:17:21.943
21384	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2541,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:35:59.771
21385	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ENCERRADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ESTORNADO"}	soadmin	2019-10-16 22:35:59.771
21386	item_lote	\N	DELETE	{"id_item_lote":5267,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21387	item_lote	\N	DELETE	{"id_item_lote":5268,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21388	item_lote	\N	DELETE	{"id_item_lote":5269,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21389	item_lote	\N	DELETE	{"id_item_lote":5270,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21390	item_lote	\N	DELETE	{"id_item_lote":5271,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21391	item_lote	\N	DELETE	{"id_item_lote":5272,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21392	item_lote	\N	DELETE	{"id_item_lote":5273,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21393	item_lote	\N	DELETE	{"id_item_lote":5274,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21394	item_lote	\N	DELETE	{"id_item_lote":5275,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21395	item_lote	\N	DELETE	{"id_item_lote":5276,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21396	item_lote	\N	DELETE	{"id_item_lote":5277,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21397	item_lote	\N	DELETE	{"id_item_lote":5278,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21398	item_lote	\N	DELETE	{"id_item_lote":5279,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21399	item_lote	\N	DELETE	{"id_item_lote":5280,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21400	item_lote	\N	DELETE	{"id_item_lote":5281,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21401	item_lote	\N	DELETE	{"id_item_lote":5282,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21402	item_lote	\N	DELETE	{"id_item_lote":5283,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21403	item_lote	\N	DELETE	{"id_item_lote":5284,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21404	item_lote	\N	DELETE	{"id_item_lote":5285,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21405	item_lote	\N	DELETE	{"id_item_lote":5286,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21406	item_lote	\N	DELETE	{"id_item_lote":5287,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21407	item_lote	\N	DELETE	{"id_item_lote":5288,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21408	item_lote	\N	DELETE	{"id_item_lote":5289,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21409	item_lote	\N	DELETE	{"id_item_lote":5290,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21410	item_lote	\N	DELETE	{"id_item_lote":5291,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21411	item_lote	\N	DELETE	{"id_item_lote":5292,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21412	item_lote	\N	DELETE	{"id_item_lote":5293,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21413	item_lote	\N	DELETE	{"id_item_lote":5294,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21414	item_lote	\N	DELETE	{"id_item_lote":5295,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21415	item_lote	\N	DELETE	{"id_item_lote":5296,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21416	item_lote	\N	DELETE	{"id_item_lote":5297,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21417	item_lote	\N	DELETE	{"id_item_lote":5298,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21418	item_lote	\N	DELETE	{"id_item_lote":5299,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21419	item_lote	\N	DELETE	{"id_item_lote":5300,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21420	item_lote	\N	DELETE	{"id_item_lote":5301,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21421	item_lote	\N	DELETE	{"id_item_lote":5302,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21422	item_lote	\N	DELETE	{"id_item_lote":5303,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21423	item_lote	\N	DELETE	{"id_item_lote":5304,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21424	item_lote	\N	DELETE	{"id_item_lote":5305,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21425	item_lote	\N	DELETE	{"id_item_lote":5306,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21426	item_lote	\N	DELETE	{"id_item_lote":5307,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21427	item_lote	\N	DELETE	{"id_item_lote":5308,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21428	item_lote	\N	DELETE	{"id_item_lote":5309,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21429	item_lote	\N	DELETE	{"id_item_lote":5310,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21430	item_lote	\N	DELETE	{"id_item_lote":5311,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21431	item_lote	\N	DELETE	{"id_item_lote":5262,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21432	item_lote	\N	DELETE	{"id_item_lote":5263,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21433	item_lote	\N	DELETE	{"id_item_lote":5264,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21434	item_lote	\N	DELETE	{"id_item_lote":5265,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21435	item_lote	\N	DELETE	{"id_item_lote":5266,"fk_lote_id":211,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-02","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:35:59.771
21436	lote	\N	DELETE	{"id_lote":211,"fk_pedido_id":448,"data_cadastro":"2019-10-02","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 22:35:59.771
21437	requisicao	\N	UPDATE	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2541,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2541,"retorno":"100","data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:35:59.771
21442	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2544,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:44:22.335
21443	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 22:44:22.335
21444	item_pedido	\N	UPDATE	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 22:44:22.335
21445	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2544,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2544,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:44:22.335
21446	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2545,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:44:47.407
21447	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 22:44:47.407
21448	item_pedido	\N	UPDATE	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 22:44:47.407
21449	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2545,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2545,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:44:47.407
21450	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2546,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:46:09.025
21451	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 22:46:09.025
21452	item_pedido	\N	UPDATE	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 22:46:09.025
21453	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2546,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2546,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:46:09.025
21454	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2547,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:46:16.08
21455	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ENCERRADO"}	soadmin	2019-10-16 22:46:16.08
21456	lote	\N	INSERT	\N	{"id_lote":212,"fk_pedido_id":448,"data_cadastro":"2019-10-16","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 22:46:16.08
21457	item_lote	\N	INSERT	\N	{"id_item_lote":5312,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21458	item_lote	\N	INSERT	\N	{"id_item_lote":5313,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21459	item_lote	\N	INSERT	\N	{"id_item_lote":5314,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21460	item_lote	\N	INSERT	\N	{"id_item_lote":5315,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21461	item_lote	\N	INSERT	\N	{"id_item_lote":5316,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21462	item_lote	\N	INSERT	\N	{"id_item_lote":5317,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21463	item_lote	\N	INSERT	\N	{"id_item_lote":5318,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21464	item_lote	\N	INSERT	\N	{"id_item_lote":5319,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21465	item_lote	\N	INSERT	\N	{"id_item_lote":5320,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21466	item_lote	\N	INSERT	\N	{"id_item_lote":5321,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21467	item_lote	\N	INSERT	\N	{"id_item_lote":5322,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21468	item_lote	\N	INSERT	\N	{"id_item_lote":5323,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21469	item_lote	\N	INSERT	\N	{"id_item_lote":5324,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21470	item_lote	\N	INSERT	\N	{"id_item_lote":5325,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21471	item_lote	\N	INSERT	\N	{"id_item_lote":5326,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21472	item_lote	\N	INSERT	\N	{"id_item_lote":5327,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21473	item_lote	\N	INSERT	\N	{"id_item_lote":5328,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21474	item_lote	\N	INSERT	\N	{"id_item_lote":5329,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21475	item_lote	\N	INSERT	\N	{"id_item_lote":5330,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21476	item_lote	\N	INSERT	\N	{"id_item_lote":5331,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21477	item_lote	\N	INSERT	\N	{"id_item_lote":5332,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21478	item_lote	\N	INSERT	\N	{"id_item_lote":5333,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21479	item_lote	\N	INSERT	\N	{"id_item_lote":5334,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21480	item_lote	\N	INSERT	\N	{"id_item_lote":5335,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21481	item_lote	\N	INSERT	\N	{"id_item_lote":5336,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21482	item_lote	\N	INSERT	\N	{"id_item_lote":5337,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21483	item_lote	\N	INSERT	\N	{"id_item_lote":5338,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21484	item_lote	\N	INSERT	\N	{"id_item_lote":5339,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21485	item_lote	\N	INSERT	\N	{"id_item_lote":5340,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21486	item_lote	\N	INSERT	\N	{"id_item_lote":5341,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21487	item_lote	\N	INSERT	\N	{"id_item_lote":5342,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21488	item_lote	\N	INSERT	\N	{"id_item_lote":5343,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21489	item_lote	\N	INSERT	\N	{"id_item_lote":5344,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21490	item_lote	\N	INSERT	\N	{"id_item_lote":5345,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21491	item_lote	\N	INSERT	\N	{"id_item_lote":5346,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21492	item_lote	\N	INSERT	\N	{"id_item_lote":5347,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21493	item_lote	\N	INSERT	\N	{"id_item_lote":5348,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21494	item_lote	\N	INSERT	\N	{"id_item_lote":5349,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21495	item_lote	\N	INSERT	\N	{"id_item_lote":5350,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21496	item_lote	\N	INSERT	\N	{"id_item_lote":5351,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21497	item_lote	\N	INSERT	\N	{"id_item_lote":5352,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21498	item_lote	\N	INSERT	\N	{"id_item_lote":5353,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21499	item_lote	\N	INSERT	\N	{"id_item_lote":5354,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21500	item_lote	\N	INSERT	\N	{"id_item_lote":5355,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21501	item_lote	\N	INSERT	\N	{"id_item_lote":5356,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21502	item_lote	\N	INSERT	\N	{"id_item_lote":5357,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21503	item_lote	\N	INSERT	\N	{"id_item_lote":5358,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21504	item_lote	\N	INSERT	\N	{"id_item_lote":5359,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21505	item_lote	\N	INSERT	\N	{"id_item_lote":5360,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21506	item_lote	\N	INSERT	\N	{"id_item_lote":5361,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	soadmin	2019-10-16 22:46:16.08
21507	requisicao	\N	UPDATE	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2547,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_encerrar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2547,"retorno":"100","data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:46:16.08
21508	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2548,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:50:13.943
21509	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ENCERRADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 22:50:13.943
21510	item_lote	\N	DELETE	{"id_item_lote":5312,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21511	item_lote	\N	DELETE	{"id_item_lote":5313,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21512	item_lote	\N	DELETE	{"id_item_lote":5314,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21513	item_lote	\N	DELETE	{"id_item_lote":5315,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21514	item_lote	\N	DELETE	{"id_item_lote":5316,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21515	item_lote	\N	DELETE	{"id_item_lote":5317,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21516	item_lote	\N	DELETE	{"id_item_lote":5318,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21517	item_lote	\N	DELETE	{"id_item_lote":5319,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21518	item_lote	\N	DELETE	{"id_item_lote":5320,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21519	item_lote	\N	DELETE	{"id_item_lote":5321,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21520	item_lote	\N	DELETE	{"id_item_lote":5322,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21521	item_lote	\N	DELETE	{"id_item_lote":5323,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21522	item_lote	\N	DELETE	{"id_item_lote":5324,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21523	item_lote	\N	DELETE	{"id_item_lote":5325,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21524	item_lote	\N	DELETE	{"id_item_lote":5326,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21525	item_lote	\N	DELETE	{"id_item_lote":5327,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21526	item_lote	\N	DELETE	{"id_item_lote":5328,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21527	item_lote	\N	DELETE	{"id_item_lote":5329,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21528	item_lote	\N	DELETE	{"id_item_lote":5330,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21529	item_lote	\N	DELETE	{"id_item_lote":5331,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21530	item_lote	\N	DELETE	{"id_item_lote":5332,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21531	item_lote	\N	DELETE	{"id_item_lote":5333,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21532	item_lote	\N	DELETE	{"id_item_lote":5334,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21533	item_lote	\N	DELETE	{"id_item_lote":5335,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21534	item_lote	\N	DELETE	{"id_item_lote":5336,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21535	item_lote	\N	DELETE	{"id_item_lote":5337,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21536	item_lote	\N	DELETE	{"id_item_lote":5338,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21537	item_lote	\N	DELETE	{"id_item_lote":5339,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21538	item_lote	\N	DELETE	{"id_item_lote":5340,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21539	item_lote	\N	DELETE	{"id_item_lote":5341,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21540	item_lote	\N	DELETE	{"id_item_lote":5342,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21541	item_lote	\N	DELETE	{"id_item_lote":5343,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21542	item_lote	\N	DELETE	{"id_item_lote":5344,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21543	item_lote	\N	DELETE	{"id_item_lote":5345,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21544	item_lote	\N	DELETE	{"id_item_lote":5346,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21545	item_lote	\N	DELETE	{"id_item_lote":5347,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21546	item_lote	\N	DELETE	{"id_item_lote":5348,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21547	item_lote	\N	DELETE	{"id_item_lote":5349,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21548	item_lote	\N	DELETE	{"id_item_lote":5350,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21549	item_lote	\N	DELETE	{"id_item_lote":5351,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21550	item_lote	\N	DELETE	{"id_item_lote":5352,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21551	item_lote	\N	DELETE	{"id_item_lote":5353,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21552	item_lote	\N	DELETE	{"id_item_lote":5354,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21553	item_lote	\N	DELETE	{"id_item_lote":5355,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21554	item_lote	\N	DELETE	{"id_item_lote":5356,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21555	item_lote	\N	DELETE	{"id_item_lote":5357,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21556	item_lote	\N	DELETE	{"id_item_lote":5358,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21557	item_lote	\N	DELETE	{"id_item_lote":5359,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21558	item_lote	\N	DELETE	{"id_item_lote":5360,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21559	item_lote	\N	DELETE	{"id_item_lote":5361,"fk_lote_id":212,"fk_item_pedido_saida_id":null,"data_validade":null,"lote_fabricante":null,"data_retirada":null,"motivo_retirada":null,"quantidade_item":1,"fk_item_pedido_entrada_id":495,"data_cadastro":"2019-10-16","aberto":false,"data_abertura":null,"motivo_abertura":null}	\N	soadmin	2019-10-16 22:50:13.943
21560	lote	\N	DELETE	{"id_lote":212,"fk_pedido_id":448,"data_cadastro":"2019-10-16","vazio":false,"observacao":null,"fk_mercadoria_id":51,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 22:50:13.943
21561	requisicao	\N	UPDATE	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2548,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_estornar_pedido","params_json":{"pedido_id": "448"},"id_requisicao":2548,"retorno":"100","data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:50:13.943
21562	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2549,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:50:25.813
21563	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 22:50:25.813
21564	item_pedido	\N	UPDATE	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 22:50:25.813
21565	item_pedido	\N	INSERT	\N	{"id_item_pedido":497,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 22:50:25.813
21566	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2549,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2549,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:50:25.813
21577	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2554,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:55:09.474
21578	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 22:55:09.474
21579	item_pedido	\N	UPDATE	{"id_item_pedido":497,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_item_pedido":497,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 22:55:09.474
21580	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2554,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2554,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 22:55:09.474
21593	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2559,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:03:12.872
21594	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:03:12.872
21595	item_pedido	\N	UPDATE	{"id_item_pedido":497,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	{"id_item_pedido":497,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:03:12.872
21596	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2559,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2559,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:03:12.872
21597	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2560,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:10:52.65
21598	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:10:52.65
21599	item_pedido	\N	DELETE	{"id_item_pedido":497,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:10:52.65
21600	item_pedido	\N	INSERT	\N	{"id_item_pedido":498,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:10:52.65
21601	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2560,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2560,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:10:52.65
21602	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 498, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2561,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:11:19.794
21603	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:11:19.794
21604	item_pedido	\N	DELETE	{"id_item_pedido":498,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:11:19.794
21605	item_pedido	\N	INSERT	\N	{"id_item_pedido":499,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:11:19.794
21606	item_pedido	\N	DELETE	{"id_item_pedido":495,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:11:19.794
21607	item_pedido	\N	INSERT	\N	{"id_item_pedido":500,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:11:19.794
21608	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 498, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2561,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 498, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2561,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:11:19.794
21609	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 500, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 499, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2562,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:13:25.692
21610	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:13:25.692
21611	item_pedido	\N	DELETE	{"id_item_pedido":500,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:13:25.692
21612	item_pedido	\N	INSERT	\N	{"id_item_pedido":501,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:13:25.692
21613	item_pedido	\N	DELETE	{"id_item_pedido":499,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:13:25.692
21614	item_pedido	\N	INSERT	\N	{"id_item_pedido":502,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:13:25.692
21615	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 500, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 499, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2562,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 500, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 499, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2562,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:13:25.692
21616	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2563,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:14:03.443
21617	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:14:03.443
21618	item_pedido	\N	INSERT	\N	{"id_item_pedido":503,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:14:03.443
21619	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2563,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2563,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:14:03.443
21638	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 506, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2569,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:20:36.643
21639	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:20:36.643
21620	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2564,"retorno":null,"data_requisicao":"2019-10-16","usuario":"postgres","mensagem":null}	postgres	2019-10-16 23:15:19.11
21621	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	postgres	2019-10-16 23:15:19.11
21622	item_pedido	\N	INSERT	\N	{"id_item_pedido":504,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	postgres	2019-10-16 23:15:19.11
21623	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2564,"retorno":null,"data_requisicao":"2019-10-16","usuario":"postgres","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2564,"retorno":null,"data_requisicao":"2019-10-16","usuario":"postgres","mensagem":null}	postgres	2019-10-16 23:15:19.11
21630	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2568,"retorno":null,"data_requisicao":"2019-10-16","usuario":"postgres","mensagem":null}	postgres	2019-10-16 23:19:34.357
21631	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	postgres	2019-10-16 23:19:34.357
21632	item_pedido	\N	DELETE	{"id_item_pedido":501,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":50,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	postgres	2019-10-16 23:19:34.357
21633	item_pedido	\N	DELETE	{"id_item_pedido":502,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":3,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	postgres	2019-10-16 23:19:34.357
21634	item_pedido	\N	DELETE	{"id_item_pedido":503,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	\N	postgres	2019-10-16 23:19:34.357
21635	item_pedido	\N	DELETE	{"id_item_pedido":504,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	\N	postgres	2019-10-16 23:19:34.357
21636	item_pedido	\N	INSERT	\N	{"id_item_pedido":506,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	postgres	2019-10-16 23:19:34.357
21637	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2568,"retorno":null,"data_requisicao":"2019-10-16","usuario":"postgres","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2568,"retorno":null,"data_requisicao":"2019-10-16","usuario":"postgres","mensagem":null}	postgres	2019-10-16 23:19:34.357
21640	item_pedido	\N	DELETE	{"id_item_pedido":506,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:20:36.643
21641	item_pedido	\N	INSERT	\N	{"id_item_pedido":507,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:20:36.643
21642	item_pedido	\N	DELETE	{"id_item_pedido":507,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:20:36.643
21643	item_pedido	\N	INSERT	\N	{"id_item_pedido":508,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:20:36.643
21644	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 506, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2569,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 506, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2569,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:20:36.643
21645	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 508, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 10, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2570,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:21:23.243
21646	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:21:23.243
21647	item_pedido	\N	DELETE	{"id_item_pedido":508,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:21:23.243
21648	item_pedido	\N	INSERT	\N	{"id_item_pedido":509,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":10,"valor_unitario":1,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:21:23.243
21649	item_pedido	\N	DELETE	{"id_item_pedido":509,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":10,"valor_unitario":1,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:21:23.243
21650	item_pedido	\N	INSERT	\N	{"id_item_pedido":510,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:21:23.243
21651	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 508, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 10, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2570,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 508, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 10, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2570,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:21:23.243
21652	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 510, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]},"id_requisicao":2571,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:33:57.357
21653	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:33:57.357
21654	item_pedido	\N	DELETE	{"id_item_pedido":510,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:33:57.357
21655	item_pedido	\N	INSERT	\N	{"id_item_pedido":511,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:33:57.357
21656	item_pedido	\N	DELETE	{"id_item_pedido":511,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:33:57.357
21657	item_pedido	\N	INSERT	\N	{"id_item_pedido":512,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:33:57.357
21658	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 510, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]},"id_requisicao":2571,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 510, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]},"id_requisicao":2571,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:33:57.357
21659	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 512, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]},"id_requisicao":2572,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:36:05.348
21660	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:36:05.348
21661	item_pedido	\N	DELETE	{"id_item_pedido":512,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:36:05.348
21662	item_pedido	\N	INSERT	\N	{"id_item_pedido":513,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:36:05.348
21663	item_pedido	\N	DELETE	{"id_item_pedido":513,"fk_pedido_id":448,"fk_mercadoria_id":38,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:36:05.348
21664	item_pedido	\N	INSERT	\N	{"id_item_pedido":514,"fk_pedido_id":448,"fk_mercadoria_id":35,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:36:05.348
21665	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 512, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]},"id_requisicao":2572,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 512, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]},"id_requisicao":2572,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:36:05.348
21666	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 514, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2573,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:37:39.458
21667	item_pedido	\N	DELETE	{"id_item_pedido":514,"fk_pedido_id":448,"fk_mercadoria_id":35,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:37:39.458
21668	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:37:39.458
21669	item_pedido	\N	INSERT	\N	{"id_item_pedido":515,"fk_pedido_id":448,"fk_mercadoria_id":35,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:37:39.458
21670	item_pedido	\N	INSERT	\N	{"id_item_pedido":516,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:37:39.458
21671	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 514, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2573,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 514, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]},"id_requisicao":2573,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:37:39.458
21672	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2574,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:44:45.824
21673	item_pedido	\N	DELETE	{"id_item_pedido":515,"fk_pedido_id":448,"fk_mercadoria_id":35,"quantidade":1,"valor_unitario":0,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:44:45.824
21674	item_pedido	\N	DELETE	{"id_item_pedido":516,"fk_pedido_id":448,"fk_mercadoria_id":51,"quantidade":1,"valor_unitario":23,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:44:45.824
21675	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:44:45.824
21676	item_pedido	\N	INSERT	\N	{"id_item_pedido":517,"fk_pedido_id":448,"fk_mercadoria_id":36,"quantidade":11,"valor_unitario":1,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:44:45.824
21677	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2574,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2574,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:44:45.824
21678	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 517, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2575,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:45:25.07
21679	item_pedido	\N	DELETE	{"id_item_pedido":517,"fk_pedido_id":448,"fk_mercadoria_id":36,"quantidade":11,"valor_unitario":1,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:45:25.07
21680	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:45:25.07
21681	item_pedido	\N	INSERT	\N	{"id_item_pedido":518,"fk_pedido_id":448,"fk_mercadoria_id":36,"quantidade":11,"valor_unitario":0,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:45:25.07
21682	item_pedido	\N	INSERT	\N	{"id_item_pedido":519,"fk_pedido_id":448,"fk_mercadoria_id":36,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:45:25.07
21683	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 517, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2575,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 517, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2575,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:45:25.07
21690	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 519, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2577,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:47:11.056
21691	item_pedido	\N	DELETE	{"id_item_pedido":518,"fk_pedido_id":448,"fk_mercadoria_id":36,"quantidade":11,"valor_unitario":0,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:47:11.056
21692	item_pedido	\N	DELETE	{"id_item_pedido":519,"fk_pedido_id":448,"fk_mercadoria_id":36,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	\N	soadmin	2019-10-16 23:47:11.056
21693	pedido	\N	UPDATE	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	{"id_pedido":448,"fk_pessoa_id":316,"data_entrega":null,"tipo_pedido":"COMPRA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":"\\t","situacao":"ESTORNADO"}	soadmin	2019-10-16 23:47:11.056
21694	item_pedido	\N	INSERT	\N	{"id_item_pedido":522,"fk_pedido_id":448,"fk_mercadoria_id":36,"quantidade":1,"valor_unitario":1,"fk_unidade_medida_id":276}	soadmin	2019-10-16 23:47:11.056
21695	requisicao	\N	UPDATE	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 519, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2577,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_cadastro_pedido","params_json":{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 519, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]},"id_requisicao":2577,"retorno":null,"data_requisicao":"2019-10-16","usuario":"soadmin","mensagem":null}	soadmin	2019-10-16 23:47:11.056
21696	requisicao	\N	INSERT	\N	{"metodo":"soad.prc_cancelar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2578,"retorno":null,"data_requisicao":"2019-10-17","usuario":"soadmin","mensagem":null}	soadmin	2019-10-17 00:03:40.903
21697	pedido	\N	UPDATE	{"id_pedido":449,"fk_pessoa_id":321,"data_entrega":null,"tipo_pedido":"VENDA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"ESTORNADO"}	{"id_pedido":449,"fk_pessoa_id":321,"data_entrega":null,"tipo_pedido":"VENDA","data_cadastro":"2019-10-02T00:00:00-03:00","observacao":null,"situacao":"CANCELADO"}	soadmin	2019-10-17 00:03:40.903
21698	requisicao	\N	UPDATE	{"metodo":"soad.prc_cancelar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2578,"retorno":null,"data_requisicao":"2019-10-17","usuario":"soadmin","mensagem":null}	{"metodo":"soad.prc_cancelar_pedido","params_json":{"pedido_id": "449"},"id_requisicao":2578,"retorno":"100","data_requisicao":"2019-10-17","usuario":"soadmin","mensagem":null}	soadmin	2019-10-17 00:03:40.903
21104	requisicao	\N	INSERT	\N	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "7", "insumo_id": "15", "quantidade": "1", "realizar": false},"id_requisicao":2480,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:14:51.946
21105	remanufatura	\N	INSERT	\N	{"id_remanufatura":1214,"fk_pedido_id":null,"fk_casco_id":7,"valor_unitario":null,"data_cadastro":"2019-09-28","fk_insumo_id":15,"situacao":"CADASTRADA","codigo":null}	soadmin	2019-09-28 13:14:51.946
21106	requisicao	\N	UPDATE	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "7", "insumo_id": "15", "quantidade": "1", "realizar": false},"id_requisicao":2480,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	{"metodo":"soad.fnc_gerar_remanufatura","params_json":{"casco_id": "7", "insumo_id": "15", "quantidade": "1", "realizar": false},"id_requisicao":2480,"retorno":null,"data_requisicao":"2019-09-28","usuario":"soadmin","mensagem":null}	soadmin	2019-09-28 13:14:51.946
\.


--
-- TOC entry 3267 (class 0 OID 116259)
-- Dependencies: 214
-- Data for Name: mercadoria; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.mercadoria (id_mercadoria, descricao, marca, ativo, data_cadastro, permite_venda, valor_venda, codigo) FROM stdin;
36	STATIC CONTROL YELLOW	STATIC CONTROL	t	2019-09-19	f	0	SCYE
35	STATIC CONTROL CYAN	STATIC CONTROL	t	2019-09-19	f	0	SCCY
37	STATIC CONTROL MAGENTA	STATIC CONTROL	t	2019-09-19	f	0	SCMA
38	HIGH FUSION HF 2025 HP	HIGH FUSION	t	2019-09-19	f	0	HF2025
39	STATIC CONTROL BLACK	HIGH FUSION	t	2019-09-19	f	0	SCBK
40	HIGH FUSION UNIVERSAL SAMSUNG	HIGH FUSION	t	2019-09-19	f	0	HFUSAM
41	CARTUCHO HP 614 C/ CASCO	HP	t	2019-09-19	t	18	HP614CC
42	TONER SAMSUNG 1610 B/ TROCA	SAMSUNG	t	2019-09-19	t	55	SAM1610BT
43	TONER SAMSUNG D205 B/ TROCA	SAMSUNG	t	2019-09-19	t	150	SAMD205BT
44	TONER SAMSUNG ML 101 B/ TROCA	SAMSUNG	t	2019-09-19	f	0	SAMML101BT
45	TONER HP 6002 AMARELO B/ TROCA	HP	t	2019-09-19	f	0	HP6002AMBT
46	CARTUCHO HP 22	HP	t	2019-09-19	t	23	HP22
48	CARTUCHO HP 614	HP	t	2019-09-19	t	45	HP614
49	CARTUCHO LEX 26	LEXMARK	t	2019-09-19	t	45	LEX26
50	CARTUCHO HP 92	HP	t	2019-09-19	t	18	HP92
51	CARTUCHO HP 21	HP	t	2019-09-19	t	23	HP21
47	CARTUCHO HP 27	HP	t	2019-09-19	t	45	HP27
53	CARTUCHO HP 26	HP	t	2019-09-19	t	23	HP26
\.


--
-- TOC entry 3290 (class 0 OID 116337)
-- Dependencies: 237
-- Data for Name: unidade_medida; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.unidade_medida (id_unidade_medida, descricao, abreviacao) FROM stdin;
107	MILIGRAMA	mg
276	UNIDADE	un
105	KILOGRAMA	kg
283	GRAMA	g
106	LITRO	l
108	MILILITRO	ml
\.


--
-- TOC entry 3257 (class 0 OID 116221)
-- Dependencies: 204
-- Data for Name: insumo; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.insumo (id_insumo, fk_mercadoria_id, quantidade_embalagem, fk_unidade_medida_id, colorido) FROM stdin;
11	36	0	105	t
10	35	0	105	t
12	37	0	105	t
13	38	0	105	f
14	39	0	105	f
15	40	0	105	f
\.


--
-- TOC entry 3252 (class 0 OID 116205)
-- Dependencies: 199
-- Data for Name: casco; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.casco (id_casco, fk_insumo_id, fk_mercadoria_id, quantidade_insumo, fk_unidade_medida_insumo, tipo_casco) FROM stdin;
5	14	41	20	107	TONER
6	15	42	20	107	TONER
7	15	43	50	107	TONER
8	15	44	50	107	TONER
9	13	45	50	107	TONER
\.


--
-- TOC entry 3274 (class 0 OID 116281)
-- Dependencies: 221
-- Data for Name: pais; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.pais (id_pais, nome, sigla) FROM stdin;
56	BRASIL	BR
\.


--
-- TOC entry 3255 (class 0 OID 116216)
-- Dependencies: 202
-- Data for Name: estado; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.estado (id_estado, fk_pais_id, nome, sigla) FROM stdin;
546	56	ACRE	AC
547	56	ALAGOAS	AL
548	56	AMAPÁ	AP
549	56	AMAZONAS	AM
550	56	BAHIA	BA
551	56	CEARÁ	CE
552	56	DISTRITO FEDERAL	DF
553	56	ESPÍRITO SANTO	ES
554	56	GOIÁS	GO
555	56	MARANHÃO	MA
556	56	MATO GROSSO	MT
557	56	MATO GROSSO DO SUL	MS
558	56	MINAS GERAIS	MG
559	56	PARÁ	PA
560	56	PARAÍBA	PB
561	56	PARANÁ	PR
562	56	PERNAMBUCO	PE
563	56	PIAUÍ	PI
564	56	RIO DE JANEIRO	RJ
565	56	RIO GRANDE DO NORTE	RN
566	56	RIO GRANDE DO SUL	RS
567	56	RONDÔNIA	RO
568	56	RORAIMA	RR
569	56	SANTA CATARINA	SC
570	56	SÃO PAULO	SP
571	56	SERGIPE	SE
572	56	TOCANTINS	TO
\.


--
-- TOC entry 3272 (class 0 OID 116276)
-- Dependencies: 219
-- Data for Name: municipio; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.municipio (id_municipio, fk_estado_id, nome, cod_ibge) FROM stdin;
34	561	PONTA GROSSA	\N
35	561	CURITIBA	\N
36	561	CASTRO	\N
37	564	RIO DE JANEIRO	\N
38	552	BRASÍLIA	\N
39	570	SÃO PAULO	\N
\.


--
-- TOC entry 3278 (class 0 OID 116294)
-- Dependencies: 225
-- Data for Name: pessoa; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.pessoa (id_pessoa, nome, email, telefone, data_cadastro, inscricao_estadual) FROM stdin;
313	A.P.F. DO CMEI DRº GABRIEL BACILA	\N	\N	2019-09-19	ISENTO
314	ASSOCIAÇÃO DOS SERVIDORES PUBLICOS MUNICIPAIS DE PONTA GROSSA	\N	4232244177	2019-09-19	ISENTO
315	BIANCA MARIA LAMOGLIA	\N	4230251468	2019-09-19	ISENTO
316	POTENCIAL SUPRIMENTOS DE INFORMATICA LTDA	\N	4432675555	2019-09-19	9.032.598.509
317	DGX DISTRIBURIDORA	\N	1121725202	2019-09-19	142.764.046.110
318	MICROL INFORMATICA LTDA	\N	4133491286	2019-09-19	ISENTO
319	NEIDE SABARIEGO-ME	\N	4132052051	2019-09-19	90.743293-97
320	SUZANO PAPEL E CELULOSE S.A	\N	1130379000	2019-09-19	90.790.569-17
321	Idomar Augusto	idomar@uepg.br	42999823030	2019-10-02	ISENTO
311	FUNDEPAR/COLÉGIO ESTADUAL JOSÉ ELIAS DA ROCHA/FUNDO ROTATIVO	\N	4232241451	2019-09-19	ISENTO
312	A C PEREIRA - INFORMATICA EIRELI	\N	\N	2019-09-19	ISENTO
\.


--
-- TOC entry 3253 (class 0 OID 116210)
-- Dependencies: 200
-- Data for Name: endereco; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.endereco (id_endereco, fk_municipio_id, fk_pessoa_id, logradouro, numero, bairro, cep, complemento, tipo) FROM stdin;
59	34	314	R MARQUES DO PARANA	00000	RONDA	84051060		COMERCIAL
60	34	315	R CASTANHEIRA	00000	CONTORNO	84061370		COMERCIAL
61	35	316	RUA RODOLFO CREMM	6650	JARDIM ANDRADE	87035480		COMERCIAL
62	39	317	RUA ALFREDO MAIA	433	LUZ	01106010		COMERCIAL
63	34	318	RUA CYRO PEREIRA	667	CIC	81170230		COMERCIAL
64	34	319	RUA CORONEL OSCAR RODRIGUES	70	S\\u00c3O BRAZ	8230057		COMERCIAL
65	35	320	AV THOMA CARMEL	1600	GATUP\\\\u00ca	83060000		COMERCIAL
58	34	313	PROFESSOR PLACIDO CARDON	00000	CONTORNO	84060290		COMERCIAL
66	34	321	Rua Padre jos\\\\u00e9 da Silva	123	Jardim Nova R\\\\u00fassia	84031029	Pr\\\\u00f3ximo ao mercadinho do seu z\\\\u00e9	COMERCIAL
56	34	311	RUA RICARDO WAGNER	200	OLARIAS	84035220		COMERCIAL
57	34	312	RUA ABELIO BENATTI	00000	JARDIM SOL	84072000		COMERCIAL
\.


--
-- TOC entry 3276 (class 0 OID 116286)
-- Dependencies: 223
-- Data for Name: pedido; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.pedido (id_pedido, fk_pessoa_id, data_entrega, tipo_pedido, data_cadastro, observacao, situacao) FROM stdin;
443	317	\N	COMPRA	2019-09-19 00:00:00-03	\N	ENCERRADO
444	312	\N	VENDA	2019-09-19 00:00:00-03	\N	CANCELADO
445	313	\N	VENDA	2019-09-19 00:00:00-03	\N	ENCERRADO
446	312	\N	VENDA	2019-09-19 00:00:00-03	\N	CANCELADO
447	316	\N	COMPRA	2019-09-19 00:00:00-03	\N	ENCERRADO
448	316	\N	COMPRA	2019-10-02 00:00:00-03	\t	ESTORNADO
449	321	\N	VENDA	2019-10-02 00:00:00-03	\N	CANCELADO
\.


--
-- TOC entry 3263 (class 0 OID 116241)
-- Dependencies: 210
-- Data for Name: item_pedido; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.item_pedido (id_item_pedido, fk_pedido_id, fk_mercadoria_id, quantidade, valor_unitario, fk_unidade_medida_id) FROM stdin;
488	443	49	50	45	276
489	444	49	5	45	276
490	445	49	10	45	276
491	447	35	20	45	276
492	447	36	20	30	276
493	447	37	23	10	276
494	447	43	20	150	276
496	449	51	5	23	276
522	448	36	1	1	276
\.


--
-- TOC entry 3265 (class 0 OID 116249)
-- Dependencies: 212
-- Data for Name: lote; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.lote (id_lote, fk_pedido_id, data_cadastro, vazio, observacao, fk_mercadoria_id, valor_unitario, fk_unidade_medida_id) FROM stdin;
209	447	2019-09-19	f	\N	37	10	276
210	447	2019-09-19	f	\N	43	150	276
208	447	2019-09-19	f	\N	36	30	276
206	443	2019-09-19	f	\N	49	45	276
207	447	2019-09-19	f	\N	35	45	276
\.


--
-- TOC entry 3259 (class 0 OID 116227)
-- Dependencies: 206
-- Data for Name: item_lote; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.item_lote (id_item_lote, fk_lote_id, fk_item_pedido_saida_id, data_validade, lote_fabricante, data_retirada, motivo_retirada, quantidade_item, fk_item_pedido_entrada_id, data_cadastro, aberto, data_abertura, motivo_abertura) FROM stdin;
5144	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5145	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5146	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5147	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5148	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5149	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5150	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5151	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5152	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5153	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5154	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5155	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5156	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5157	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5158	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5159	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5160	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5161	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5162	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5163	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5164	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5165	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5166	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5167	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5168	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5169	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5170	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5171	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5172	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5173	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5174	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5175	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5176	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5177	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5178	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5133	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5132	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5131	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5130	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5129	206	\N	\N	\N	\N	\N	1	488	2019-09-19	f	\N	\N
5134	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5135	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5136	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5137	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5138	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5139	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5140	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5141	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5142	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5143	206	490	\N	\N	2019-09-19 03:31:24.1437-03	Pedido 445 Tipo: VENDA	0	488	2019-09-19	f	\N	\N
5182	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5183	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5184	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5185	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5186	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5187	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5188	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5189	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5190	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5191	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5192	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5193	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5194	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5195	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5196	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5197	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5198	207	\N	\N	\N	\N	\N	1	491	2019-09-19	f	\N	\N
5200	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5201	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5202	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5203	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5204	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5205	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5206	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5207	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5208	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5209	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5210	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5211	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5212	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5213	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5214	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5215	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5216	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5217	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5218	208	\N	\N	\N	\N	\N	1	492	2019-09-19	f	\N	\N
5219	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5199	208	\N	\N	\N	2019-09-19 03:48:30.8954-03	Remanufatura (operação interna)\\nItem utilizado (Vazio)	0	492	2019-09-19	t	2019-09-19	Remanufatura (operação interna)
5220	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5221	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5222	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5223	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5224	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5225	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5226	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5227	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5228	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5229	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5230	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5231	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5232	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5233	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5234	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5235	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5236	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5237	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5238	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5239	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5240	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5181	207	\N	\N	\N	2019-10-02 23:22:54.9478-03	\N	0	491	2019-09-19	t	2019-10-02	Remanufatura (operação interna)
5241	209	\N	\N	\N	\N	\N	1	493	2019-09-19	f	\N	\N
5242	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5243	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5244	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5245	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5246	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5247	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5248	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5249	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5250	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5251	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5252	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5253	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5254	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5255	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5256	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5257	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5258	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5259	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5260	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5261	210	\N	\N	\N	\N	\N	1	494	2019-09-19	f	\N	\N
5179	207	\N	\N	\N	2019-09-28 13:16:35.1023-03	\N	0	491	2019-09-19	t	2019-09-28	Remanufatura (operação interna)
5180	207	\N	\N	\N	2019-10-02 23:13:15.1589-03	\N	0	491	2019-09-19	t	2019-10-02	Remanufatura (operação interna)
\.


--
-- TOC entry 3285 (class 0 OID 116314)
-- Dependencies: 232
-- Data for Name: remanufatura; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.remanufatura (id_remanufatura, fk_pedido_id, fk_casco_id, valor_unitario, data_cadastro, fk_insumo_id, situacao, codigo) FROM stdin;
1209	\N	5	0.0000	2019-09-19	14	CANCELADA	\N
1210	\N	5	0.0000	2019-09-19	14	CANCELADA	\N
1211	\N	5	\N	2019-09-19	14	CADASTRADA	\N
1212	\N	6	\N	2019-09-19	11	REALIZADA	000001909191212
1213	\N	6	\N	2019-09-19	11	REALIZADA	000001909191213
1214	\N	7	\N	2019-09-28	15	CADASTRADA	\N
1215	\N	7	\N	2019-09-28	10	REALIZADA	000001909281215
1216	\N	8	\N	2019-10-02	15	CADASTRADA	\N
1218	\N	5	\N	2019-10-02	10	REALIZADA	000001910021218
1219	\N	5	\N	2019-10-02	10	REALIZADA	000001910021219
1220	\N	5	\N	2019-10-02	10	REALIZADA	000001910021220
1221	\N	5	\N	2019-10-02	10	REALIZADA	000001910021221
1222	\N	5	\N	2019-10-02	10	REALIZADA	000001910021222
1223	\N	5	\N	2019-10-02	10	REALIZADA	000001910021223
1227	\N	5	\N	2019-10-02	14	CADASTRADA	\N
1228	\N	9	\N	2019-10-02	10	REALIZADA	000001910021228
1229	\N	9	\N	2019-10-16	10	CADASTRADA	\N
1230	\N	9	\N	2019-10-16	13	CADASTRADA	\N
1231	\N	9	\N	2019-10-16	10	CADASTRADA	\N
\.


--
-- TOC entry 3261 (class 0 OID 116235)
-- Dependencies: 208
-- Data for Name: item_lote_remanufatura; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.item_lote_remanufatura (id_item_lote_remanufatura, fk_remanufatura_id, fk_item_lote_id, data_cadastro) FROM stdin;
249	1212	5199	2019-09-19
250	1213	5199	2019-09-19
251	1215	5179	2019-09-28
252	1218	5180	2019-10-02
253	1219	5180	2019-10-02
254	1220	5180	2019-10-02
255	1221	5180	2019-10-02
256	1222	5180	2019-10-02
257	1223	5181	2019-10-02
258	1228	5181	2019-10-02
\.


--
-- TOC entry 3268 (class 0 OID 116266)
-- Dependencies: 215
-- Data for Name: modalidade; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.modalidade (id_modalidade, descricao) FROM stdin;
57	CLIENTE
58	FORNECEDOR
\.


--
-- TOC entry 3270 (class 0 OID 116271)
-- Dependencies: 217
-- Data for Name: modalidade_pessoa; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.modalidade_pessoa (id_modalidade_pessoa, fk_pessoa_id, fk_modalidade_id) FROM stdin;
166	313	57
167	314	57
168	315	57
169	316	58
170	317	58
171	318	58
172	319	58
174	320	58
179	321	57
180	311	57
181	311	58
182	312	57
183	312	58
\.


--
-- TOC entry 3279 (class 0 OID 116298)
-- Dependencies: 226
-- Data for Name: pessoa_fisica; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.pessoa_fisica (id_pessoa_fisica, fk_pessoa_id, cpf, data_cadastro, rg) FROM stdin;
71	321	11111111111	22:50:51.3388-03	\N
\.


--
-- TOC entry 3282 (class 0 OID 116306)
-- Dependencies: 229
-- Data for Name: pessoa_juridica; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.pessoa_juridica (id_pessoa_juridica, fk_pessoa_id, cnpj, fantasia, data_cadastro) FROM stdin;
155	313	06195377000120	\N	2019-09-19 02:39:46.1161-03
156	314	80254972000141	ASPM	2019-09-19 02:40:59.4976-03
157	315	31423223000195	TOP LIMP	2019-09-19 02:42:13.0499-03
158	316	07152924000152	POTENCIAL	2019-09-19 02:43:23.3997-03
159	317	18810122000109	DGX	2019-09-19 02:44:47.8456-03
160	318	07531617000182	MICROL	2019-09-19 02:45:33.6396-03
161	319	27168508000150	LORIFLEX	2019-09-19 02:46:27.3516-03
162	320	16404287015004	SUZANO	2019-09-19 02:47:57.9016-03
153	311	77741312000180	\N	2019-09-19 02:37:07.5077-03
154	312	02526512000111	PEREIRA & CONCEIÇÃO - INFORMÁTICA	2019-09-19 02:38:34.1097-03
\.


--
-- TOC entry 3287 (class 0 OID 116325)
-- Dependencies: 234
-- Data for Name: requisicao; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.requisicao (metodo, params_json, id_requisicao, retorno, data_requisicao, usuario, mensagem) FROM stdin;
soad.fnc_cadastro_pessoa	{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": []}	2411	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57]}	2412	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "A.P.F. DO CMEI DR\\u00ba GABRIEL BACILA", "documento": "06195377000120", "inscricao_estadual": "ISENTO", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "PROFESSOR PLACIDO CARDON", "numero": "00000", "bairro": "CONTORNO", "cep": "84060290", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]}	2413	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "ASSOCIA\\u00c7\\u00c3O DOS SERVIDORES PUBLICOS MUNICIPAIS DE PONTA GROSSA", "telefone": "4232244177", "documento": "80254972000141", "inscricao_estadual": "ISENTO", "fantasia": "ASPM", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "R MARQUES DO PARANA", "numero": "00000", "bairro": "RONDA", "cep": "84051060", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]}	2414	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "BIANCA MARIA LAMOGLIA", "telefone": "4230251468", "documento": "31423223000195", "inscricao_estadual": "ISENTO", "fantasia": "TOP LIMP", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "R CASTANHEIRA", "numero": "00000", "bairro": "CONTORNO", "cep": "84061370", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]}	2415	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "POTENCIAL SUPRIMENTOS DE INFORMATICA LTDA", "telefone": "4432675555", "documento": "07152924000152", "inscricao_estadual": "9.032.598.509", "fantasia": "POTENCIAL", "endereco": [{"pessoa_id": "", "id_municipio": 35, "logradouro": "RUA RODOLFO CREMM", "numero": "6650", "bairro": "JARDIM ANDRADE", "cep": "87035480", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [58]}	2416	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "DGX DISTRIBURIDORA", "telefone": "1121725202", "documento": "18810122000109", "inscricao_estadual": "142.764.046.110", "fantasia": "DGX", "endereco": [{"pessoa_id": "", "id_municipio": 39, "logradouro": "RUA ALFREDO MAIA", "numero": "433", "bairro": "LUZ", "cep": "01106010", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [58]}	2417	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "MICROL INFORMATICA LTDA", "telefone": "4133491286", "documento": "07531617000182", "fantasia": "MICROL", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "RUA CYRO PEREIRA", "numero": "667", "bairro": "CIC", "cep": "81170230", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [58]}	2418	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "NEIDE SABARIEGO-ME", "telefone": "4132052051", "documento": "27168508000150", "inscricao_estadual": "90.743293-97", "fantasia": "LORIFLEX", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "RUA CORONEL OSCAR RODRIGUES", "numero": "70", "bairro": "S\\u00c3O BRAZ", "cep": "8230057", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [58]}	2419	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "SUZANO PAPEL E CELULOSE S.A", "telefone": "1130379000", "documento": "16404287015004", "inscricao_estadual": "90.790.569-17", "fantasia": "SUZANO", "endereco": [{"pessoa_id": "", "id_municipio": 35, "logradouro": "AV THOMA CARMEL", "numero": "1600", "bairro": "GATUP\\u00ca", "cep": "83060000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [58]}	2421	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "SUZANO PAPEL E CELULOSE S.A", "telefone": "1130379000", "documento": "16404287015004", "inscricao_estadual": "90.790.569-17", "fantasia": "SUZANO", "pessoa_id": "320", "endereco": [{"pessoa_id": "320", "id_municipio": 35, "logradouro": "AV THOMA CARMEL", "numero": "1600", "bairro": "GATUP\\\\u00ca", "cep": "83060000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "65"}], "modalidade": [58]}	2423	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "SCCY", "descricao": "STATIC CONTROL CY", "marca": "STATIC CONTROL", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 107, "colorido": true}	2424	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "SCYE", "descricao": "STATIC CONTROL YELLOW", "marca": "STATIC CONTROL", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 105, "colorido": true}	2425	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"mercadoria_id": 35, "codigo": "SCCY", "descricao": "STATIC CONTROL CYAN", "marca": "STATIC CONTROL", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 107, "colorido": true}	2426	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"mercadoria_id": 35, "codigo": "SCCY", "descricao": "STATIC CONTROL CYAN", "marca": "STATIC CONTROL", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 105, "colorido": true}	2427	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "SCMA", "descricao": "STATIC CONTROL MAGENTA", "marca": "STATIC CONTROL", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 105, "colorido": true}	2428	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HF2025", "descricao": "HIGH FUSION HF 2025 HP", "marca": "HIGH FUSION", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 105, "colorido": true}	2429	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "FUNDEPAR/COL\\u00c9GIO ESTADUAL JOS\\u00c9 ELIAS DA ROCHA/FUNDO ROTATIVO", "telefone": "4232241451", "documento": "77741312000180", "inscricao_estadual": "ISENTO", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "RUA RICARDO WAGNER", "numero": "200", "bairro": "OLARIAS", "cep": "84035220", "complemento": "", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]}	2410	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"mercadoria_id": 38, "codigo": "HF2025", "descricao": "HIGH FUSION HF 2025 HP", "marca": "HIGH FUSION", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 105, "colorido": false}	2430	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "SCBK", "descricao": "STATIC CONTROL BLACK", "marca": "HIGH FUSION", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 105, "colorido": false}	2431	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HFUSAM", "descricao": "HIGH FUSION UNIVERSAL SAMSUNG", "marca": "HIGH FUSION", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "INSUMO", "quantidade": 0.0, "unidade_medida_id": 105, "colorido": false}	2432	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HP614CC", "descricao": "CARTUCHO HP 614 C/ CASCO", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 18.0, "tipo": "CASCO", "insumo_id": 14, "quantidade": 20.0, "unidade_medida_id": 107}	2433	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "SAM1610BT", "descricao": "TONER SAMSUNG 1610 B/ TROCA", "marca": "SAMSUNG", "ativo": true, "permite_venda": true, "valor_venda": 55.0, "tipo": "CASCO", "insumo_id": 15, "quantidade": 20.0, "unidade_medida_id": 107}	2434	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "SAMD205BT", "descricao": "TONER SAMSUNG D205 B/ TROCA", "marca": "SAMSUNG", "ativo": true, "permite_venda": true, "valor_venda": 150.0, "tipo": "CASCO", "insumo_id": 15, "quantidade": 50.0, "unidade_medida_id": 107}	2435	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "SAMML101BT", "descricao": "TONER SAMSUNG ML 101 B/ TROCA", "marca": "SAMSUNG", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "CASCO", "insumo_id": 15, "quantidade": 50.0, "unidade_medida_id": 107}	2436	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HP6002AMBT", "descricao": "TONER HP 6002 AMARELO B/ TROCA", "marca": "HP", "ativo": true, "permite_venda": false, "valor_venda": 0.0, "tipo": "CASCO", "insumo_id": 13, "quantidade": 50.0, "unidade_medida_id": 107}	2437	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "CARTUCHOHP", "descricao": "CARTUCHO HP 22", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 23.0, "tipo": "MERCADORIA"}	2438	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HP27", "descricao": "CARTUCHO HP 27", "marca": "STATIC CONTROL", "ativo": true, "permite_venda": true, "valor_venda": 45.0, "tipo": "MERCADORIA"}	2439	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"mercadoria_id": 46, "codigo": "HP22", "descricao": "CARTUCHO HP 22", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 23.0, "tipo": "MERCADORIA"}	2440	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HP614", "descricao": "CARTUCHO HP 614", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 45.0, "tipo": "MERCADORIA"}	2441	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"mercadoria_id": 47, "codigo": "HP27", "descricao": "CARTUCHO HP 27", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 45.0, "tipo": "MERCADORIA"}	2442	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "LEX26", "descricao": "CARTUCHO LEX 26", "marca": "LEXMARK", "ativo": true, "permite_venda": true, "valor_venda": 45.0, "tipo": "MERCADORIA"}	2443	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HP92", "descricao": "CARTUCHO HP 92", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 18.0, "tipo": "MERCADORIA"}	2444	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HP21", "descricao": "CARTUCHO HP 21", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 0.0, "tipo": "MERCADORIA"}	2445	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"mercadoria_id": 51, "codigo": "HP21", "descricao": "CARTUCHO HP 21", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 23.0, "tipo": "MERCADORIA"}	2446	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "AAA", "descricao": "AAA", "marca": "STATIC CONTROL", "ativo": true, "permite_venda": true, "valor_venda": 0.0, "tipo": "MERCADORIA"}	2447	\N	2019-09-19	soadmin	\N
soad.prc_delete_mercadoria	{"mercadoria_id": "52"}	2448	100	2019-09-19	soadmin	\N
soad.fnc_cadastro_pedido	{"pessoa_id": 317, "tipo_pedido": "COMPRA", "data_entrega": "19/09/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 49, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 45.0, "codigo": ""}]}	2449	\N	2019-09-19	soadmin	\N
soad.prc_encerrar_pedido	{"pedido_id": "443"}	2450	100	2019-09-19	soadmin	\N
soad.fnc_cadastro_pedido	{"pessoa_id": 312, "tipo_pedido": "VENDA", "data_entrega": "19/09/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 49, "quantidade": 5, "unidade_medida_id": 276, "valor_unitario": 45.0, "codigo": ""}]}	2451	\N	2019-09-19	soadmin	\N
soad.prc_encerrar_pedido	{"pedido_id": "444"}	2452	100	2019-09-19	soadmin	\N
soad.prc_estornar_pedido	{"pedido_id": "444"}	2453	100	2019-09-19	soadmin	\N
soad.prc_cancelar_pedido	{"pedido_id": "444"}	2454	100	2019-09-19	soadmin	\N
soad.fnc_cadastro_pedido	{"pessoa_id": 313, "tipo_pedido": "VENDA", "data_entrega": "19/09/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 49, "quantidade": 10, "unidade_medida_id": 276, "valor_unitario": 45.0, "codigo": ""}]}	2455	\N	2019-09-19	soadmin	\N
soad.prc_encerrar_pedido	{"pedido_id": "445"}	2456	100	2019-09-19	soadmin	\N
soad.fnc_cadastro_pedido	{"pessoa_id": 312, "tipo_pedido": "VENDA", "data_entrega": "19/09/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "REMANUFATURA", "casco_id": 5, "insumo_id": 14, "quantidade": 2, "valor_unitario": 23.0, "nova_remanufatura": true, "codigo": ""}]}	2457	\N	2019-09-19	soadmin	\N
soad.prc_cancelar_pedido	{"pedido_id": "446"}	2462	100	2019-09-19	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "5", "insumo_id": "14", "quantidade": "1", "realizar": false}	2463	\N	2019-09-19	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "6", "insumo_id": "11", "quantidade": "1", "realizar": false}	2467	\N	2019-09-19	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1212, "simular": true}	2468	\N	2019-09-19	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1212}	2469	\N	2019-09-19	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1212", "simular": true}	2470	\N	2019-09-19	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "6", "insumo_id": "11", "quantidade": "1", "realizar": false}	2471	\N	2019-09-19	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1213, "simular": true}	2472	\N	2019-09-19	soadmin	\N
soad.fnc_cadastro_pedido	{"pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "19/09/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 20, "unidade_medida_id": 276, "valor_unitario": 45.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 20, "unidade_medida_id": 276, "valor_unitario": 30.0, "codigo": ""}, {"item_pedido_id": -3, "tipo_item": "MERCADORIA", "mercadoria_id": 37, "quantidade": 23, "unidade_medida_id": 276, "valor_unitario": 10.0, "codigo": ""}, {"item_pedido_id": -4, "tipo_item": "MERCADORIA", "mercadoria_id": 43, "quantidade": 20, "unidade_medida_id": 276, "valor_unitario": 150.0, "codigo": ""}]}	2465	\N	2019-09-19	soadmin	\N
soad.prc_encerrar_pedido	{"pedido_id": "447"}	2466	100	2019-09-19	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1213}	2473	\N	2019-09-19	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1213", "simular": true}	2474	\N	2019-09-19	soadmin	\N
soad.prc_esvaziar_item_lote	{"item_lote_id": "5199"}	2475	100	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"mercadoria_id": 47, "codigo": "HP27", "descricao": "CARTUCHO HP 27", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 45.0, "tipo": "MERCADORIA"}	2476	\N	2019-09-19	soadmin	\N
soad.fnc_insert_update_mercadoria	{"codigo": "HP26", "descricao": "CARTUCHO HP 26", "marca": "HP", "ativo": true, "permite_venda": true, "valor_venda": 23.0, "tipo": "MERCADORIA"}	2477	\N	2019-09-19	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "7", "insumo_id": "15", "quantidade": "1", "realizar": false}	2480	\N	2019-09-28	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "7", "insumo_id": "10", "quantidade": "1", "realizar": false}	2482	\N	2019-09-28	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1215, "simular": true}	2483	\N	2019-09-28	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1215}	2484	\N	2019-09-28	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1215", "simular": true}	2485	\N	2019-09-28	soadmin	\N
soad.prc_esvaziar_item_lote	{"item_lote_id": "5179"}	2486	100	2019-09-28	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]}	2490	\N	2019-10-02	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57]}	2491	\N	2019-10-02	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "endereco": [{"pessoa_id": "", "id_municipio": 34, "logradouro": "Rua Padre jos\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\u00fassia", "cep": "84031029", "complemento": "Pr\\u00f3ximo ao mercadinho do seu z\\u00e9", "tipo": "COMERCIAL", "id_endereco": ""}], "modalidade": [57]}	2492	\N	2019-10-02	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "Idomar Augusto", "email": "idomar@uepg.br", "telefone": "42999823030", "documento": "11111111111", "inscricao_estadual": "ISENTO", "pessoa_id": "321", "endereco": [{"pessoa_id": "321", "id_municipio": 34, "logradouro": "Rua Padre jos\\\\u00e9 da Silva", "numero": "123", "bairro": "Jardim Nova R\\\\u00fassia", "cep": "84031029", "complemento": "Pr\\\\u00f3ximo ao mercadinho do seu z\\\\u00e9", "tipo": "COMERCIAL", "id_endereco": "66"}], "modalidade": [57]}	2493	\N	2019-10-02	soadmin	\N
soad.fnc_cadastro_pedido	{"pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2494	\N	2019-10-02	soadmin	\N
soad.prc_encerrar_pedido	{"pedido_id": "448"}	2495	100	2019-10-02	soadmin	\N
soad.fnc_cadastro_pedido	{"pessoa_id": 321, "tipo_pedido": "VENDA", "data_entrega": "02/10/2019", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 5, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2496	\N	2019-10-02	soadmin	\N
soad.prc_encerrar_pedido	{"pedido_id": "449"}	2497	100	2019-10-02	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "8", "insumo_id": "15", "quantidade": "1", "realizar": false}	2498	\N	2019-10-02	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "8", "insumo_id": "10", "quantidade": "1", "realizar": false}	2500	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1217, "simular": true}	2501	\N	2019-10-02	soadmin	\N
soad.prc_delete_remanufatura	{"remanufatura_id": "[1217]"}	2502	100	2019-10-02	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "5", "insumo_id": "10", "quantidade": "1", "realizar": false}	2503	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1218, "simular": true}	2504	\N	2019-10-02	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false}	2505	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1219, "simular": true}	2506	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1218}	2507	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1218", "simular": true}	2508	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1219}	2509	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1219", "simular": true}	2510	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1220}	2511	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1220", "simular": true}	2512	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1221}	2513	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1221", "simular": true}	2514	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1222}	2515	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1222", "simular": true}	2516	\N	2019-10-02	soadmin	\N
soad.prc_esvaziar_item_lote	{"item_lote_id": "5180"}	2517	100	2019-10-02	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "5", "insumo_id": "10", "quantidade": "4", "realizar": false}	2518	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1223, "simular": true}	2519	\N	2019-10-02	soadmin	\N
soad.prc_delete_remanufatura	{"remanufatura_id": "[1224, 1225, 1226]"}	2520	100	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1223}	2521	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1223", "simular": true}	2522	\N	2019-10-02	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "5", "insumo_id": "14", "quantidade": "1", "realizar": false}	2523	\N	2019-10-02	soadmin	\N
soad.prc_estornar_pedido	{"pedido_id": "449"}	2530	100	2019-10-09	soadmin	\N
soad.prc_estornar_pedido	{"pedido_id": "448"}	2541	100	2019-10-16	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false}	2525	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1228, "simular": true}	2526	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1228}	2527	\N	2019-10-02	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": "1228", "simular": true}	2528	\N	2019-10-02	soadmin	\N
soad.prc_esvaziar_item_lote	{"item_lote_id": "5181"}	2529	100	2019-10-02	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "FUNDEPAR/COL\\u00c9GIO ESTADUAL JOS\\u00c9 ELIAS DA ROCHA/FUNDO ROTATIVO", "telefone": "4232241451", "documento": "77741312000180", "inscricao_estadual": "ISENTO", "pessoa_id": "311", "endereco": [{"pessoa_id": "311", "id_municipio": 34, "logradouro": "RUA RICARDO WAGNER", "numero": "200", "bairro": "OLARIAS", "cep": "84035220", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "56"}], "modalidade": [57, 58]}	2531	\N	2019-10-09	soadmin	\N
soad.fnc_cadastro_pessoa	{"nome": "A C PEREIRA - INFORMATICA EIRELI", "documento": "02526512000111", "inscricao_estadual": "ISENTO", "fantasia": "PEREIRA & CONCEI\\u00c7\\u00c3O - INFORM\\u00c1TICA", "pessoa_id": "312", "endereco": [{"pessoa_id": "312", "id_municipio": 34, "logradouro": "RUA ABELIO BENATTI", "numero": "00000", "bairro": "JARDIM SOL", "cep": "84072000", "complemento": "", "tipo": "COMERCIAL", "id_endereco": "57"}], "modalidade": [57, 58]}	2532	\N	2019-10-15	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false}	2533	\N	2019-10-16	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1229, "simular": true}	2534	\N	2019-10-16	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "9", "insumo_id": "13", "quantidade": "1", "realizar": false}	2536	\N	2019-10-16	soadmin	\N
soad.fnc_gerar_remanufatura	{"casco_id": "9", "insumo_id": "10", "quantidade": "1", "realizar": false}	2538	\N	2019-10-16	soadmin	\N
soad.fnc_realizar_remanufatura	{"remanufatura_id": 1231, "simular": true}	2539	\N	2019-10-16	soadmin	\N
soad.prc_delete_remanufatura	{"remanufatura_id": "[]"}	2540	100	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2544	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2545	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2546	\N	2019-10-16	soadmin	\N
soad.prc_encerrar_pedido	{"pedido_id": "448"}	2547	100	2019-10-16	soadmin	\N
soad.prc_estornar_pedido	{"pedido_id": "448"}	2548	100	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2549	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2554	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2559	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 497, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2560	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 498, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 495, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2561	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 500, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 50, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": 499, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 3, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2562	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]}	2563	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]}	2564	\N	2019-10-16	postgres	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]}	2568	\N	2019-10-16	postgres	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 506, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2569	\N	2019-10-16	soadmin	\N
soad.prc_cancelar_pedido	{"pedido_id": "449"}	2578	100	2019-10-17	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 508, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 10, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2570	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 510, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]}	2571	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 512, "tipo_item": "MERCADORIA", "mercadoria_id": 38, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}]}	2572	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 514, "tipo_item": "MERCADORIA", "mercadoria_id": 35, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 51, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 23.0, "codigo": ""}]}	2573	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": -1, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]}	2574	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 517, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 11, "unidade_medida_id": 276, "valor_unitario": 0.0, "codigo": ""}, {"item_pedido_id": -2, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]}	2575	\N	2019-10-16	soadmin	\N
soad.fnc_cadastro_pedido	{"pedido_id": "448", "pessoa_id": 316, "tipo_pedido": "COMPRA", "data_entrega": "16/10/2019", "observacao": "\\t", "itens": [{"item_pedido_id": 519, "tipo_item": "MERCADORIA", "mercadoria_id": 36, "quantidade": 1, "unidade_medida_id": 276, "valor_unitario": 1.0, "codigo": ""}]}	2577	\N	2019-10-16	soadmin	\N
\.


--
-- TOC entry 3292 (class 0 OID 116342)
-- Dependencies: 239
-- Data for Name: usuario; Type: TABLE DATA; Schema: soad; Owner: postgres
--

COPY soad.usuario (id_usuario, fk_pessoa_id, usuario, funcao) FROM stdin;
\.


--
-- TOC entry 3299 (class 0 OID 0)
-- Dependencies: 198
-- Name: auditoria_id_auditoria_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.auditoria_id_auditoria_seq', 21698, true);


--
-- TOC entry 3300 (class 0 OID 0)
-- Dependencies: 201
-- Name: endereco_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.endereco_id_seq', 66, true);


--
-- TOC entry 3301 (class 0 OID 0)
-- Dependencies: 203
-- Name: estado_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.estado_id_seq', 1050, true);


--
-- TOC entry 3302 (class 0 OID 0)
-- Dependencies: 205
-- Name: insumo_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.insumo_id_seq', 15, true);


--
-- TOC entry 3303 (class 0 OID 0)
-- Dependencies: 207
-- Name: item_lote_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.item_lote_id_seq', 5361, true);


--
-- TOC entry 3304 (class 0 OID 0)
-- Dependencies: 209
-- Name: item_lote_remanufatura_id_remanufatura_item_lote_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.item_lote_remanufatura_id_remanufatura_item_lote_seq', 258, true);


--
-- TOC entry 3305 (class 0 OID 0)
-- Dependencies: 211
-- Name: item_pedido_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.item_pedido_id_seq', 522, true);


--
-- TOC entry 3306 (class 0 OID 0)
-- Dependencies: 213
-- Name: lote_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.lote_id_seq', 212, true);


--
-- TOC entry 3307 (class 0 OID 0)
-- Dependencies: 216
-- Name: modalidade_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.modalidade_id_seq', 155, true);


--
-- TOC entry 3308 (class 0 OID 0)
-- Dependencies: 218
-- Name: modalidade_pessoa_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.modalidade_pessoa_id_seq', 183, true);


--
-- TOC entry 3309 (class 0 OID 0)
-- Dependencies: 220
-- Name: municipio_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.municipio_id_seq', 39, true);


--
-- TOC entry 3310 (class 0 OID 0)
-- Dependencies: 222
-- Name: pais_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.pais_id_seq', 143, true);


--
-- TOC entry 3311 (class 0 OID 0)
-- Dependencies: 224
-- Name: pedido_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.pedido_id_seq', 449, true);


--
-- TOC entry 3312 (class 0 OID 0)
-- Dependencies: 227
-- Name: pessoa_fisica_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.pessoa_fisica_id_seq', 71, true);


--
-- TOC entry 3313 (class 0 OID 0)
-- Dependencies: 228
-- Name: pessoa_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.pessoa_id_seq', 321, true);


--
-- TOC entry 3314 (class 0 OID 0)
-- Dependencies: 230
-- Name: pessoa_juridica_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.pessoa_juridica_id_seq', 162, true);


--
-- TOC entry 3315 (class 0 OID 0)
-- Dependencies: 231
-- Name: produto_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.produto_id_seq', 53, true);


--
-- TOC entry 3316 (class 0 OID 0)
-- Dependencies: 233
-- Name: remanufatura_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.remanufatura_id_seq', 1231, true);


--
-- TOC entry 3317 (class 0 OID 0)
-- Dependencies: 235
-- Name: requisicoes_id_requisicao_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.requisicoes_id_requisicao_seq', 2578, true);


--
-- TOC entry 3318 (class 0 OID 0)
-- Dependencies: 236
-- Name: toner_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.toner_id_seq', 9, true);


--
-- TOC entry 3319 (class 0 OID 0)
-- Dependencies: 238
-- Name: unidade_medida_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.unidade_medida_id_seq', 349, true);


--
-- TOC entry 3320 (class 0 OID 0)
-- Dependencies: 240
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: soad; Owner: postgres
--

SELECT pg_catalog.setval('soad.usuario_id_seq', 1, false);


-- Completed on 2019-10-17 01:11:35

--
-- PostgreSQL database dump complete
--

