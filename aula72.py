# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.



# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total
    


# valores = multiplicar(2, 2, 3, 4, 5)
# print(valores)



def par_impar(valor):
    conta = valor % 2 == 0
    
    if conta:
        return f'O {valor} é PAR!!'
    return f'O {valor} é IMPAR!'
    # return valor
    
print(par_impar(5))
print(par_impar(2))
print(par_impar(7))
print(par_impar(8))
print(par_impar(13))
