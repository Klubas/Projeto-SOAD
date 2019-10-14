#!/bin/bash
#./venv/bin/python3 ./Resources/Scripts/Installer.py /usr/bin ./Resources/Scripts/SQL/dump.backup
pg_restore --host "localhost" --port "5432" --username "lucas" --no-password --role "postgres" --dbname "postgres" --verbose "./Resources/Scripts/SQL/backup"
