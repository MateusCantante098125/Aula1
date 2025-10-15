lista = []
menores = []
n_elementos = 3
repeticoes = 0
maior = 0

for i in range(n_elementos+1):
    aux = int(input("Digite um número: "))
    lista.append(aux)

for i in range(n_elementos):
    for j in range(i+1,n_elementos):
        if lista[i] > lista[j] and lista[j] != lista[i-1]:
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
        else:
            continue
        
                    
            
print(lista)
        