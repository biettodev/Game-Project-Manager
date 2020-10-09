from desktop.interface import *
from os import path, getcwd
import sqlite3

dbPath = path.join(f'{getcwd()}', 'database', 'game_design_doc.db')

# Handle connection errors
try:
    conn = sqlite3.connect(dbPath)
except:
    print('Não foi possível conectar ao Banco de Dados.')
else:
    print('Conexão com Banco de Dados realizado com sucesso!')

# Definition of cursor
cursor = conn.cursor()

# Table creation
try:
    tableCreation = """
        CREATE TABLE IF NOT EXISTS game_projects(
            game_cod INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            strongs TEXT,
            weaks TEXT,
            oportunities TEXT,
            threads TEXT,
            objective TEXT,
            history TEXT,
            assets TEXT,
            animations TEXT,
            levels TEXT,
            network TEXT,
            audio TEXT,
            main_gameplay TEXT,
            sec_gameplay TEXT,
            interfaces TEXT,
            colors1 TEXT,
            colors2 TEXT,
            session_time TEXT
        );
    """
    cursor.execute(tableCreation)
except:
    print('Erro na criação da tabela de projetos de jogo.')

# List all registers from database
def getGameProject():
    try:
        select = "SELECT * FROM game_projects"
    except:
        print('O arquivo não pôde ser lido.')
    else:
        header('DOCUMENTOS CRIADOS')
        cursor.execute(select)
        for l in cursor.fetchall():
            print(l)
 
 
# Makes new game project register   
def createGameProject(project):
    try:
        cursor.execute(
            """INSERT INTO game_projects(description) 
            VALUES('{}')""".format(project['description'])
        )
        conn.commit()
    except:
        print('Houve um erro ao registrar os dados do novo projeto.')
    else:
        print('Novo registro realizado!')
 
 
# Update one register
def updateGameProject(game_cod, game_description):    
    try:
        cursor.execute("""
            UPDATE game_projects
            SET game_description = ?
            WHERE game_cod = ?
            """, (game_description, game_cod))
        conn.commit()
    except:
        print('Houve ao atualizar os dados do projeto.')
    else:
        print('Dados atualizados com sucesso!')
    
# Game project delete function
def deleteGameProject(game_cod):
    try:
        cursor.execute("DELETE FROM game_projects WHERE game_cod = {}".format(game_cod))
        conn.commit()
    except:
        print('Não foi possível deletar este jogo! Tente novamente mais tarde.')
    else:
        print('Jogo excluído da lista!')
    pass