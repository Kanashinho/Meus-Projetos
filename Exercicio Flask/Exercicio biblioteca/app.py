from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade= Biblioteca('Biblioteca da Cidade')
biblioteca_shopping= Biblioteca('Biblioteca do Shopping')

livro1 = Livro('1984', 'George Orwell', 30.0, '084-3245')
revista1 = Revista('National Geographic', 'Jhon Doe', 15.0, 'Quinta')

# revista1.aplicar_desconto()
# biblioteca_cidade.alterna_estado()

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)


def main():
    # Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))
    biblioteca_cidade.exibir_itens()

if __name__ == '__main__':
    main()