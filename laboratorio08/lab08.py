dicionario = {"categorias simples": {
                "filme que causou mais bocejos": {},
                "filme que foi mais pausado": {},
                "filme que mais revirou olhos": {},
                "filme que não gerou discussão nas redes sociais": {},
                "enredo mais sem noção": {}}}
 
 
def coleta_avaliacoes(qtd_avaliadores, dicionario):
    """Coleta dados de cada avaliação e insere em uma lista."""
    for i in range(qtd_avaliadores):
        lst_dados = input().split(", ")
        insere_dicionario(lst_dados, dicionario)
 
 
def insere_dicionario(dados, dicionario):
    """Insere as informações de avaliação em um dicionário."""
 
    categoria = dados[1]
    filme = dados[2]
    nota = int(dados[3])
 
    if filme in dicionario["categorias simples"][categoria]:
 
        dicionario["categorias simples"][categoria][filme] = \
        soma_nota(categoria, filme, nota, dicionario)
 
    else:
        dicionario["categorias simples"][categoria].update({filme: [nota, 1]})
        
 
def soma_nota(categoria, filme, nota, dicionario):
    """Soma as notas do mesmo filme e mesma categoria dada por avaliadores diferentes."""
 
    valor_chave = dicionario['categorias simples'][categoria][filme]
    return [valor_chave[0] + int(nota), valor_chave[1] + 1 ]
 
 
def vencedor_simples(dados_filmes):
    """Retorna uma lista de vencedores para cada categoria de filmes com base nos dados de avaliação fornecidos."""
 
    vencedores = []
    for categoria, filmes in dados_filmes['categorias simples'].items():
 
        filme_com_maior_media = ""
        maior_media = 0
        quantidade_avaliacoes = 0
 
        for filme, [notas, avaliacoes] in filmes.items():
            media_filme = notas / avaliacoes
 
            if media_filme > maior_media or \
            (media_filme == maior_media and avaliacoes > quantidade_avaliacoes):
                
                filme_com_maior_media = filme
                maior_media = media_filme
                quantidade_avaliacoes = avaliacoes
 
        vencedores.append([filme_com_maior_media, categoria, maior_media])
 
    return vencedores
 
 
def vencedor_pior_filme(lst):
    """Retorna o nome do filme com o maior numero de categorias vencidas."""
 
    ocorrencias = {}
 
    for sublista in lst:
        filme = sublista[0]
        if filme in ocorrencias:
            ocorrencias[filme] += 1
        else:
            ocorrencias[filme] = 1
 
    nome = ""
    contador = 0
    for chave, valor in ocorrencias.items():
        if valor != contador:
            if valor > contador:
                contador = valor
                nome = chave
        else:
            pontuacao1 = 0
            pontuacao2 = 0
            for sub in lst:
                if sub[0] == nome:
                    pontuacao1 = sub[2]
                elif sub[0] == chave:
                    pontuacao2 = sub[2]
 
            if pontuacao1 < pontuacao2:
                nome = chave
 
    return nome
 
 
def filmes_ausentes(lista, dicionario):
    """Retorna uma lista com o nome dos filmes que não ganharam nenhuma categoria."""
 
    filmes_presentes = []
    for chave in dicionario["categorias simples"]:
        for filme in dicionario["categorias simples"][chave]:
            filmes_presentes.append(filme)
 
    ausentes = [filme for filme in lista if filme not in filmes_presentes]
    return ausentes
 
 
def impressao(vencedores_simples, pior_filme, ausentes):
    """Imprime os resultados da premiação, incluindo os vencedores nas categorias simples, o pior filme e os filmes ausentes."""
 
    print("#### abacaxi de ouro ####\n")
    print("categorias simples")
    for i in range(5):
        print(f"categoria: {vencedores_simples[i][1]}")
        print(f"- {vencedores_simples[i][0]}")
    print()
    print("categorias especiais")
    print("prêmio pior filme do ano")
    print(f"- {pior_filme}")
    print("prêmio não merecia estar aqui")
    if len(ausentes) == 0:
        print("- sem ganhadores")
    else:
        filmes_str = ", ".join(ausentes)
        print("- " + filmes_str)
 
def main():
 
    qtd_filmes = int(input())
 
    filmes = [input() for i in range(qtd_filmes)]
 
    coleta_avaliacoes(int(input()), dicionario)
 
    vencedores_caso_simples = vencedor_simples(dicionario)
 
    pior_filme = vencedor_pior_filme(vencedores_caso_simples)
 
    ausente = filmes_ausentes(filmes, dicionario)
    
    impressao(vencedores_caso_simples, pior_filme, ausente)
 
if __name__ == "__main__":
    main()