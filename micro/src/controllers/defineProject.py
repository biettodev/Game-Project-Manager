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
                strongs,
                weaks,
                opportunities,
                threads,
                objective,
                history,
                assets,
                animations,
                levels,
                network,
                audio,
                main_gameplay,
                sec_gameplay,
                colors1,
                colors2,
                session_time
            )
            VALUES(
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """
        values = [
            project['description'],
            project['strongs'],
            project['weaks'],
            project['opportunities'],
            project['threads'],
            project['objective'],
            project['history'],
            project['assets'],
            project['animations'],
            project['levels'],
            project['network'],
            project['audio'],
            project['main_gameplay'],
            project['sec_gameplay'],
            project['colors1'],
            project['colors2'],
            project['session_time'],
        ]
        
        cursor.execute(sql_insert, values)
        conn.commit()
    except:
        print('Houve um erro ao registrar os dados do novo projeto.')
    else:
        print('Novo registro realizado!')
    
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