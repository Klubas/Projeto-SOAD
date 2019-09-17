import os
import subprocess
import sys


class Installer:
    def __init__(self, postgresfolder=None, dump_file=None, host="localhost", port=5432):
        self.folder_runtime = postgresfolder
        self.dump_file = dump_file
        self.host = host
        self.port = str(port)

    def create_database(self):
        cmd = "pg_restore"
        if self.folder_runtime:
            cmd = '"' + str(os.path.join(self.folder_runtime, "pg_restore.exe")) + '" '

        args = '--host "' + self.host \
               + '" --port "' + self.port \
               + '" --username "postgres" --role "postgres" --dbname "postgres" --password "5151" --verbose "' \
               + self.dump_file + '"'

        cmd = cmd + ' ' + args
        print(cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        print(p)

if __name__ == '__main__':
    print(str(sys.argv))
    installer = Installer(sys.argv[1], sys.argv[2])
    installer.create_database()
    #
    c = input(">")
    #installer = Installer(os.path.join("C:", "Program Files (x86)", "pgAdmin 4", "v4", "runtime"))