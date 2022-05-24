import os

print('Lembre de colocar \\ entre as palavras do caminho')
caminho_dir = input('Digite o caminho que deseja verificar: ')

#le os arquivos q tem no diretorio

nome_subs = os.listdir(caminho_dir)

print(nome_subs)

