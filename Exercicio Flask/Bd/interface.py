import tkinter as tk
import orm
from tkinter import messagebox

def adicionar_anime():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.adicionar_anime(nome, ano, nota)
    messagebox.showinfo("Sucesso", "Anime adicionado com sucesso!")

def autalizar_anime():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.atualizar_anime(id, nome, ano, nota)
    messagebox.showinfo("Sucesso", "Anime atualizado com sucesso!")

def deletar_anime():
    id = entry_id.get()
    orm.deletar_anime(id)
    messagebox.showinfo("Sucesso", "Anime deletado com sucesso!")

root = tk.Tk()
root.title("Gerenciador de Animes")

label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=18, pady=5)

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=18, pady=5)

label_ano = tk.Label(root, text="Ano:")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=18, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=18, pady=5)

button_adicionar = tk.Button(root, text="Adicionar Anime", command=adicionar_anime)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = tk.Button(root, text="Atualizar Anime", command=autalizar_anime)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_deletar = tk.Button(root, text="Deletar Anime", command=deletar_anime)
button_deletar.grid(row=6, column=0, columnspan=2, pady=5)


root.mainloop()