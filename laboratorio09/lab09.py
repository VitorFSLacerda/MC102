def recebe_matriz(qtd_linhas):
    """Recebe um número inteiro 'qtd_linhas' como entrada e assim produz uma matriz."""
    
    matriz = [input().split() for _ in range(qtd_linhas)]
    imprime_matriz(matriz)
    mapear(matriz)
 
 
def mapear(matriz):
    """Percorre a matriz linha por linha."""
 
    alternar_coluna = False
 
    for indice_linha in range(len(matriz)):
        
        tamanho_coluna = len(matriz[0])-1
 
        if indice_linha % 2 == 0:
 
            if alternar_coluna:
                
                matriz[indice_linha][0] = "r" #pula 1 da coluna da esquerda
                matriz[indice_linha-1][0] = "."
                imprime_matriz(matriz)
            alternar_coluna = True
            move_para_direita(matriz, indice_linha)
 
        else:
            
            matriz[indice_linha][tamanho_coluna] = "r" #pula 1 da coluna da direita
            matriz[indice_linha-1][tamanho_coluna] = "."
            move_para_esquerda(matriz, indice_linha)
 
    if len(matriz) % 2 == 0:
        move_ultima_coluna(matriz)
 
 
def move_para_direita(matriz, indice_linha):
    """Move o elemento 'r' para a direita na linha especificada pelo 'indice_linha' na matriz."""
 
    verificacao = [False]
 
    for indice_coluna in range(len(matriz[0])):
        
                if verificacao[0] == True:
                    
                    retorna_percurso(matriz, verificacao[1], verificacao[2])
                    verificacao = [False]
                    
                matriz[indice_linha][indice_coluna] = "r"
                
                if indice_coluna > 0:
                    
                    matriz[indice_linha][indice_coluna-1] = "."
                    imprime_matriz(matriz)
 
                if ((indice_coluna + 1 < len(matriz[indice_linha]))\
                    and (matriz[indice_linha][indice_coluna + 1] != "o"))\
                    or (indice_coluna == len(matriz[0])):
                    
                    verificacao = verifica_lados(matriz, indice_linha, indice_coluna)
 
 
def move_para_esquerda(matriz, indice_linha):
    """Move o elemento 'r' para a esquerda na linha especificada pelo 'indice_linha' na matriz."""
 
    verificacao = [False]
 
    for indice_coluna in range(len(matriz[indice_linha])-1, -1, -1):
        
                if verificacao[0] == True:
                    
                    retorna_percurso(matriz, verificacao[1], verificacao[2])
                    verificacao = [False]
 
                matriz[indice_linha][indice_coluna] = "r"
                
                if indice_coluna < len(matriz[indice_linha])-1:
 
                    matriz[indice_linha][indice_coluna+1] = "."
                imprime_matriz(matriz)
 
                if ((indice_coluna != 0) and (matriz[indice_linha][indice_coluna - 1] != "o"))\
                    and (indice_coluna != 0):
                    
                    verificacao = verifica_lados(matriz, indice_linha, indice_coluna)
 
 
def verifica_lados(matriz, indice_linha, indice_coluna):
    """Verifica se há 'o' nas posições adjacentes à posição do 'r' na matriz."""
 
    auxiliar = False
    inicial = [indice_linha, indice_coluna]
    atual = []
 
    while True:
        
        if indice_coluna > 0 and matriz[indice_linha][indice_coluna-1] == "o": #Verifica esquerda.
 
            matriz[indice_linha][indice_coluna] = "."
            matriz[indice_linha][indice_coluna-1] = "r"
            auxiliar = True
            imprime_matriz(matriz)
            indice_linha, indice_coluna = indice_linha, indice_coluna-1
            atual = [indice_linha, indice_coluna]
 
        elif indice_linha > 0 and matriz[indice_linha-1][indice_coluna] == "o": #Verifica cima.
 
            matriz[indice_linha][indice_coluna] = "."
            matriz[indice_linha-1][indice_coluna] = "r"
            auxiliar = True
            imprime_matriz(matriz)
            indice_linha, indice_coluna = indice_linha-1, indice_coluna
            atual = [indice_linha, indice_coluna]
            
        elif indice_coluna < len(matriz[indice_linha])-1\
            and matriz[indice_linha][indice_coluna+1] == "o": #Verifica direita.
 
            matriz[indice_linha][indice_coluna] = "."
            matriz[indice_linha][indice_coluna+1] = "r"
            auxiliar = True
            imprime_matriz(matriz)
            indice_linha, indice_coluna = indice_linha, indice_coluna+1
            atual = [indice_linha, indice_coluna]
            
        elif indice_linha < len(matriz)-1 and matriz[indice_linha+1][indice_coluna] == "o": #Verifica baixo.
 
            matriz[indice_linha][indice_coluna] = "."
            matriz[indice_linha+1][indice_coluna] = "r"
            auxiliar = True
            imprime_matriz(matriz)
            indice_linha, indice_coluna = indice_linha+1, indice_coluna
            atual = [indice_linha, indice_coluna]
        
        else:
            break
 
    if auxiliar:
 
        return [True, inicial, atual]
    else:
 
        return [False]
 
 
def retorna_percurso(matriz, inicial, atual):
    """Retorna ao percurso anterior após limpeza, movendo o elemento 'r' da posição atual para a posição inicial."""
 
    indice_linha0, indice_coluna0 = inicial
    indice_linha, indice_coluna = atual
 
    while True:
 
        if indice_coluna > indice_coluna0:
 
            matriz[indice_linha][indice_coluna] = "."
            matriz[indice_linha][indice_coluna - 1] = "r"
            imprime_matriz(matriz)
            indice_coluna -= 1
 
        elif indice_coluna < indice_coluna0:
 
            matriz[indice_linha][indice_coluna] = "."
            matriz[indice_linha][indice_coluna + 1] = "r"
            imprime_matriz(matriz)
            indice_coluna += 1
 
        elif indice_coluna == indice_coluna0:
 
            if indice_linha > indice_linha0:
 
                matriz[indice_linha][indice_coluna] = "."
                matriz[indice_linha - 1][indice_coluna] = "r"
                imprime_matriz(matriz)
                indice_linha -= 1
 
            if indice_linha < indice_linha0:
 
                matriz[indice_linha][indice_coluna] = "."
                matriz[indice_linha + 1][indice_coluna] = "r"
                imprime_matriz(matriz)
                indice_linha += 1
 
            if indice_linha == indice_linha0:
                break
 
        retorno = verifica_lados(matriz, indice_linha, indice_coluna)
 
        if retorno[0] != False: 
 
            indice_linha, indice_coluna = retorno[2][0], retorno[2][1]
 
 
def move_ultima_coluna(matriz):
    """Move o elemento 'r' até a última coluna da matriz."""
 
    ultima_linha = matriz[-1]
 
    for i in range(len(ultima_linha)-1):
 
        ultima_linha[i+1] = "r"
        ultima_linha[i] = "."
        matriz[-1] = ultima_linha
        imprime_matriz(matriz)
 
 
def imprime_matriz(matriz):
    """Imprime a matriz."""
 
    for linha in matriz:
        print(*linha)
    print()
 
 
def main():
 
	recebe_matriz(int(input()))
 
if __name__ == "__main__":
	main()