# def desconect(*args):
#     exti_ = input('DESEJA SAIR? [S]IM OU [N]ÃO ').lower().startswith('s')
#     if exti_ == True:
#         return args

# while True:
#     print('_' *10)

#     desconect(break)

def encontrar_numero(lista, alvo):
    for numero in lista:
        if numero == alvo:
            print(f"Número {alvo} encontrado!")
            break  # Sai do loop assim que o número é encontrado
    else:
        print(f"Número {alvo} não encontrado na lista.")

# Exemplo de uso:
lista_numeros = [1, 3, 7, 10, 15]
encontrar_numero(lista_numeros, 10)
# Saída: Número 10 encontrado!
