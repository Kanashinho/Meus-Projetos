from modelos.avaliacao import Avaliacao
from modelos.itens.itens_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []

    def __init__(self, name):
        self.name = name
        self._active = False
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(25)}| {'Nota Média'.ljust(25)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f'{biblioteca.name.ljust(25)} | {str(biblioteca.media_avaliacao).ljust(25)} | {biblioteca._active}')

    def alterna_estado(self):
        self._active = not self._active

    @property
    def ativo(self):
        return 'ativada' if self._active else 'desativada'
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media
    
    def adicionar_item(self,item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)


    def exibir_itens(self):
        print(f'Itens da Biblioteca {self.name}\n')
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, 'isbn'):
                msg_livro = f'{i}. Títilo: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item.isbn}'
                print(msg_livro)
            else:
                msg_revista = f'{i}. Títilo: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edicao: {item.edicao}'
                print(msg_revista)