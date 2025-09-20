while True: 
    nota_matematica = float(input("Introduza a nota de Matemática (0-20): "))
    if 0 <= nota_matematica <= 20:
        break
    
while True:
    nota_portugues = float(input("Introduza a nota de Português (0-20): "))
    if 0 <= nota_portugues <= 20:
        break
    
while True:
    nota_ingles = float(input("Introduza a nota de Inglês (0-20): "))
    if 0 <= nota_ingles <= 20:
        break
    
while True:
    nota_geografia = float(input("Introduza a nota de Geografia (0-20): "))
    if 0 <= nota_geografia <= 20:
        break

media = (nota_matematica + nota_portugues + nota_ingles + nota_geografia) / 4

if media >= 9.5:
    print("Aprovado", media, "valores")
else:
    print("Reprovado", media, "valores")