import sqlite3

conexao = sqlite3.connect('Animes.db')

cursor = conexao.cursor()

cursor.execute(
    """
        INSERT INTO animes(nome, ano, nota)
        VALUES('Initial D', 1995, 10 )
    """
)

conexao.commit()
conexao.close()
print('Dados add a tabela')