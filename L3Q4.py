with open('questao 4/nomes.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    
linhas = conteudo.split('\n')

linhas_adicionar = []

for linha in linhas:
    if linha[0] != "#":
        linhas_adicionar.append(linha)

print(linhas_adicionar)

with open('questao 4/arq.txt', 'w') as opfile:
    opfile.write("\n".join(linhas_adicionar))

#falta fazer q ele não leia o que for #
   
