import os
import json

print('DESEJA SE CONECTAR AO SISTEMA?: ')
conect = input('[S]IM OU [N]ÃO:' ).lower().startswith('s')

list_homework = []
list_homework_remake = []

if conect == True:
    os.system('cls')
    print('VOCÊ ENTROU NO SISTEMA📲')

    while True:
        os.system('cls')
        print(list_homework)
        print('O QUE DESEJA FAZER?: ')
        print('COMANDOS: INCLUIR / DESFAZER / REFAZER / SAIR /')
        user = input('DIGITE O COMANDO: ').lower()

        if user == 'incluir':
            add = input('')
            list_homework.append(add)
            
        if user == 'desfazer':
            list_homework.pop()
            list_homework_remake.append(list_homework)

        if user == 'refazer':
            list_homework = list_homework_remake.pop()
            list_homework.append(list_homework)



        if user == 'sair':
            with open('Exercicio 18.json', 'w') as arquivo:
                json.dump(list_homework, arquivo)
            print('DESCONECTADO📴')
            break
else:
    print('DESCONECTADO📴')

