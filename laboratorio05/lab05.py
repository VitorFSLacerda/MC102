def reverter(i, j):
    global genoma
    if j > len(genoma):
        j = len(genoma)-1
 
    if (i >= 0 and i < len(genoma)) and j >= 0:
 
        lst_subgenoma = genoma[i:j+1:+1]
        lst_genoma_revertido = lst_subgenoma[::-1]
        genoma = genoma[:i] + lst_genoma_revertido + genoma[j+1:]    
 
def transpor(i, j, k):
    global genoma
 
    if k > len(genoma):
        k = len(genoma)-1
 
    if (i >= 0 and i < len(genoma)) and (j >= 0 and j < len(genoma)) and k >= 0:
        
        lst_subgenoma_1 = genoma[i:j+1:+1]
        lst_subgenoma_2 = genoma[j+1:k+1:+1]
        genoma = genoma[:i] + lst_subgenoma_2 + lst_subgenoma_1 + genoma[k+1:]
 
def combinar(add_genoma, i):
    global genoma
    
    if i > 0:
        genoma = genoma[:i] + add_genoma + genoma[i:]
 
    elif i == 0:
        if genoma != []:
            genoma = add_genoma + genoma
        else:
            genoma = add_genoma
 
def concatenar(elemento):
    global genoma
 
    genoma += elemento
 
def remover(i, j):
    global genoma
    
    if j > len(genoma):
        j = len(genoma)-1
 
    if (i >= 0 and i < len(genoma)) and j >= 0:
        genoma = genoma[:i] + genoma[j+1:]
        if genoma == "":
            genoma = []
 
def transpor_e_reverter(i, j, k):
    
    transpor(i, j, k)
    reverter(i, k)
 
def buscar(busca):
    global genoma
 
    qtd_repeticoes = genoma.count(busca)
 
    return print(qtd_repeticoes)
 
def buscar_bidirecional(busca):
    global genoma
 
    qtd_repeticoes_atual = genoma.count(busca)
    lst_temporaria = genoma[::-1]
    qtd_repeticoes_revertido = lst_temporaria.count(busca)
 
    return print(qtd_repeticoes_atual + qtd_repeticoes_revertido)
 
def mostrar():
    global genoma
 
    return print(*genoma, sep="")
 
informacoes = []
coleta_dados = 0
 
genoma = input()
 
if genoma != "sair":
 
    while coleta_dados != "sair":
        coleta_dados = input()
 
        if coleta_dados != "sair":
            informacoes.append(coleta_dados.split())
            
    for sublista in informacoes:
        for elemento in sublista:
            if elemento == "reverter":
 
                sublista[1] = int(sublista[1])
                sublista[2] = int(sublista[2])
                reverter(sublista[1], sublista[2])
 
            elif elemento == "transpor":
 
                sublista[1] = int(sublista[1])
                sublista[2] = int(sublista[2])
                sublista[3] = int(sublista[3])
                transpor(sublista[1], sublista[2], sublista[3])
 
            elif elemento == "combinar":
 
                sublista[2] = int(sublista[2])
                combinar(sublista[1], sublista[2])
 
            elif elemento == "concatenar":
 
                concatenar(sublista[1])
 
            elif elemento == "remover":
 
                sublista[1] = int(sublista[1])
                sublista[2] = int(sublista[2])
                remover(sublista[1], sublista[2])
 
            elif elemento == "transpor_e_reverter":
 
                sublista[1] = int(sublista[1])
                sublista[2] = int(sublista[2])
                sublista[3] = int(sublista[3])
                transpor_e_reverter(sublista[1], sublista[2], sublista[3])
 
            elif elemento == "buscar":
 
                buscar(sublista[1])
 
            elif elemento == "buscar_bidirecional":
 
                buscar_bidirecional(sublista[1])
                
            elif elemento == "mostrar":
 
                mostrar()