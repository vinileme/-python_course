""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    resultado_soma = num_1_float + num_2_float
    resultado_subtracao = num_1_float - num_2_float
    resultado_multi = num_1_float * num_2_float
    resultado_divisao = num_1_float / num_2_float
    
    
    if operador == '+':
        print(f'O resultado da soma é: {resultado_soma:.2f}')
    elif operador == '-':
        print(f'O resultado da subtração é: {resultado_subtracao:.2f}')
    elif operador == '*':
        print(f'O resultado da multiplicação é: {resultado_multi:.2f}')
    else:
        print(f'O resultado da divisão é: {resultado_divisao:.2f}')
        
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break