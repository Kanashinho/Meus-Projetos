import sqlite3

conexao = sqlite3.connect('Animes.db')

cursor = conexao.cursor()

id = 1

cursor.execute(
    """
        UPDATE animes SET ano = ?
        WHERE id = ?
    """,
    (2024, id)
)

conexao.commit()

print('Dados atualizados')