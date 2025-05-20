"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []

while True:
    print('O QUE DESEJA FAZER NA SUA LISTA?')
    usuario = input('[I]nserir [A]pagar [L]istar: ').lower()

    if usuario.lower() == 'i':
        os.system('cls')
        usuario = input('QUAL ITEM DESEJA ADD?:').lower()
        lista_compras.append(usuario)

    elif usuario.lower() == 'l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('AINDA NÃO A ITENS')

        for i, valor in enumerate(lista_compras):
            print('ESSE SÃO OS SEUS ITENS:')
            print(i, valor)
            
        
    elif usuario.lower() == 'a':
        
        usuario = input('QUAL ITEM DESEJA APAGAR?')

        try:
            indice = int(usuario)
            del lista_compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
        
    else:
        print('ESSA RESPOSTA É INVALIDA ._.')
        print('Por favor, escolha i, a ou l.')
