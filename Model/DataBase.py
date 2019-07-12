from pydal import DAL, Field


class DataBase:

    def __init__(self, username, password, host, port, pool_size=5):

        self.username = username
        self.host = host
        self.port=port
        self.folder = 'database'
        self.dbinfo = 'postgres://' + username + ':' + password + '@' + host + ':' + str(port) + '/postgres'

        self.db = DAL(
            self.dbinfo,
            folder=self.folder,
            pool_size=pool_size
        )
        self.db.__call__()

    def parse_params(self, params_dict):
        params = ''
        for key in params_dict.keys():
            params = params + 'p_' + key + '=>' + "'" + params_dict[key] + "'" + ', '
        # remove a virgula que sobra no ultimo parametro antes de retornar
        return params[:-2]

    def call_procedure(self, procedure, params):
        params = self.parse_params(params)
        sql = "CALL soad." + procedure + "(" + params + ")"
        self.execute_sql(sql)

    def execute_sql(self, sql):
        try:
            self.db.executesql(sql)
            self.db.commit()
        except Exception as e:
            print(e)

"""
from PySide2.QtSql import QSqlDatabase

self.db = QSqlDatabase.addDatabase('QPSQL')
self.db.setHostName(host)
self.db.setPort(port)
self.db.setDatabaseName("postgres")
self.db.setUserName(username)
self.db.setPassword(password)

if self.db.open():
    self.db = QSqlDatabase.database()
else:
    print(self.db.lastError())
"""