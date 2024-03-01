

primeiro_numero = input('Digite um número: ')
segundo_numero = input('Digite outro número: ')


if primeiro_numero > segundo_numero:
    print(f'O maior número foi o {primeiro_numero} \n')
    print(f'O menor número foi o {segundo_numero}')
elif segundo_numero > primeiro_numero:
    print(f'O maior número foi o {segundo_numero} \n')
    print(f'O menor número foi o {primeiro_numero}')
else:
    print(f'Os números {primeiro_numero} e {segundo_numero} são iguais!')
    