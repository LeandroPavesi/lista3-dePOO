print('Lembra de colocar questao 1/(caminho)')
caminho = input('Digite o nome da pasta existente: ')

palavra = input('Digite a palavra q deseja verificar:')

with open(f'{caminho}', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.split('\n')

dados = []

for linha in linhas:
    dados.append(linha)

print(dados) #teste

cont = 0
for i in range(len(dados)):
    if palavra == dados[i]:
        cont += 1

print(f'A palavra {palavra} é repetida {cont}')
