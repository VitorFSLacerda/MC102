def preenche_com_zero(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    if len(vetor1) > len(vetor2):
        for x in range(len(vetor2), len(vetor1)):
            vetor2.append(int(0))
        return vetor2
 
    elif len(vetor1) < len(vetor2):
        for x in range(len(vetor1), len(vetor2)):
            vetor1.append(int(0))
        return vetor1
    return vetor1
 
 
def preenche_com_um(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    if len(vetor1) > len(vetor2):
        for x in range(len(vetor2), len(vetor1)):
            vetor2.append(int(1))
        return vetor2
 
    elif len(vetor1) < len(vetor2):
        for x in range(len(vetor1), len(vetor2)):
            vetor1.append(int(1))
        return vetor1
    return vetor1
 
 
def iguala_tamanho(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    if len(vetor1) > len(vetor2):
        for x in range(len(vetor2), len(vetor1)):
            vetor2.append(int(1))
        return vetor2
 
    elif len(vetor1) < len(vetor2):
        for x in range(len(vetor1), len(vetor2)):
            vetor1.append(int(0))
        return vetor1
    return vetor1
 
 
def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    preenche_com_zero(vetor1, vetor2)
 
    lst_temp = []
    for i in range(len(vetor1)):
        lst_temp.append(vetor1[i] + vetor2[i])
 
    return lst_temp
 
 
def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    preenche_com_zero(vetor1, vetor2)
 
    lst_temp = []
    for i in range(len(vetor1)):
        lst_temp.append(vetor1[i] - vetor2[i])
 
    return lst_temp
 
 
def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    preenche_com_um(vetor1, vetor2)
 
    lst_temp = []
    for i in range(len(vetor1)):
        lst_temp.append(vetor1[i] * vetor2[i])
 
    return lst_temp
 
 
def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    iguala_tamanho(vetor1, vetor2)
 
    lst_temp = []
    for i in range(len(vetor1)):
        lst_temp.append(vetor1[i] // vetor2[i])
 
    return lst_temp
 
 
def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
 
    for i in range(len(vetor)):
        vetor[i] *= escalar
 
    return vetor
 
 
def n_duplicacao(vetor: list[int], num: int) -> list[int]:
 
    if num > 0:
        vetor *= num
 
    elif num == 0:
        vetor.clear()
 
    return vetor
 
 
def soma_elementos(vetor: list[int]) -> int:
 
    contador: int = 0
    for numero in vetor:
        contador += numero
 
    return contador
 
 
def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
 
    preenche_com_um(vetor1, vetor2)
    lista_um = multiplica_vetores(vetor1, vetor2)
    lista_dois = soma_elementos(lista_um)
 
    return lista_dois
 
 
def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
 
    lst_temp = []
    for num_um in range(len(vetor1)):
        contador = 0
 
        for num_dois in range(len(vetor2)):
            contador += vetor1[num_um] * vetor2[num_dois]
 
        lst_temp.append(contador)
 
    return lst_temp
 
 
def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
 
    lst_temp = []
    for i in range(len(vetor) - len(mascara) + 1):
        contador = 0
 
        for x in range(len(mascara)):
            contador += vetor[i + x] * mascara[x]
 
        lst_temp.append(contador)
    return lst_temp
 
 
def main() -> None:
 
    vetor_um = list(map(int, input().split(",")))
 
    while True:
        coleta_dados = input()
 
        if coleta_dados != "fim":
            operacoes = coleta_dados
 
            if operacoes == "soma_elementos":
                vetor_um = [soma_elementos(vetor_um)]
                print(vetor_um)
 
            else:
                vetor_dois: list[int] = [int(x) for x in input().split(",")]
 
                if operacoes == "soma_vetores":
                    vetor_um = soma_vetores(vetor_um, vetor_dois)
                    print(vetor_um)
 
                elif operacoes == "subtrai_vetores":
                    vetor_um = subtrai_vetores(vetor_um, vetor_dois)
                    print(vetor_um)
 
                elif operacoes == "multiplica_vetores":
                    vetor_um = multiplica_vetores(vetor_um, vetor_dois)
                    print(vetor_um)
 
                elif operacoes == "divide_vetores":
                    vetor_um = divide_vetores(vetor_um, vetor_dois)
                    print(vetor_um)
 
                elif operacoes == "multiplicacao_escalar":
                    vetor_um = multiplicacao_escalar(vetor_um, vetor_dois[0])
                    print(vetor_um)
 
                elif operacoes == "n_duplicacao":
                    vetor_um = n_duplicacao(vetor_um, vetor_dois[0])
                    print(vetor_um)
 
                elif operacoes == "produto_interno":
                    vetor_um = [produto_interno(vetor_um, vetor_dois)]
                    print(vetor_um)
 
                elif operacoes == "multiplica_todos":
                    vetor_um = multiplica_todos(vetor_um, vetor_dois)
                    print(vetor_um)
 
                elif operacoes == "correlacao_cruzada":
                    vetor_um = correlacao_cruzada(vetor_um, vetor_dois)
                    print(vetor_um)
        else:
            break
 
 
if __name__ == "__main__":
    main()
 