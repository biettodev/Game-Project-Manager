from src.database.connection import *

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
