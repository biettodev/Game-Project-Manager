from view.interface import *
from os import path, getcwd
import sqlite3

dbPath = path.join(f'{getcwd()}', 'model', 'game_design_doc.db')

try:
    conn = sqlite3.connect(dbPath)
except:
    print('Não foi possível conectar ao Banco de Dados.')
else:
    print('Conexão com Banco de Dados realizado com sucesso!')

cursor = conn.cursor()

def getGameProject():
    try:
        select = "SELECT * FROM game_project"
    except:
        print('O arquivo não pôde ser lido.')
    else:
        header('DOCUMENTOS CRIADOS')
        cursor.execute(select)
        for l in cursor.fetchall():
            print(l)
            
            
def createGameProject(description='Nulo'):
    try:
        cursor.execute("INSERT INTO game_project(game_description) VALUES('{}')".format(description))
        conn.commit()
    except:
        print('Houve um erro ao registrar os dados do novo projeto.')
    else:
        print('Novo registro realizado!')
        

def updateGameProject(game_cod, game_description):    
    try:
        cursor.execute("""
            UPDATE game_project
            SET game_description = ?
            WHERE game_cod = ?
            """, (game_description, game_cod))
        conn.commit()
    except:
        print('Houve ao atualizar os dados do projeto.')
    else:
        print('Dados atualizados com sucesso!')
    

def deleteGameProject(game_cod):
    try:
        cursor.execute("DELETE FROM game_project WHERE game_cod = {}".format(game_cod))
        conn.commit()
    except:
        print('Não foi possível deletar este jogo! Tente novamente mais tarde.')
    else:
        print('Jogo excluído da lista!')
    pass