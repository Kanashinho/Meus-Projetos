# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multi(numero):
    def multiplicar(num):
        return numero * num
    return multiplicar
# duplicar = multi(10)
print(multi(3)(10))

