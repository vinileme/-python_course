## EXERCÍCIO 8.1



# def display_message():
#     print('Estou aprendendo a usar funções nesse capítulo 8 do livro de python!')
    
# display_message()




# ## EXECÍCIO 8.2


# def favorite_book(title):
#     print(f'Um dos meus livros favoritos é {title}!')
    
    
# favorite_book('Alice no país das maravilhas')



#EXERCÍCIO 8.3
# def make_shirt(size, text):
#     print(f'O tamanho da camiseta será {size}, e na estampa estará escrito {text}')
    
    
# make_shirt('GG', 'O mundo é bonito')
# make_shirt(size='M', text='Snoopy fedorento')
    
    
#EXERCÍCIO 8.4

# def make_shirt(size='GG', text="Eu amo Python"):
#     print(f'O tamanho da camiseta será {size}, e na estampa estará escrito {text}')
    
    
    
# make_shirt(size='G')
# make_shirt(size='M')
# make_shirt(text='Eu to aprendendo essa porcaria') 


'''
Escreva uma função chamada city_country() que recebe o nome de uma cidade e seu país. A função deve retornar uma string formatada como esta:
"Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e exiba os valores re-tornados.

'''


# def city_country(city, country):
#     names = f"{city}, {country}"
#     return names.title()

# value = city_country('santiago', 'chile')
# value1 = city_country('brasilia', 'brasil')
# value2 = city_country('california', 'estados unidos')
# print(value)
# print(value1)
# print(value2)
'''

Álbum: Escreva uma função chamada make_album() que crie um dicionário representando um álbum de música. A função deve ter o nome de um artista e o título de álbum, 
e deve retornar um dicionário com essas duas informações. Utilize a função para criar três dicionários representando álbuns distintos. Exiba cada valor de retorno 
para mostrar que os dicionários estão armazenando adequadamente as informações do álbum.


Use None para adicionar um parâmetro opcional ao make_album() que possibilite armazenar o número de músicas em um álbum. Se a linha chamadora incluir um valor para 
o número de músicas, adicione esse valor ao dicionário do álbum. Crie, pelo menos, uma nova chamada de função que inclua o número de músicas em um álbum.


'''


# def make_album(name, title, musics=None):
    
#     if musics == None:
#         band = {
#             'vocal': name,
#             'name': title,
#         }
#         return band
#     band = {
#             'vocal': name,
#             'name': title,
#             'tracks': musics,
#         }
#     return band

# user = make_album('Jimi Dendrix','Guns an Roses')
# print(user)






'''



8.8 Álbuns de usuários: Comece com seu programa do Exercício 8.7. Escreva um loop while que possibilite aos usuários inserir o artista e o título de um álbum.
Após receber essas informações, chame make_album() com a entrada do usuário e exiba o dicionário criado. Não se esqueça de incluir um valor de saída no loop while.


'''


# while True:
    
#     def make_album(name, title=None, musics=None):
        
#         if musics == None:
#             band = {
#                 'vocal': name,
#                 'name': title,
#             }
#             return band
#         band = {
#                 'vocal': name,
#                 'name': title,
#                 'tracks': musics,
#             }
#         return band

#     name = input('Digite o nome o artista: ')
#     title = input('Digite o nome do album do artista: ')
    
#     value = {"vocal": name, "album": title}
    
#     make_album(value)
#     print(value)
    
    
    
    



def make_album(name, title=None, musics=None):
    """
    Função para criar um dicionário representando um álbum musical.
    """
    if musics is None:
        album = {
            'vocal': name,
            'title': title,
        }
    else:
        album = {
            'vocal': name,
            'title': title,
            'tracks': musics,
        }
    return album

while True:
    name = input('Digite o nome do artista: ')
    title = input('Digite o nome do álbum do artista: ')

    album_dict = make_album(name, title)
    print(album_dict)
