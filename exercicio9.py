media_idades = 0
media_alturas = 0
altura_mais_alta = 0
idade_mais_nova = 100 
n_alunos = int(input("Introduza o número de alunos: "))

for i in range (0,n_alunos):
    idade = int(input("Introduza a idade do aluno: "))
    altura = float(input("Introduza a altura do aluno: "))
    
    media_idades = media_idades + idade
    media_alturas = media_alturas + altura
    
    if idade_mais_nova >= idade:
        idade_mais_nova = idade
    if altura > altura_mais_alta :
        altura_mais_alta = altura

print("A média das idades é: ", media_idades/n_alunos)
print("A média das alturas é: ", media_alturas/n_alunos)
print("A idade mais nova é: ", idade_mais_nova)
print("A altura mais alta é: ", altura_mais_alta)