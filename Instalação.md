SOAD - Sistema organizacional de armazenagem e distribuição

Pós Instalação:

Antes da primeira execução do sistema, deve ser instalado o banco de dados PostgreSQL 11 e realizado as seguintes configurações:

- No momento da instalação definir uma senha para o usuário 'postgres'

Utilizando o painel PgAdmin:
   - Criar usuário administrador "soadmin"
   - Fazer restore utilizando o arquivo:
        <Local de instalação>\SOAD Sistema\Resources\Scripts\SQL\dump.backup

Após isso, o sistema poderá ser utilizado normalmente. 