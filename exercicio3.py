lista = []
menores = []
n_elementos = int(input("Qual o tamanho da lista? "))

for i in range(n_elementos):
    aux = int(input("Digite um número: "))
    lista.append(aux)

valor = int(input("Digite um número para buscar na lista: "))

for numero in lista:
    if numero == valor:
        print(f"O número {valor} foi encontrado na lista.")
        var = 1
        break
  
if var != 1:
    print(f"O número {valor} não foi encontrado na lista.")
                    