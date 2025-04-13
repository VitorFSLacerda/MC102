dias = int(input())
 
info_dias = []
 
def remove_repeticoes(x):
    '''Converte em um dicionário e retorna reconversão para lista.'''
    return list(dict.fromkeys(x))
 
for i in range(dias):
    
    lst_brigas = []
 
    animais_brigam = int(input())
 
    for x in range(animais_brigam):
        lst_brigas.append(input().split())
 
    lst_proc_qtd = input().split()
    sublst_proc_qtd = []
    
    for x in range(0, len(lst_proc_qtd), 2):
        lst_proc_qtd[x+1] = int(lst_proc_qtd[x+1])
        sublst_proc_qtd.append([lst_proc_qtd[x], int(lst_proc_qtd[x+1])])
 
    total_animais_diarios = int(input())
    lst_animais_proc = []
 
    sublst_animais_proc = []
 
    for x in range(total_animais_diarios):
        [lst_animais_proc.append(y) for y in input().split()]
    
    for x in range(0, len(lst_animais_proc), 2):
        sublst_animais_proc.append([lst_animais_proc[x], (lst_animais_proc[x+1])])
 
    brigas = 0
 
    [lst.sort() for lst in lst_brigas] 
    for x in range(0, len(lst_animais_proc)-2, 2):
        for y in range(2, len(lst_animais_proc), 2):
            aux = [lst_animais_proc[x], lst_animais_proc[y]]
            if (sorted(aux) in lst_brigas) and (x != y):
                lst_brigas.remove(sorted(aux))
                brigas += 1
 
    animais_atendidos = []
    animais_n_atendidos = []
    proc_n_disponivel = []
 
    for sublst_1 in sublst_animais_proc:
 
        for sublst_2 in sublst_proc_qtd:
            
            if sublst_1[1] == sublst_2[0] and sublst_2[1] > 0:
                animais_atendidos.append(sublst_1[0])
                sublst_2[1] -= 1
 
            elif sublst_1[1] == sublst_2[0] and sublst_2[1] <= 0:
                animais_n_atendidos.append(sublst_1[0])
 
            elif sublst_1[1] not in lst_proc_qtd:
                proc_n_disponivel.append(sublst_1[0])
 
    info_dias.append([brigas, animais_atendidos, animais_n_atendidos, proc_n_disponivel, sublst_proc_qtd])
 
num_dia = 1
for dia in info_dias:
    print(f"Dia: {num_dia}")
    print(f"Brigas: {dia[0]}")
    
    if len(dia[1]) > 0:
        print("Animais atendidos: ", end="")
        print(f"{dia[1][0]}", end="")                
        [print(f", {animal}", end="") for animal in dia[1][1:]]
        print()
 
    if len(dia[2]) > 0:
        print("Animais não atendidos: ", end="")
        print(f"{dia[2][0]}", end="")                
        [print(f", {animal}", end="") for animal in dia[2][1:]]
        print()
 
    if len(dia[3]) > 0:
        proc_n_disp = remove_repeticoes(dia[3])
        for animal in proc_n_disp:
            print("Animal", animal, "solicitou procedimento não disponível.")
       
    print()
    num_dia+=1