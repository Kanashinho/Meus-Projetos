import sqlite3

def conecta_db():
    conexao = sqlite3.connect('Animes.db')
    return conexao

def insere_dados(nome, ano, nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
    """
        INSERT INTO animes(nome, ano, nota)
        VALUES(?,?,? )
    """, (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()

def listar_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Animes')
    dados = cursor.fetchall()
    cursor.close()
    return dados