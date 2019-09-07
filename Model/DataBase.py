import json
import logging
import os

from PySide2.QtCore import QThreadPool
from pydal import DAL

from Controller.Componentes.Worker import Worker


class DataBase:

    def __init__(self, username, password, host='localhost', port=5432, pool_size=5):
        self.schema = 'soad'
        self.username = username
        self.host = host
        self.port = port
        self.folder = 'Resources' + os.sep + 'database'
        self.dbinfo = 'postgres://' + username + ':' + password + '@' + host + ':' + str(port) + '/postgres'
        self.db = DAL(
            self.dbinfo,
            folder=self.folder,
            pool_size=pool_size,
            migrate=False
        )
        self.connection = None
        self.threadpool = QThreadPool()


    def busca_registro(self, nome_tabela, coluna, valor='', operador='='):

        sql = "select * from " + self.schema + ".fnc_buscar_registro(" \
              + "p_tabela=>" + "'" + nome_tabela + "'" \
              + ", p_coluna=>" + "'" + coluna + "'" \
              + ", p_valor=>" + "'" + valor + "'" \
              + ", p_operador=>" + "'" + operador + "'" \
              + ");"

        return self.execute_sql(sql)

    def get_registro(self, fnc, campo, valor):

        sql = "select * from " + self.schema + "." + fnc + "(" \
              + "p_" + campo + "=>" + "'" + str(valor) + "'" \
              + ");"

        return self.execute_sql(sql)

    def call_procedure(self, schema, params):

        # Remove parametros vazios
        vazio = []
        for param in params["params"].items():
            if param[1] == '':
                vazio.append(param[0])
        for i in range(len(vazio)):
            del params["params"][vazio[i]]

        params = json.dumps(params)
        sql = "select * from " + schema + ".fnc_chamada_de_metodo(" \
              + "p_json_params=>" + "'" + params + "'" \
            + ");"

        return self.execute_sql(sql)

    def execute_sql(self, sql):
        try:
            retorno = self.db.executesql(query=sql, as_dict=True)
            self.db.commit()
            logging.debug('sql=' + str(sql))
            logging.debug('retorno=' + str(retorno))
            prc = True, retorno, str(self.db._lastsql)

        except Exception as e:
            self.db.rollback()
            prc = False, e, str(sql)

        except:
            prc = False, 'Exceção não tratada', str(sql)

        return prc

    def __conectar_banco__(self, progress_callback):
        try:
            self.connection = self.db.__call__()
            #progress_callback.emit(100)
        except Exception as e:
            pass

            #progress_callback.emit(0)
        return self

    def definir_schema(self, schema):
        self.schema = schema
        self.execute_sql("SET search_path TO " + self.schema)  # Define o schema

    def fechar_conexao(self):
        self.db.close()

    def progress_fn(self, n):
        print("%d%% done" % n)

    def retorno_conexao(self, s):
        self.connection = s

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def abrir_conexao(self):
        # Pass the function to execute
        worker = Worker(self.db.__call__)  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.retorno_conexao)
        worker.signals.finished.connect(self.thread_complete)
        #worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

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