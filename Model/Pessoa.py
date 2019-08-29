class Pessoa:

    def __init__(self, nome, email, telefone, documento, inscricao_estadual='ISENTO', fantasia=None, id_pessoa=''):
        self.id_pessoa = str(id_pessoa)
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.inscricao_estadual = inscricao_estadual
        self.documento = documento
        self.fantasia = fantasia
        self.modalidade = list()
        self.endereco = list()

    def to_dict(self):

        enderecos = list(dict())
        if self.endereco is not None:
            for e in self.endereco:
                enderecos.append(e.to_dict())

        return {
                "nome": self.nome,
                "email": self.email,
                "telefone": self.telefone,
                "documento": self.documento,
                "inscricao_estadual": self.inscricao_estadual,
                "fantasia": self.fantasia,
                "pessoa_id": self.id_pessoa,
                "endereco": enderecos,
                "modalidade": list(self.modalidade)
        }
