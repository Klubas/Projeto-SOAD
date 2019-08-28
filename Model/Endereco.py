
class Endereco:

    def __init__(self, id_pessoa, id_municipio, id_estado, id_pais, logradouro, numero, bairro, cep, complemento, tipo='COMERCIAL'):
        self.id_pessoa = id_pessoa
        self.id_municipio = id_municipio
        self.id_estado = id_estado
        self.id_pais = id_pais
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.complemento = complemento
        self.tipo = tipo

