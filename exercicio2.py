from random import randrange

a = randrange(1, 10)  # não pode ser 0 para evitar divisão por zero
b = randrange(5, 20)
c = randrange(5, 20)

delta = b**2 - 4*a*c  # discriminante

if delta < 0:
    print("Não existem raízes reais")
else:
    resultado1 = (-b + delta**0.5) / (2*a)
    resultado2 = (-b - delta**0.5) / (2*a)
    print("Com o valor de a =", a)
    print("Com o valor de b =", b)
    print("Com o valor de c =", c)
    print("O resultado da raiz é:", resultado1)
    print("O resultado da raiz é:", resultado2)