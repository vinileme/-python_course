"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
lista.pop()


indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])
    
