with open('questao 3/votos.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.split('\n')

dados = []


for linha in linhas:
    fragmentos = linha.split(',')
    if len(fragmentos) > 1:
        dados.append(fragmentos)

print(dados)

print('Candidato: ', fragmentos[0])
print('Numero de votos: ', fragmentos[1])