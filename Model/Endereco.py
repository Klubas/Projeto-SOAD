
class Endereco:

    def __init__(self
                 , id_pessoa
                 , logradouro
                 , numero
                 , bairro
                 , cep
                 , complemento
                 , tipo='COMERCIAL'
                 , id_municipio=None
                 , municipio=None
                 , id_estado=None
                 , estado=None
                 , id_pais=None
                 , pais=None
                 , id_endereco=''):
        self.id_endereco = str(id_endereco)
        self.id_pessoa = str(id_pessoa)
        self.id_municipio = id_municipio
        self.municipio = municipio
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.complemento = complemento
        self.tipo = tipo
        self.id_pais = id_pais
        self.pais = pais
        self.id_estado = id_estado
        self.estado = estado

    def to_dict(self):
        return {
            "pessoa_id": self.id_pessoa,
            "id_municipio": self.id_municipio,
            "municipio": self.municipio,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "bairro": self.bairro,
            "cep": self.cep,
            "complemento": self.complemento,
            "tipo": self.tipo,
            "id_endereco": self.id_endereco,
            "pais": self.pais,
            "sigla_uf": self.estado
        }

