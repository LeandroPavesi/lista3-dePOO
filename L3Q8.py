from cmath import sqrt

with open('usuarios.csv', 'r', encoding='utf-8') as arquivo:
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

#transformando a lista com os dados de consumo em inteiros
novo_espaço = list(map(int, espaço))


#convertendo bytes para MegaBytes
convertido = []
for converter in novo_espaço:
    mb = (converter/(1024**2))
    convertido.append(mb)

#total de consumo
total_bytes = sum(convertido)


usuarios_str = list(map(str, usuarios2))
consumo_str = list(map(str, convertido))

juntos = []

with open('relatorio.txt', "w") as arqW:
    arqW.write('Usuario Espaco utilizado    % do uso')

    usado = []

    for uso in convertido:
        usado.append(((uso*100)/total_bytes))
    
    for i in range(len(usuarios2)):
        arqW.write(f'\n{usuarios2[i]} {convertido[i]:.5}MB {usado[i]:.5}%\n')
        
    arqW.write(f'\nEspaco total ocupado: {total_bytes:.5}MB')
    arqW.write(f'\nEspaco medio ocupado: {(total_bytes/6):.5}MB')
            
            

