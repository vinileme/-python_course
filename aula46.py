"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'garrafa'
letras_acertadas = ''
numero_tentativas = 0
tentativas_maximas = len(palavra_secreta) * 2
while True:
    letra_digitada = input('Digite apenas uma letra: ').lower()
    numero_tentativas += 1
    
    if numero_tentativas >= tentativas_maximas:
        print('VOCÊ PERDEU!!! HAHAHAH')
        break
    else:
        if len(letra_digitada) > 1:
            print('Você digitou mais de uma letra!')
            continue
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
    
        palavra_formada = ''  
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*' 
        print(palavra_formada)
        
        if palavra_formada == palavra_secreta:
            os.system('clear')
            print('PARABÉNS, VOCÊ GANHOU!!')
            print(f'A palavra era {palavra_secreta}, e precisou de {numero_tentativas} tentativas!')
            letras_acertadas = ''
            numero_tentativas = 0
            tentativas_maximas = len(palavra_secreta) * 2