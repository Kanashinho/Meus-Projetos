"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Digite seu primeio nome:')
name = len(entrada)

if name <= 3:
    print(f'Seu nome é curto, ele tem {name} letas.')
elif name >= 4:
    print(f'Seu nome tem tamanho medio, ele tem {name} letas.')
elif name >= 6:
    print(f'Seu nome é longo, ele tem {name} letas.')


