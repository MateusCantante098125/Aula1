numero_dado = int(input("Introduza um número : "))
divisor = 2
fatores = []
aux = numero_dado
while True:
    while aux % divisor == 0:
        fatores.append(divisor)
        aux = aux / divisor

    divisor += 1
    if aux == 1:
        break
print("A factorização do numero",numero_dado,"é",fatores)
