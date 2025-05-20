import sqlite3

conexao = sqlite3.connect('Animes.db')

cursor = conexao.cursor()

dados = cursor.execute('SELECT * FROM Animes')

print(dados.fetchall())