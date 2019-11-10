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

    def get_documento(self, mascara=True):
        if mascara:
            if len(self.documento) == 11:
                documento = self.documento[:3] + "." + self.documento[3:6] + "." + self.documento[6:9] + "-" + self.documento[9:]
            else:
                documento = "%s.%s.%s/%s-%s" % (self.documento[0:2], self.documento[2:5], self.documento[5:8], self.documento[8:12], self.documento[12:14])
            return documento
        else:
            return self.documento

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
