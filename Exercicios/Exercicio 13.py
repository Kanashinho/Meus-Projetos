# Exercício - sistema de perguntas e respostas

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

import os
os.system('cls')
print('PRONTO PARA O DESAFIO?😎')
start = input('[S]im ou [N]ão: ').lower().startswith('s')

def resultado(*args):
    if resposta == True:
        return 'ACERTOU, PARABÉNS🎉'
    else:
        return '😝 ERROU'

acertos = 0
erros = 0

if start == True:
    nome = input('SEU NOME: ').upper()
    os.system('cls')
    print('Primera pergunta:')
    print(nome,',Quanto é 2+2?')
    alternativas_1 = 1, 2, 3, 4
    for i, opcoes in enumerate(alternativas_1):
        print(i,')', opcoes)
    resposta = input('Qual a sua resposta? ').startswith('3')
    if resposta == True:
        acertos += 1
    else:
        erros += 1
    print(resultado(1))

    
    print('Segunda pergunta:')
    print(nome,',Quanto é 5 x 5?')
    alternativas_1 = 15, 25, 35, 40
    for opcoes in enumerate(alternativas_1):
        print(opcoes)
    resposta = input('Qual a sua resposta? ').startswith('1')
    if resposta == True:
        acertos += 1
    else:
        erros += 1
    print(resultado(1))
    
    print('Terceira pergunta:')
    print(nome,',Quanto é 10/2?')
    alternativas_1 = 10, 9, 3, 5
    for opcoes in enumerate(alternativas_1):
        print(opcoes)
    resposta = input('Qual a sua resposta? ').startswith('3')
    if resposta == True:
        acertos += 1
    else:
        erros += 1
    os.system('cls')
    print(resultado(1))
    print('ACERTOS:', acertos)
    print('ERROS:', erros)
else:
    print('VOLTE SEMPRE😘')