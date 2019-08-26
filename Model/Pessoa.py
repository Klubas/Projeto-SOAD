
class Pessoa:

    def __init__(self, nome, email, telefone, documento, inscricao_estadual='ISENTO', fantasia=None, id_pessoa=None):
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
        if self.id_pessoa:
            return {
                "id_pessoa": self.id_pessoa,
                "nome": self.nome,
                "email": self.email,
                "telefone": self.telefone,
                "documento": self.documento,
                "inscricao_estadual": self.inscricao_estadual,
                "fantasia": self.fantasia,
                "modalidade": self.modalidade,
                "endereco": self.endereco
            }
        else:
            return {
                "nome": self.nome,
                "email": self.email,
                "telefone": self.telefone,
                "documento": self.documento,
                "inscricao_estadual": self.inscricao_estadual,
                "fantasia": self.fantasia
            }