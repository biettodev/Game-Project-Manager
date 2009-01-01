##############################
# DOCUMENT CREATE AND DELETE #
##############################

from src.database.tableCreations import *
from src.database.connection import *
 
# Makes new game project register   
def createGameProject(project):
    try:
        sql_insert = """
            INSERT INTO game_projects (
                description,
                objective,
                history,
                assets,
                animations,
                levels,
                network,
                audio,
                main_gameplay,
                sec_gameplay
            )
            VALUES(
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """
        values = [
            project['description'],
            project['objective'],
            project['history'],
            project['assets'],
            project['animations'],
            project['levels'],
            project['network'],
            project['audio'],
            project['main_gameplay'],
            project['sec_gameplay']
    ]
        
        cursor.execute(sql_insert, values)
        conn.commit()
    except:
        return 'Houve um erro ao registrar os dados do novo projeto.'
    else:
        return 'Novo registro realizado!'
    
# Game project delete function
def deleteGameProject(game_cod):
    try:
        cursor.execute("DELETE FROM game_projects WHERE game_cod = {}".format(game_cod))
        conn.commit()
    except:
        return 'Não foi possível deletar este jogo! Tente novamente mais tarde.'
    else:
        return 'Jogo excluído da lista!'