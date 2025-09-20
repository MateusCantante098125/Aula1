nome = ""
idade = 0
idade_mais_nova = 1000
nome_mais_novo = ""
cartao_cidadao = ""

while True :
    idade = int(input("Introduza a sua idade : "))
    if idade == 999 :
        break
    
    nome = input("Introduza o seu nome : ")
    cartao_cidadao = input("Introduza o número do seu cartão : ")

    if idade_mais_nova > idade :
        idade_mais_nova = idade
        nome_mais_novo = nome

print("A pessoa mais nova do grupo é o", nome_mais_novo, "com", idade_mais_nova, "anos")
