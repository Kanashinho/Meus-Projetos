"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

print('Jogo da Palavra Secreta')
palavra= 'botafogo'
start = input('Pronto para começar?[s]sim [n]ão:').lower().startswith('s')
start_1 = start
acertos = ''
erros = 0

if start_1 == True:
    print('Descubra a palavra com o menor numero de tentativas')
    print('Boa Sorte >_o')
    print('A Palavra secreta é:')
    print('*'*8)
    while True:
        letra = input('Digite uma Letra:')
        erros += 1
        if len(letra) > 1:   
            print('Digite só uma letra')
            continue
        if letra in palavra:
            acertos += letra

        palavra_formada=''

        for letra_acertada in palavra:
            if letra_acertada in acertos:
                palavra_formada+=letra_acertada
            else:
                palavra_formada+='*'
        print(palavra_formada)
        
        if palavra_formada == palavra:
            os.system('cls')
            print('PARABENS VOCÊ GANHOU <3')
            print(f'A PALAVRA ERA {palavra}')
            print('TENTATIVAS', erros) 
else:
    print('Volte Sempre <3')