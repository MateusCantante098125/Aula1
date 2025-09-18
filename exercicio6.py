lado1 = float(input("Insira o valor do lado 1: "))
lado2 = float(input("Insira o valor do lado 2: "))
area = lado1 * lado2

if lado1 == lado2:
    print("O quadrado tem uma área de",area)
else:
    print("O retângulo tem uma área de",area)