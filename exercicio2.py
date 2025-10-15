lista = []
menores = []
n_elementos = int(input("Qual o tamanho da lista? "))

for i in range(n_elementos):
    aux = int(input("Digite um número: "))
    lista.append(aux)

for i in range(n_elementos):
    for j in range(i,n_elementos):
        if lista[i] > lista[j] and lista[j] != lista[i-1]:
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
        else:
            continue
        
      
            
print(lista)
        