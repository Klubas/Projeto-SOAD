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
            , _os=None
            , override_pg_path=False
    ):
        self.dump_file = dump_file
        self.host = host
        self.port = str(port)
        self.username = username
        self.password = password

        if not _os:
            import platform
            _os = platform.system()
        else:
            self.os = _os

        if self.os == 'Linux' and override_pg_path:
            self.folder_runtime = '/usr/bin'
        else:
            self.folder_runtime = postgresfolder

    def create_database(self):
        # Dump
        # /usr/bin/pg_dump --file "/home/lucas/git/Projeto-SOAD/Resources/Scripts/SQL/dump.backup"
        # --host "localhost" --port "5433" --username "postgres" --no-password --verbose --quote-all-identifiers
        # --format=t --blobs --create --clean --section=pre-data --section=data --section=post-data --inserts
        # --column-inserts --disable-dollar-quoting --use-set-session-authorization --encoding "UTF8" "postgres"
        if self.os == 'Windows':
            cmd = "pg_restore.exe"
        elif self.os == 'Linux':
            cmd = "pg_restore"
        else:
            logging.info("[Installer] Plataforma " + self.os + " sem suporte.")
            return

        if self.folder_runtime:
            cmd = str(os.path.join(self.folder_runtime, cmd))

            if self.os == 'Windows':
                self.dump_file = '"' + self.dump_file + '"'
                cmd = '"' + cmd + '" '

        elif self.os == 'Linux':
            cmd = '/usr/bin/' + cmd
        else:
            logging.info("[Installer] Pasta com executável  pg_restore não informada")

        os.environ["PGPASSWORD"] = self.password

        args = ' --host ' + self.host + \
               ' --port ' + self.port + \
               ' --username ' + self.username + \
               ' --role "postgres" --dbname "postgres" --verbose ' + self.dump_file

        # "Resources\database\bin\runtime\pg_restore.exe"  --host localhost --port 5433 --username soadmin --role "postgres" --dbname "postgres" --verbose Resources\Scripts\SQL\dump.backup
        cmd = cmd + args
        logging.info("[Installer] Restore: " + cmd)

        cmd = shlex.split(cmd)
        logging.debug("[Installer] Args: " + str(cmd))

        with open("log.txt", "w") as f:
            p = subprocess.Popen(cmd, stdout=f)
            p.wait()

        os.environ["PGPASSWORD"] = ''


if __name__ == '__main__':
    installer = Installer(sys.argv[1], sys.argv[2])
    installer.create_database()
