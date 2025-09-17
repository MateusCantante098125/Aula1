media = 0
n_notas = 0
nota_melhor = 0
nome_melhor = ""

while True:
    nome = input("Introduza o seu nome: ")
    if nome == "STOP":
        media = media / n_notas
        break
    else:
        nota = float(input("Introduza uma nota: "))
        media = media + nota
        n_notas = n_notas + 1

    if nota_melhor < nota:
        nota_melhor = nota
        nome_melhor = nome
    if nome == "STOP":
        media = media / n_notas
        break
    else:
        media = media + nota
        n_notas = n_notas + 1

print("O melhor aluno é o",nome_melhor)
print("A média das notas foi de",media)