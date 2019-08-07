
class Pessoa:

    def __init__(self, nome, email, telefone, documento, inscricao_estadual='ISENTO', fantasia=None, id_pessoa=None):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.inscricao_estadual = inscricao_estadual
        self.documento = documento
        self.fantasia = fantasia

        self.modalidade = list()
        self.endereco = list()
