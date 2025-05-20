#Iterando strings com while

#       012345678910
nome = 'Barcelona'  # Iteráveis
#      1110987654321
#nova_string += '*L*u*i*z* *O*t*á*v*i*o'

indice = 0 
novo_nome= ''
while indice < len(nome):
    letra= nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)


