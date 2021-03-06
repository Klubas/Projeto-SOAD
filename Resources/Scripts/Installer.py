import logging
import os
import shlex
import subprocess
import sys


class Installer:
    def __init__(
            self
            , postgresfolder=None
            , dump_file=None
            , username='postgres'
            , password=''
            , host='localhost'
            , port=5432
            , dbname='postgres'
            , _os=None
            , override_pg_path=True
    ):
        self.dump_file = dump_file
        self.host = host
        self.port = str(port)
        self.dbname = dbname
        self.username = username
        self.password = password
        os.environ["PGPASSWORD"] = self.password

        if _os is None:
            import platform
            _os = platform.system()

        self._os = _os

        if self._os == 'Linux' and override_pg_path:
            self.folder_runtime = '/usr/bin'
        else:
            self.folder_runtime = postgresfolder

    def get_cmd(self, cmd):
        if self._os == 'Windows':
            cmd = cmd + '.exe '
        elif self._os == 'Linux':
            cmd = cmd
        else:
            logging.info("[Installer] Plataforma " + self._os + " sem suporte.")
            return

        if self.folder_runtime:
            cmd = str(os.path.join(self.folder_runtime, cmd))

        return cmd

    def create_user(self, user='soadmin', password='soad2019', permissoes='SUPERUSER CREATEDB CREATEROLE LOGIN'):

        cmd = self.get_cmd('psql')

        sql = 'CREATE ROLE {user} WITH {permissoes} PASSWORD \'{password}\''\
            .format(user=user, password=password, permissoes=permissoes)

        args = ' --host ' + self.host + \
               ' --port ' + self.port + \
               ' --username ' + self.username + ' -c "' + sql + '"' + \
               ' --dbname ' + self.dbname

        self.run_cmd(cmd + args)

    def configuracoes_iniciais(self):
        cmd = self.get_cmd('psql')

        sql = "SELECT * FROM soad.prc_configuracao_definicoes_iniciais()"

        args = ' --host ' + self.host + \
               ' --port ' + self.port + \
               ' --username ' + self.username + ' -c "' + sql + '"'

        self.run_cmd(cmd + args)

    def create_database(self):
        # Dump
        # /usr/bin/pg_dump --file "/home/lucas/git/Projeto-SOAD/Resources/Scripts/SQL/dump.backup"
        # --host "localhost" --port "5433" --username "postgres" --no-password --verbose --quote-all-identifiers
        # --format=t --blobs --create --clean --section=pre-data --section=data --section=post-data --inserts
        # --column-inserts --disable-dollar-quoting --use-set-session-authorization --encoding "UTF8" "postgres"

        self.create_user(password=self.password)

        cmd = self.get_cmd('pg_restore')

        if self._os == 'Windows':
            self.dump_file = '"' + self.dump_file + '"'
            cmd = '"' + cmd + '" '

        else:
            logging.info("[Installer] Pasta com executável  pg_restore não informada")

        args = ' --host ' + self.host + \
               ' --port ' + self.port + \
               ' --username ' + self.username + \
               ' --role "postgres" --dbname "postgres" --verbose ' + self.dump_file #+ \
               #' --single-transaction'

        # "Resources\database\bin\runtime\pg_restore.exe"  --host localhost --port 5433 --username soadmin --role "postgres" --dbname "postgres" --verbose Resources\Scripts\SQL\dump.backup

        self.run_cmd(cmd + args)

        self.configuracoes_iniciais()

        os.environ["PGPASSWORD"] = ''

    @staticmethod
    def run_cmd(cmd):

        logging.info("[Installer] Restore: " + cmd)

        if sys.platform == 'Linux' or sys.platform == 'Darwin':
            cmd = shlex.split(cmd)

        logging.debug("[Installer] Args: " + str(cmd))

        subprocess.call(cmd)


if __name__ == '__main__':
    installer = Installer(sys.argv[1], sys.argv[2])
    installer.create_database()
