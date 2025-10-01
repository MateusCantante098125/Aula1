nota_mais_alta=0
genero_associado_nota=0
turma_associado_nota=0

numero_de_raparigas=0

idade_mais_nova=0
idade_mais_velha=0
aluno_mais_velho=0
aluno_mais_novo=0
turma_aluno_mais_novo=0
turma_aluno_mais_velho=0


numero_turmas=int(input("Introduza o numero de turmas no TeSP : "))
turma=0

while turma<numero_turmas:
    numero_de_alunos=int(input("Introduza o numero de alunos da turma : "))

    for alunos in (1,numero_de_alunos+1):
        print("\n0 é igual a feminino")
        print("1 é igual a masculino")
        genero=int(input("\nIntroduza o genero deste aluno : "))
        idade=int(input("\nIntroduza a idade deste aluno : "))
        nota=float(input("\nIntroduza a nota de acesso deste aluno : "))

        if idade>idade_mais_nova and idade_mais_nova==0:
            idade_mais_nova=idade
        elif idade<idade_mais_nova:
            idade_mais_nova=idade
        if idade>idade_mais_velha and idade_mais_velha==0:
            idade_mais_velha=idade
        elif idade>idade_mais_velha:
            idade_mais_velha=idade
        if genero==0:
            numero_de_raparigas+=1
        if nota > nota_mais_alta:
            nota_mais_alta= nota
            turma_associado_nota = turma
            genero_associado_nota = genero
            if genero_associado_nota==0:
                genero_associado_nota="Femenino"
            else:
                genero_associado_nota=="Masculino"
    turma+=1
print("A turma com o aluno mais novo é a",turma_aluno_mais_novo)
print("A turma com o aluno mais velho é a ",turma_aluno_mais_velho)
print("No TeSP existem no total ",numero_de_raparigas,"raparigas")
print("A turma com o aluno que teve a nota de entrada mais alta foi a turma ",turma_associado_nota)
print("A nota mais alta foi de ",nota_mais_alta," e o genéro deste aluno é ",genero_associado_nota)