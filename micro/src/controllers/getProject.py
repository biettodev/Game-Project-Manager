###########################
# DOCUMENTS VISUALIZAITON #
###########################

from view.interface import *

from src.database.tableCreations import *
from src.database.connection import *

# List all registers from database
def getGameProjects():
    try:
        select = "SELECT * FROM game_projects"
        cursor.execute(select)
    except:
        print('O arquivo não pôde ser lido.')
    else:
        header('DOCUMENTOS CRIADOS')
        for l in cursor.fetchall():
            print(l)
            
# Select and show an unique register
def getGameProject(game_cod):
    try:
        sql_select = """ 
            SELECT * FROM game_projects 
            WHERE game_cod = {}
        """.format(game_cod)
        
        result = cursor.execute(sql_select)
    except:
        print('Não foi possível abrir este documento!')
    else:
        return result.fetchone()