import sqlite3

conexao = sqlite3.connect('Animes.db')

cursor = conexao.cursor()

id = 7,7

cursor.execute(
    """
        DELETE FROM animes
        WHERE ID in (?,?)
    """,
    id
)

conexao.commit()

print('Dados deletados')