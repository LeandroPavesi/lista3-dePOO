def resultado(caminho_alunos, caminho_notas):

    with open(f'{caminho_alunos}', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    
    linhas = conteudo.split('\n')

    alunos = []

    for linha in linhas:
            alunos.append(linha)
    print(alunos)

    with open(f'{caminho_notas}', 'r', encoding='utf-8') as arquivo2:
        conteudo2 = arquivo2.read()
    
    linhas = conteudo2.split('\n')

    #pegando a primeira linha e separando
    #notas 1

    linhas = linhas[0:1]
    notas = []
    for linha in linhas:
        fragmentos = linha.split(' ')
        if len(fragmentos) > 1:
            notas.append(fragmentos)
    print(notas)
    notas_int = list(map(int, fragmentos))
    res_notas = sum(notas_int)/3
    print('notas 2:', res_notas)


 #notas 2
    linhas2 = linhas[1:2]
    notas2 = []
    for linha in linhas2:
        fragmentos2 = linha.split(' ')
        if len(fragmentos2) > 1:
            notas2.append(fragmentos2)
    print(notas2)
    notas_int2 = list(map(int, fragmentos))
    res_notas2 = sum(notas_int2)/3
    print('notas 2:', res_notas2)

    #notas 3
    linhas3 = linhas[2:3]
    notas3 = []
    for linha in linhas3:
        fragmentos3 = linha.split(' ')
        if len(fragmentos3) > 1:
            notas3.append(fragmentos3)
    print(notas3)
    notas_int3 = list(map(int, fragmentos3))
    res_notas3 = sum(notas_int3)/3
    print('notas 3:', res_notas3)
        
    



resultin = resultado('questao 7/alunos.txt', 'questao 7/notas.txt')