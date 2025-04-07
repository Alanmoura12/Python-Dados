with open ('dados.txt',  encoding='utf-8') as arquivo:
    texto = arquivo.read()
    contador = texto.count('dados')
    print('total da palavra "dados" aparece !', contador)