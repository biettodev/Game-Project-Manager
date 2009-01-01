from src.database.connection import *

# Table creation
try:
    tableCreation = """
        CREATE TABLE IF NOT EXISTS game_projects(
            game_cod INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            objective TEXT,
            history TEXT,
            assets TEXT,
            animations TEXT,
            levels TEXT,
            network TEXT,
            audio TEXT,
            main_gameplay TEXT,
            sec_gameplay TEXT
        );
    """
    cursor.execute(tableCreation)
except:
    print('Erro na criação da tabela de projetos de jogo.')
