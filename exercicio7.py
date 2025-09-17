numero = (input("Digite um número: "))
algarismo_maior = "0"
for i in numero:
    if i > algarismo_maior:
        algarismo_maior = i
print("O maior algarismo é:", algarismo_maior)