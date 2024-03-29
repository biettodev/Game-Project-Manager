from os import path, getcwd
import sqlite3

dbPath = path.join(f'{getcwd()}','src/database', 'game_projects.db')

# Handle connection errors
try:
    conn = sqlite3.connect('game_projects.db')
except:
    print('Não foi possível conectar ao Banco de Dados.')
else:
    print('Conexão com Banco de Dados realizada com sucesso!')
    
    # Definition of cursor
    cursor = conn.cursor()
