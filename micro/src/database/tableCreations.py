from src.database.connection import *

# Table creation
try:
    tableCreation = """
        CREATE TABLE IF NOT EXISTS game_projects(
            game_cod INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            strongs TEXT,
            weaks TEXT,
            oppornities,
            threads TEXT,
            objective TEXT,
            history INTEGER,
            assets TEXT,
            animations TEXT,
            levels TEXT,
            network INTEGER,
            audio TEXT,
            main_gameplay TEXT NOT NULL,
            sec_gameplay TEXT,
            colors1 TEXT,
            colors2 TEXT,
            session_time TEXT
        );
    """
    cursor.execute(tableCreation)
except:
    print('Erro na criação da tabela de projetos de jogo.')
