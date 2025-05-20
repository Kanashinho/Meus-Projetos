"""
1-Perguntar ao usuario a conta que ele desa fazer $
2-Tratar dados do usuario
3-Criar variaves com as multiplicadores aritemeticos
4-Entrgar o resultado ao usuario
"""
while True:

    numero = float(input('Digite um numero:'))
    multiplicador = (input('Qual multiplicador desaja usar?+-*/:'))
    numero1 = float(input('Digite um numero:'))
    
    numero_validos= None
    num_1 = 0
    num_2 = 0
    try:
        numero_validos = True
    except:
        numero_validos= None
    if numero_validos is None:
        print('Um ou ambos ou numeros digitados são invalidos')
        continue
    multiplicador_1 = '+-*/'

    if multiplicador not in multiplicador_1:
        print('Multiplicador invalido')
        continue
    if len(multiplicador) > 1:
        print('Digite apenas uma multiplicador._.')
        continue
    if multiplicador == '+':
        print(f'Seu numero {numero} {multiplicador} {numero1} é igual {numero + numero1}')
    elif multiplicador == '-':
        print(f'Seu numero {numero} {multiplicador} {numero1} é igual {numero - numero1}')
    elif multiplicador == '*':
        print(f'Seu numero {numero} {multiplicador} {numero1} é igual {numero * numero1}')
    elif multiplicador == '/':
        print(f'Seu numero {numero} {multiplicador} {numero1} é igual {numero / numero1}')
    sair = input('Deseja sair ou Realizar uma nova conta?[s]im:').lower().startswith('s')
    if sair is True:
        break