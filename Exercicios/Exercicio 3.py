''' 1-Perguntar ao usuario dois numeros
    2-Responder se o primeiro numero é maoir, menor ou igual ao segundo
'''

valor_um= input('Diga-me um numero:')
valor_dois= input('Diga-me outro numero:')

if valor_um > valor_dois:
    print(valor_um, 'É maior que', valor_dois)
elif valor_um == valor_dois:
    print(valor_um, 'É igual a', valor_dois)
elif valor_um < valor_dois:
    print(valor_um, 'É menor que', valor_dois)
elif valor_dois > valor_um:
    print(valor_dois, 'É maior que', valor_um)
elif valor_dois < valor_um:
    print(valor_dois, 'É menor que', valor_um)    
else:
    print('Você não digitou um dos numeros pedidos!')