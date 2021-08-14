from os import path, getcwd
import sqlite3

dbPath = path.join(f'{getcwd()}','src/database', 'game_projects.sqlite')

# Handle connection errors
try:
    conn = sqlite3.connect(dbPath)
except:
    print('Não foi possível conectar ao Banco de Dados.')
else:
    print('Conexão com Banco de Dados realizada com sucesso!')
    
    # Definition of cursor
    cursor = conn.cursor()
