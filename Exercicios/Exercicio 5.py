"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero intero:')

if numero.isdigit():
    numero_int = int(numero)
    num = numero_int % 2 == 0 
    num_ = 'impar'
    if num:
        num_ = 'par'
    print(f'Seu numero {numero} é {num_}')
        
else:
    print('O numero escolhido não é inteiro')
