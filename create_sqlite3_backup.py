import shutil
import sqlite3
import datetime

# Caminho para o arquivo do banco de dados original e para o backup
db_file = "./db.sqlite3"
backup_file = f"backup_db.sqlite3"

# Copiando o arquivo do banco de dados para criar o backup
shutil.copy2(db_file, backup_file)

print(f"Backup criado: {backup_file}")
