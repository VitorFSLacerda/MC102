jogadores = int(input())
 
grupo_1 = jogadores // 2
if jogadores % 2 == 1:
    grupo_1 += 1
 
caixa_magica = input().split()
lista_caixamagica = []
for x in caixa_magica:
    lista_caixamagica.append(int(x))
 
limites = input().split()
lista_limites = []
for x in limites:
    lista_limites.append(int(x))
 
resultado_inicial = []
limite_maior = 0
limite_menor = 0
for x in range(0, len(lista_limites), 2):
    limite_maior = lista_limites[x+1]
    limite_menor = lista_limites[x]
    resultado_inicial.append(limite_maior - limite_menor)
 
lista_multiplicacao = []
for x in range(len(lista_caixamagica)):
    lista_multiplicacao.append(lista_caixamagica[x] * resultado_inicial [x])
 
lista_soma = []
for x in range(len(lista_caixamagica)):
    lista_soma.append(lista_caixamagica[x] + resultado_inicial [x])
 
#Concatena elementos específicos das listas de multiplicaçao e soma em uma única lista.
resultado_final = []
for x in range(grupo_1):
    resultado_final.append(lista_multiplicacao[x])
for x in range(grupo_1, len(lista_soma)):
    resultado_final.append(lista_soma[x])
 
#Verifica se há um jogador vencedor, mostrando sua posição e pontos ou se há empate.
maior_pontuação = resultado_final [0]
posição_jogador = 1
caso_empate = 0
for x in range(1, len(resultado_final)):
    if resultado_final[x] > maior_pontuação:
        maior_pontuação = resultado_final[x]
        posição_jogador = x + 1
        caso_empate = 0
    elif resultado_final[x] == maior_pontuação:
        caso_empate = 1
if caso_empate > 0:
    print("Rodada de cerveja para todos os jogadores!")
else:
    print(f"O jogador número {posição_jogador} vai receber o melhor bolo", end=" ")
    print(f"da cidade pois venceu com {maior_pontuação} ponto(s)!")