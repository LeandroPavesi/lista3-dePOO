with open('questao 2/nomes.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.split('\n')

lista_desordenada = []

for linha in linhas:
    lista_desordenada.append(linha)

print('\nlista desordenada: ', lista_desordenada) #teste

lista_ordenada = sorted(lista_desordenada)

print('\nLista ordenada: ', lista_ordenada)
