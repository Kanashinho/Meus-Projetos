import sqlite3

conexao = sqlite3.connect('Animes.db')

cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE animes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
             )

conexao.close()