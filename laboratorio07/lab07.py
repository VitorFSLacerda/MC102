chars_validos = {"vogal": "aeiouAEIOU",
                "consoante": "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ",
                "numero": "0,1,2,3,4,5,6,7,8,9"}
  
  
def encontra_indice(tipo, string, start=0):
    """Retorna índice individualmente."""
 
    for x in string[start:]:
        if x in chars_validos[tipo]:
            return string.index(x)
 
 
def obtem_indices(string, tipo1, tipo2):
    """Retorna os dois índices."""
 
    if len(tipo1) == 1:
        indice1 = string.index(tipo1)
    else: 
        indice1 = encontra_indice(tipo1, string)
 
    if len(tipo2) == 1:
        indice2 = valida_indice(indice1, string[indice1:].index(tipo2))
    else: 
        indice2 = encontra_indice(tipo2, string, indice1)
 
    return [indice1, indice2]
 
 
def valida_indice(ind1, ind2):
    """Retorna o segundo índice com sua posição corrigida."""
    
    if ind1 == 0 and ind2 == 0:
        ind2 = 1
 
    else:
        ind2 += ind1
    
    return ind2
 
 
def valor_k(lst, operador):
  
    if operador == "+":
        return lst[0] + lst[1]
 
    elif operador == "-":
        return lst[0] - lst[1]
 
    elif operador == "*":
        return lst[0] * lst[1]
 
 
def decodificar(codificado, chave):
 
    chave %= 95
 
    msg_decodificada = []
    for string in codificado:
        string_decodificada = ""
 
        for letra in string:
            verificador_num = ord(letra) + chave
 
            if verificador_num > 126:
                verificador_num -= 95
 
            elif verificador_num < 32:
                verificador_num += 95
 
            string_decodificada += chr(verificador_num)
        msg_decodificada.append(string_decodificada)
 
    for linha in msg_decodificada:
        print(linha)
 
 
def main():
 
    operacao = input()
    termo1 = input()
    termo2 = input()
    qtd_linhas = int(input())
 
    msgs_codificadas = []
    for i in range(qtd_linhas):
        msgs_codificadas.append(input())
 
    msg_string = "".join(msgs_codificadas)
 
    par_indices = list(obtem_indices(msg_string, termo1, termo2))
    k = valor_k(par_indices, operacao)
 
    print(k)
    decodificar(msgs_codificadas, k)
 
 
if __name__ == "__main__":
    main()