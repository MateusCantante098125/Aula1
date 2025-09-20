numero = int(input("Introduza um número: "))

if numero == 0:
    print("O fatorial do número", numero, "é 1")
else:
    i = numero - 1
    fatorial = numero
    while i > 0:
        fatorial = fatorial * i
        i = i - 1
    print("O fatorial do número", numero, "é", fatorial)