# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.




def multiplo (numero):
    def conta(multiplicacao):
        return numero * multiplicacao
    return conta
        


dobro = multiplo(2)
triplo = multiplo(3)
quadra = multiplo(4)

print(dobro(2))
print(triplo(3))
print(quadra(4))