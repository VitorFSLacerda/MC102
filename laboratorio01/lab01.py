jogada_sheila = input()
 
jogada_reginaldo = input()
 
if jogada_sheila == jogada_reginaldo:
    print("empate")
 
elif jogada_sheila == "tesoura":
    if jogada_reginaldo == "papel" or jogada_reginaldo == "lagarto":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
 
elif jogada_sheila == "papel":
    if jogada_reginaldo == "pedra" or jogada_reginaldo == "spock":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
 
elif jogada_sheila == "pedra":
    if jogada_reginaldo == "lagarto" or jogada_reginaldo == "tesoura":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
 
elif jogada_sheila == "lagarto":
    if jogada_reginaldo == "spock" or jogada_reginaldo == "papel":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
 
elif jogada_sheila == "spock":
    if jogada_reginaldo == "tesoura" or jogada_reginaldo == "pedra":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")