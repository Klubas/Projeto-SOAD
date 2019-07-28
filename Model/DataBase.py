import json
import logging
import os

from pydal import DAL


class DataBase:

    def __init__(self, username, password, host='localhost', port=5432, pool_size=5):

        self.username = username
        self.host = host
        self.port = port
        self.folder = 'Resources' + os.sep + 'database'
        self.dbinfo = 'postgres://' + username + ':' + password + '@' + host + ':' + str(port) + '/postgres'
        self.db = DAL(
            self.dbinfo,
            folder=self.folder,
            pool_size=pool_size
        )
        self.db.__call__()

    def call_procedure(self, schema, procedure, params):

        # Remove parametros vazios
        vazio = []
        for param in params["params"].items():
            print(param[1])
            if param[1] == '':
                vazio.append(param[0])
                print(param[0])

        for i in range(len(vazio)):
            del params["params"][vazio[i]]

        params = json.dumps(params)
        sql = "CALL " + schema + ".prc_chamada_de_metodo(" \
              + "p_metodo=>" + "'" + schema + "." + procedure + "'" \
              + ", p_json_params=>" + "'" + params + "'" \
              + ");"

        logging.info(sql)
        return self.execute_sql(sql)

    def execute_sql(self, sql):
        try:
            self.db.executesql(sql)
            self.db.commit()
            prc = True, 0, str(self.db._lastsql)

        except Exception as e:
            self.db.rollback()
            prc = False, e, str(sql)

        return prc

    def fechar_conexao(self):
        self.db.close()

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