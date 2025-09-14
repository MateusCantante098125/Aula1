numero = int(input("Introduza um número: "))

i = 0
n_divisoes = 0
while True:
    i = i + 1
    if numero%i == 0:
        n_divisoes = n_divisoes + 1
    else:
        n_divisoes = n_divisoes
    if i>numero:
        break
    
if n_divisoes <= 2:
    print("O número", numero,"é um número primo")
else:
    print("O número", numero,"não é um número primo")