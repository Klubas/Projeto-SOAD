from pydal import DAL, Field

class DataBase:
    def __init__(self, username, password, host, pool_size=5):
        self.username = username
        self.password = password
        self.host = host
        self.folder = 'database'
        self.pool_size = pool_size
        self.dbinfo = 'postgres://' + self.username + ':' + self.password + '@' + host + '/postgres'
        print(self.dbinfo)

        ### create DAL connection
        self.db = DAL(
            self.dbinfo,
            folder=self.folder,
            pool_size=self.pool_size
        )
        self.db.__call__()

    def parse_params(self, params_dict):
        params = ''
        for key in params_dict.keys():
            params = params + 'p_' + key + '=>' + "'" + params_dict[key] + "'" + ', '

        # remove a virgula que sobra no ultimo parametro antes de retornar
        return params[:-2]


    def insert(self, tabela, params):
        params = self.parse_params(params)
        sql = "CALL soad.insert_" + tabela + "(" + params + ")"
        try:
            called_procedure = self.db.executesql(sql)
            print(sql)
            return called_procedure
        except Exception:
            print("Erro ao executar: " + sql)

    def update(self):
        pass

    def delete(self):
        pass
