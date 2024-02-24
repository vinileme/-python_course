""" 
        Faça um lista de compras com listas. O usuário deve ter a possibilidade de inserir,
        apagar e listar valores da sua lista.
        Não permita que o programa quebre com erros de indices inexistentes na lista.
   
"""
import os

lista_de_compras = []
letras_corretas = 'I', 'A', 'L', 'inserir', 'apagar', 'listar'
parar_programa = 'stop', 'sair', 'exit', 'parar'

while True:
    acao_desejada = input('Você deseja [I]nserir, [A]pagar ou [L]istar os itens da sua lista? ')
    os.system('clear')
    if acao_desejada.upper() != parar_programa:
        for letra in letras_corretas:
            if acao_desejada.upper() == letras_corretas[0]:
                acao = input('Qual item você deseja adicionar? ')
                lista_de_compras.append(acao)
                break
            elif acao_desejada.upper() == letras_corretas[2]:
                if lista_de_compras == []:
                    print('SUA LISTA ESTÁ VAZIA!')
                    break
                else:
                    print(f'{lista_de_compras}'.upper())
                    break
            else:
                acao = input('Qual índice você deseja apagar? ')
                try:
                    indice_acao = int(acao)
                    lista_de_compras.pop(indice_acao)
                    break
                except:
                    print('Digite um índice válido!')
                    break
        else:
            print('Ação incorreta, tente novamente.')   
    else:
        break