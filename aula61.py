"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

valor = []
i = 0
multiplicador_1 = 10
multiplicador_2 = 10
resultado_1 = 0
resultado_2 = 0

while True:
    numero_gerador1 = input('Digite 9 números para gerar um CPF: ')
    if len(numero_gerador1) != 9 or not numero_gerador1.isdigit():
        print('Número inválido, digite apenas 9 números!')
    else:
        for digito in numero_gerador1:
            resultado_1 += int(digito) * multiplicador_1
            multiplicador_1 -= 1
            
    primeiro_numero = (resultado_1 * 10) % 11
    
    primeiro_numero = primeiro_numero if primeiro_numero <= 9 else 0
    
    print(primeiro_numero)
    
    numero_gerador2 = input('Agora digite 10 números para gerar um CPF: ')
    if len(numero_gerador2) != 10 or not numero_gerador2.isdigit():
        print('Número inválido, digite apenas 10 números!')
    else:
        for digito in numero_gerador2:
            resultado_2 += int(digito) * multiplicador_2
            multiplicador_2 -= 1
            
    segundo_numero = (resultado_2 * 10) % 11
    
    segundo_numero = segundo_numero if segundo_numero <= 9 else 0
    
    print(segundo_numero)