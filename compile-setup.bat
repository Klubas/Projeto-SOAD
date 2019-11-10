Y:
cd Y:\Projeto-SOAD

".\Resources\database\bin\runtime\pg_dump.exe" --schema-only --password --file ".\Resources\Scripts\SQL\dump_schema.backup" --host "10.0.2.2" --port "5433" --username "postgres" --verbose --quote-all-identifiers --format=t --blobs --create --clean --section=pre-data --section=data --section=post-data --inserts --column-inserts --disable-dollar-quoting --use-set-session-authorization --encoding "UTF8" "postgres"

rmdir /Q /S .\build
rmdir /Q /S .\dist

python Y:\Projeto-SOAD\compile-soad.py

del .\dist\SOAD-Sistema.zip
tar.exe -cf .\dist\SOAD-Sistema.zip .\dist\SOAD-Sistema

del ".\Resources\Scripts\setup\SOADsetup.exe"

"C:\Program Files (x86)\Inno Setup 6\compil32.exe" /cc ".\Resources\Scripts\setup\vm_setup_script.iss"
