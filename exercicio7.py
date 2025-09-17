def alg_maior(numero):
    
    algarismo_maior = "0"
    for i in numero:
        if i > algarismo_maior:
            algarismo_maior = i
    print("O maior algarismo é:", algarismo_maior)
    
a = (input("Digite um número: "))
alg_maior(a)