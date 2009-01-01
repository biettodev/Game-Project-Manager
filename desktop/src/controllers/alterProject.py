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
        
        # Validations
        if newInfos[i] == oldInfos[1][i+1]:
            updated = oldInfos[1][i+1]
        elif newInfos[i] == '' and oldInfos[1][i] != '':
            updated = oldInfos[1][i+1]
        else:
            updated = newInfos[i]
            
        infosToUpdate.append(updated)
    
    sql_update = """
            UPDATE game_projects
            SET description  = ?,
                objective = ?,
                history = ?,
                assets = ?,
                animations = ?,
                levels = ?,
                network = ?,
                audio = ?,
                main_gameplay = ?,
                sec_gameplay = ?
            WHERE game_cod = {}
    """.format(game_cod) 
    try:
        cursor.execute(sql_update, (infosToUpdate))
        conn.commit()
    except:
        return 'Houve um erro ao atualizar os dados do projeto.'
    else:
        return 'Dados atualizados com sucesso!'