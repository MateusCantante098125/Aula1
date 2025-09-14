nota_matematica = float(input("Introduza a nota de Matemática: "))
nota_portugues = float(input("Introduza a nota de Português: "))
nota_ingles = float(input("Introduza a nota de Inglês: "))
nota_geografia = float(input("Introduza a nota de Geografia: "))

media = (nota_matematica + nota_portugues + nota_ingles + nota_geografia) / 4

if media >= 9.5:
    print("Aprovado")
else:
    print("Reprovado")

