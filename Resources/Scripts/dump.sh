/usr/bin/pg_dump --file $HOME"/lucas/git/Projeto-SOAD/Resources/Scripts/SQL/dump.backup" --host "localhost" --port "5433" --username "postgres" --no-password --verbose --quote-all-identifiers --format=t --blobs --create --clean --section=pre-data --section=data --section=post-data  --inserts --column-inserts --disable-dollar-quoting --use-set-session-authorization --encoding "UTF8" "postgres"
/usr/bin/pg_dump --file $HOME"/git/Projeto-SOAD/Resources/Scripts/SQL/dump_schema.backup" --host "localhost" --port "5433" --username "postgres" --no-password --verbose --quote-all-identifiers --format=t --blobs --create --clean --section=pre-data --section=data --section=post-data  --inserts --column-inserts --disable-dollar-quoting --use-set-session-authorization --encoding "UTF8" "postgres" --schema-only
