with open('questao 6/pontuações.csv', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.split('\n')

dados = []
        
for linha in linhas:
    fragmentos = linha.split(';')
    if len(fragmentos) > 1:
        dados.append(fragmentos)

#adicionando num dicionario para que ele pegue os nomes e transforme 
# em chave e por eliminação pegando o maior valor daquela chave
organizando = dict(dados)

print(organizando)

linhas2 = organizando

nova = []

for i in linhas2:
    nova.append(i)

print(nova)

#escrevendo no arquivo maiores pontuações

with open('questao 6/maiores_pontuações.csv', "w") as arqW:
    arqW.write("\n".join(organizando.values))
    
        
