instrução = input("Introduza uma instrução (Ligar, Desligar e Furar): ")

for letra in instrução:
    if letra.upper() == "L":
        print("Ligar")
        break
    elif letra.upper() == "D":
        print("Desligar")
        break
    elif letra.upper() == "F":
        print("Furar")
        break
    else:
        print("Instrução inválida")
        break