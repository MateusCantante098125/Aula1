lista = []
n_par = 0
n_impar = 0
n_elementos = 10

for i in range(n_elementos):
    aux = int(input("Digite um número: "))
    lista.append(aux)
    
lista = sorted(lista)
diferença = lista[n_elementos-1]-lista[0]

for i in lista:
    if i%2 == 0:
        n_par += 1
    elif i%2 == 1 :
        n_impar += 1

print(f"Números pares: {n_par}")
print(f"Números ímpares: {n_impar}")
print(f"Diferença entre o maior e o menor: {diferença}")