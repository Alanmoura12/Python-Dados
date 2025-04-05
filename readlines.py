arquivo = open ('dados.txt', 'r', encoding='utf-8')

conteudo = arquivo.readlines()

print('Tipo do conteudo ', type(conteudo))

print('conteudo retornado pelo readlines: ')

print(repr(conteudo))

arquivo.closed()

#pucha uma lista de strings