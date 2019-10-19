import os
import sys


class Installer:
    def __init__(self, postgresfolder=None, dump_file=None, password='', host="localhost", port=5432):
        self.folder_runtime = postgresfolder
        self.dump_file = dump_file
        self.host = host
        self.port = str(port)
        self.password = password

    def create_database(self):
        cmd = "pg_restore"
        if self.folder_runtime:
            cmd = '"' + str(os.path.join(self.folder_runtime, "pg_restore.exe")) + '" '

        os.environ["PGPASSWORD"] = self.password
        args = '--host ' + self.host + ' --port ' + self.port + ' --username "soadmin" --role "postgres" --dbname "postgres" --verbose ' + self.dump_file
        os.environ["PGPASSWORD"] = ''

        cmd = cmd + ' ' + args
        print(cmd)
        f = open("log.txt", "w")
        #p = subprocess.Popen(cmd, stdout=f)
        #p.wait()

if __name__ == '__main__':
    installer = Installer(sys.argv[1], sys.argv[2])
    installer.create_database()

    #installer = Installer(os.path.join("C:", "Program Files (x86)", "pgAdmin 4", "v4", "runtime"))