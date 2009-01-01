########################
# DOCUMENT ALTERATIONS #
########################

from src.database.tableCreations import *
from src.database.connection import *

from src.controllers.getProject import *

# Update one register
def updateGameProject(game_cod, newInfos): 
    oldInfos = getGameProject(game_cod)  
    
    infosToUpdate = list()
    
    for i in range(0, len(newInfos)):
        
        if newInfos[i] == oldInfos[i+1]:
            updated = oldInfos[i+1]
        elif newInfos[i] == '' and oldInfos[i] != '':
            updated = oldInfos[i+1]
        else:
            updated = newInfos[i]
            
        infosToUpdate.append(updated)
    
    sql_update = """
            UPDATE game_projects
            SET description  = ?, 
                strongs = ?,
                weaks = ?,
                opportunities = ?,
                threads = ?,
                objective = ?,
                history = ?,
                assets = ?,
                animations = ?,
                levels = ?,
                network = ?,
                audio = ?,
                main_gameplay = ?,
                sec_gameplay = ?,
                interfaces = ?,
                colors1 = ?,
                colors2 = ?,
                session_time = ?
            WHERE game_cod = {}
    """.format(game_cod) 
    try:
        cursor.execute(sql_update, (infosToUpdate))
        conn.commit()
    except:
        print('Houve um erro ao atualizar os dados do projeto.')
    else:
        print('Dados atualizados com sucesso!')