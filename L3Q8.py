from cmath import sqrt

with open('questao 8/usuarios.csv', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.split('\n')

usuarios = []

usuarios2 = []

espaço = []
        
for linha in linhas:
    fragmentos = linha.split(';')
    if len(fragmentos) > 1:
        usuarios.append(fragmentos)
        for i in range(0, 1):
            espaço.append(fragmentos[1])
            usuarios2.append(fragmentos[0])

print(usuarios)
#transformando a lista com os dados de consumo em inteiros
novo_espaço = list(map(int, espaço))
print(novo_espaço)

#convertendo bytes para MegaBytes
convertido = []
for converter in novo_espaço:
    mb = (converter/(1024**2))
    convertido.append(mb)
print(convertido)

total_bytes = sum(convertido)
print(total_bytes)

usuarios_str = list(map(str, usuarios2))
consumo_str = list(map(str, convertido))

juntos = []

print('Juntos', usuarios2)

with open('questao 8/relatorio.txt', "w") as arqW:
    arqW.write('Usuario Espaco utilizado    % do uso')

    usado = []

    for uso in convertido:
        usado.append(((uso*100)/total_bytes))

    print('Usado>', usado)
    
    for i in usuarios2:
        for c in convertido:
            for d in usado:
                arqW.write(f'\n{i}    {c:.2f}   {d:.2f}\n ')
            
            
            

