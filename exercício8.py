aux = int(input("Quantos números pretende introduzir ? "))
numero_maior = "0"

for i in range(0,aux):
    numero = (input("Digite um número: "))
    if numero_maior<numero:
        numero_maior = numero

print("O maior número é",numero_maior)