arquivo = open ('dados.txt', 'r', encoding='utf-8')

conteudo = arquivo.readline()

print('Tipo do conteudo ', type(conteudo))

print('conteudo retornado pelo readline: ')

print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print('próximo conteúdo retornado')
print(repr(proximo_conteudo))

arquivo.closed()