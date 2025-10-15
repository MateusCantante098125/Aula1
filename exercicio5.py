menu = {
    "1": "Novo Jogo",
    "2": "Carregar Jogo",
    "3": "Configurações",
    "4": "Sair"
}

for numero,texto in menu.items():
    print(f"{numero}. {texto}")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Iniciando um novo jogo...")
    
    linha1 = [" ", " ", " "," "," "," "," "]
    linha2 = [" ", " ", " "," "," "," "," "]
    linha3 = [" ", " ", " "," "," "," "," "]
    linha4 = [" ", " ", " "," "," "," "," "]
    linha5 = [" ", " ", " "," "," "," "," "]
    linha6 = [" ", " ", " "," "," "," "," "]
    linha7 = [" ", " ", " "," "," "," "," "]
    tabuleiro = [linha1, linha2, linha3, linha4, linha5, linha6, linha7]
    
    while True:
    
        print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2], "|", tabuleiro[0][3], "|", tabuleiro[0][4], "|", tabuleiro[0][5], "|", tabuleiro[0][6])
        print("---------")
        print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2], "|", tabuleiro[1][3], "|", tabuleiro[1][4], "|", tabuleiro[1][5], "|", tabuleiro[1][6])
        print("---------")
        print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2], "|", tabuleiro[2][3], "|", tabuleiro[2][4], "|", tabuleiro[2][5], "|", tabuleiro[2][6])
        print("---------")
        print(tabuleiro[3][0], "|", tabuleiro[3][1], "|", tabuleiro[3][2], "|", tabuleiro[3][3], "|", tabuleiro[3][4], "|", tabuleiro[3][5], "|", tabuleiro[3][6])
        print("---------")
        print(tabuleiro[4][0], "|", tabuleiro[4][1], "|", tabuleiro[4][2], "|", tabuleiro[4][3], "|", tabuleiro[4][4], "|", tabuleiro[4][5], "|", tabuleiro[4][6])
        print("---------")
        print(tabuleiro[5][0], "|", tabuleiro[5][1], "|", tabuleiro[5][2], "|", tabuleiro[5][3], "|", tabuleiro[5][4], "|", tabuleiro[5][5], "|", tabuleiro[5][6])
        print("---------")
        print(tabuleiro[6][0], "|", tabuleiro[6][1], "|", tabuleiro[6][2], "|", tabuleiro[6][3], "|", tabuleiro[6][4], "|", tabuleiro[6][5], "|", tabuleiro[6][6])
        print("---------")
        
        while True:
            jogador_primario_linha = int(input("Jogador 1, escolha a linha (0, 1, 2, 3, 4, 5, 6 ou 7): "))
            jogador_primario_coluna = int(input("Jogador 1, escolha a coluna (0, 1, 2, 3, 4, 5, 6 ou 7): "))
            
            if tabuleiro[jogador_primario_linha][jogador_primario_coluna] == " " :
                tabuleiro[jogador_primario_linha][jogador_primario_coluna] = "X"
                break
            else:
                print("Posição já ocupada, escolha outra.")
        
        print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2], "|", tabuleiro[0][3], "|", tabuleiro[0][4], "|", tabuleiro[0][5], "|", tabuleiro[0][6])
        print("---------")
        print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2], "|", tabuleiro[1][3], "|", tabuleiro[1][4], "|", tabuleiro[1][5], "|", tabuleiro[1][6])
        print("---------")
        print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2], "|", tabuleiro[2][3], "|", tabuleiro[2][4], "|", tabuleiro[2][5], "|", tabuleiro[2][6])
        print("---------")
        print(tabuleiro[3][0], "|", tabuleiro[3][1], "|", tabuleiro[3][2], "|", tabuleiro[3][3], "|", tabuleiro[3][4], "|", tabuleiro[3][5], "|", tabuleiro[3][6])
        print("---------")
        print(tabuleiro[4][0], "|", tabuleiro[4][1], "|", tabuleiro[4][2], "|", tabuleiro[4][3], "|", tabuleiro[4][4], "|", tabuleiro[4][5], "|", tabuleiro[4][6])
        print("---------")
        print(tabuleiro[5][0], "|", tabuleiro[5][1], "|", tabuleiro[5][2], "|", tabuleiro[5][3], "|", tabuleiro[5][4], "|", tabuleiro[5][5], "|", tabuleiro[5][6])
        print("---------")
        print(tabuleiro[6][0], "|", tabuleiro[6][1], "|", tabuleiro[6][2], "|", tabuleiro[6][3], "|", tabuleiro[6][4], "|", tabuleiro[6][5], "|", tabuleiro[6][6])
        print("---------")
        
        if tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X" and tabuleiro[0][3] == "X": 
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X" and tabuleiro[0][3] == "X" and tabuleiro[0][4] == "X": 
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][2] == "X" and tabuleiro[0][3] == "X" and tabuleiro[0][4] == "X" and tabuleiro[0][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][3] == "X" and tabuleiro[0][4] == "X" and tabuleiro[0][5] == "X" and tabuleiro[0][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X" and tabuleiro[1][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X" and tabuleiro[1][3] == "X" and tabuleiro[1][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][2] == "X" and tabuleiro[1][3] == "X" and tabuleiro[1][4] == "X" and tabuleiro[1][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] == "X" and tabuleiro[1][4] == "X" and tabuleiro[1][5] == "X" and tabuleiro[1][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[2][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[2][3] == "X" and tabuleiro[2][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][2] == "X" and tabuleiro[2][3] == "X" and tabuleiro[2][4] == "X" and tabuleiro[2][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[2][4] == "X" and tabuleiro[2][5] == "X" and tabuleiro[2][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][0] == "X" and tabuleiro[3][1] == "X" and tabuleiro[3][2] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][1] == "X" and tabuleiro[3][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[3][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[3][4] == "X" and tabuleiro[3][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[3][4] == "X" and tabuleiro[3][5] == "X" and tabuleiro[3][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][0] == "X" and tabuleiro[4][1] == "X" and tabuleiro[4][2] == "X" and tabuleiro[4][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][1] == "X" and tabuleiro[4][2] == "X" and tabuleiro[4][3] == "X" and tabuleiro[4][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][2] == "X" and tabuleiro[4][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[4][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][0] == "X" and tabuleiro[5][1] == "X" and tabuleiro[5][2] == "X" and tabuleiro[5][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][1] == "X" and tabuleiro[5][2] == "X" and tabuleiro[5][3] == "X" and tabuleiro[5][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][2] == "X" and tabuleiro[5][3] == "X" and tabuleiro[5][4] == "X" and tabuleiro[5][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][3] == "X" and tabuleiro[5][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][0] == "X" and tabuleiro[6][1] == "X" and tabuleiro[6][2] == "X" and tabuleiro[6][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][1] == "X" and tabuleiro[6][2] == "X" and tabuleiro[6][3] == "X" and tabuleiro[6][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][2] == "X" and tabuleiro[6][3] == "X" and tabuleiro[6][4] == "X" and tabuleiro[6][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][3] == "X" and tabuleiro[6][4] == "X" and tabuleiro[6][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][1] =="X" and tabuleiro[1][2] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][2] =="X" and tabuleiro[2][3] == "X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] =="X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][2] =="X" and tabuleiro[1][3] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] =="X" and tabuleiro[2][4] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] =="X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] =="X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][3] =="X" and tabuleiro[1][4] == "X" and tabuleiro[2][5] == "X" and tabuleiro[3][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] =="X" and tabuleiro[2][4] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] =="X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] =="X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][6] == "X" and tabuleiro[1][5] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][5] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][4] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][5] == "X" and tabuleiro[1][4] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][4] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][4] == "X" and tabuleiro[1][3] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][1] == "X" and tabuleiro[4][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X" and tabuleiro[3][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X" and tabuleiro[3][0] == "X" and tabuleiro[4][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][0] == "X" and tabuleiro[3][0] == "X" and tabuleiro[4][0] == "X" and tabuleiro[5][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][0] == "X" and tabuleiro[4][0] == "X" and tabuleiro[5][0] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X" and tabuleiro[3][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X" and tabuleiro[3][1] == "X" and tabuleiro[4][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][1] == "X" and tabuleiro[3][1] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][1] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][2] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][2] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][2] == "X" and tabuleiro[6][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][3] == "X" and tabuleiro[1][3] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][3] == "X" and tabuleiro[5][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][3] == "X" and tabuleiro[5][3] == "X" and tabuleiro[6][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][4] == "X" and tabuleiro[1][4] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][4] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][4] == "X" and tabuleiro[4][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][4] == "X" and tabuleiro[3][4] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][4] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][4] == "X" and tabuleiro[6][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][5] == "X" and tabuleiro[1][5] == "X" and tabuleiro[2][5] == "X" and tabuleiro[3][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][5] == "X" and tabuleiro[2][5] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][5] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][5] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][6] == "X" and tabuleiro[1][6] == "X" and tabuleiro[2][6] == "X" and tabuleiro[3][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][6] == "X" and tabuleiro[2][6] == "X" and tabuleiro[3][6] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][6] == "X" and tabuleiro[3][6] == "X" and tabuleiro[4][6] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][6] == "X" and tabuleiro[4][6] == "X" and tabuleiro[5][6] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O" and tabuleiro[0][3] == "O": 
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O" and tabuleiro[0][3] == "O" and tabuleiro[0][4] == "O": 
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][2] == "O" and tabuleiro[0][3] == "O" and tabuleiro[0][4] == "O" and tabuleiro[0][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][3] == "O" and tabuleiro[0][4] == "O" and tabuleiro[0][5] == "O" and tabuleiro[0][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O" and tabuleiro[1][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O" and tabuleiro[1][3] == "O" and tabuleiro[1][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][2] == "O" and tabuleiro[1][3] == "O" and tabuleiro[1][4] == "O" and tabuleiro[1][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] == "O" and tabuleiro[1][4] == "O" and tabuleiro[1][5] == "O" and tabuleiro[1][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[2][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[2][3] == "O" and tabuleiro[2][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][2] == "O" and tabuleiro[2][3] == "O" and tabuleiro[2][4] == "O" and tabuleiro[2][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[2][4] == "O" and tabuleiro[2][5] == "O" and tabuleiro[2][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][0] == "O" and tabuleiro[3][1] == "O" and tabuleiro[3][2] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][1] == "O" and tabuleiro[3][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[3][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[3][4] == "O" and tabuleiro[3][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[3][4] == "O" and tabuleiro[3][5] == "O" and tabuleiro[3][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][0] == "O" and tabuleiro[4][1] == "O" and tabuleiro[4][2] == "O" and tabuleiro[4][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][1] == "O" and tabuleiro[4][2] == "O" and tabuleiro[4][3] == "O" and tabuleiro[4][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][2] == "O" and tabuleiro[4][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[4][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][0] == "O" and tabuleiro[5][1] == "O" and tabuleiro[5][2] == "O" and tabuleiro[5][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][1] == "O" and tabuleiro[5][2] == "O" and tabuleiro[5][3] == "O" and tabuleiro[5][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][2] == "O" and tabuleiro[5][3] == "O" and tabuleiro[5][4] == "O" and tabuleiro[5][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][3] == "O" and tabuleiro[5][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][0] == "O" and tabuleiro[6][1] == "O" and tabuleiro[6][2] == "O" and tabuleiro[6][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][1] == "O" and tabuleiro[6][2] == "O" and tabuleiro[6][3] == "O" and tabuleiro[6][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][2] == "O" and tabuleiro[6][3] == "O" and tabuleiro[6][4] == "O" and tabuleiro[6][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][3] == "O" and tabuleiro[6][4] == "O" and tabuleiro[6][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][1] =="O" and tabuleiro[1][2] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][2] =="O" and tabuleiro[2][3] == "O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] =="O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][2] =="O" and tabuleiro[1][3] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] =="O" and tabuleiro[2][4] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] =="O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] =="O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][3] =="O" and tabuleiro[1][4] == "O" and tabuleiro[2][5] == "O" and tabuleiro[3][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] =="O" and tabuleiro[2][4] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] =="O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] =="O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][6] == "O" and tabuleiro[1][5] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][5] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][4] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][5] == "O" and tabuleiro[1][4] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][4] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][4] == "O" and tabuleiro[1][3] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][1] == "O" and tabuleiro[4][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O" and tabuleiro[3][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O" and tabuleiro[3][0] == "O" and tabuleiro[4][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][0] == "O" and tabuleiro[3][0] == "O" and tabuleiro[4][0] == "O" and tabuleiro[5][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][0] == "O" and tabuleiro[4][0] == "O" and tabuleiro[5][0] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O" and tabuleiro[3][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O" and tabuleiro[3][1] == "O" and tabuleiro[4][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][1] == "O" and tabuleiro[3][1] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][1] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][2] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][2] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][2] == "O" and tabuleiro[6][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][3] == "O" and tabuleiro[1][3] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][3] == "O" and tabuleiro[5][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][3] == "O" and tabuleiro[5][3] == "O" and tabuleiro[6][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][4] == "O" and tabuleiro[1][4] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][4] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][4] == "O" and tabuleiro[4][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][4] == "O" and tabuleiro[3][4] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][4] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][4] == "O" and tabuleiro[6][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][5] == "O" and tabuleiro[1][5] == "O" and tabuleiro[2][5] == "O" and tabuleiro[3][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][5] == "O" and tabuleiro[2][5] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][5] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][5] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][6] == "O" and tabuleiro[1][6] == "O" and tabuleiro[2][6] == "O" and tabuleiro[3][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][6] == "O" and tabuleiro[2][6] == "O" and tabuleiro[3][6] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][6] == "O" and tabuleiro[3][6] == "O" and tabuleiro[4][6] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][6] == "O" and tabuleiro[4][6] == "O" and tabuleiro[5][6] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        
        
        while True:
            
            jogador_secundario_linha = int(input("Jogador 2, escolha a linha (0, 1, 2, 3, 4, 5, 6 ou 7): "))
            jogador_secundario_coluna = int(input("Jogador 2, escolha a coluna (0, 1, 2, 3, 4, 5, 6 ou 7): "))
            
            if tabuleiro[jogador_secundario_linha][jogador_secundario_coluna] == " " :
                tabuleiro[jogador_secundario_linha][jogador_secundario_coluna] = "O"
                break
            else:
                print("Posição já ocupada, escolha outra.")

        if tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X" and tabuleiro[0][3] == "X": 
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X" and tabuleiro[0][3] == "X" and tabuleiro[0][4] == "X": 
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][2] == "X" and tabuleiro[0][3] == "X" and tabuleiro[0][4] == "X" and tabuleiro[0][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][3] == "X" and tabuleiro[0][4] == "X" and tabuleiro[0][5] == "X" and tabuleiro[0][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X" and tabuleiro[1][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X" and tabuleiro[1][3] == "X" and tabuleiro[1][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][2] == "X" and tabuleiro[1][3] == "X" and tabuleiro[1][4] == "X" and tabuleiro[1][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] == "X" and tabuleiro[1][4] == "X" and tabuleiro[1][5] == "X" and tabuleiro[1][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[2][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[2][3] == "X" and tabuleiro[2][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][2] == "X" and tabuleiro[2][3] == "X" and tabuleiro[2][4] == "X" and tabuleiro[2][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[2][4] == "X" and tabuleiro[2][5] == "X" and tabuleiro[2][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][0] == "X" and tabuleiro[3][1] == "X" and tabuleiro[3][2] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][1] == "X" and tabuleiro[3][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[3][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[3][4] == "X" and tabuleiro[3][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[3][4] == "X" and tabuleiro[3][5] == "X" and tabuleiro[3][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][0] == "X" and tabuleiro[4][1] == "X" and tabuleiro[4][2] == "X" and tabuleiro[4][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][1] == "X" and tabuleiro[4][2] == "X" and tabuleiro[4][3] == "X" and tabuleiro[4][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][2] == "X" and tabuleiro[4][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[4][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[4][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][0] == "X" and tabuleiro[5][1] == "X" and tabuleiro[5][2] == "X" and tabuleiro[5][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][1] == "X" and tabuleiro[5][2] == "X" and tabuleiro[5][3] == "X" and tabuleiro[5][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][2] == "X" and tabuleiro[5][3] == "X" and tabuleiro[5][4] == "X" and tabuleiro[5][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[5][3] == "X" and tabuleiro[5][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][0] == "X" and tabuleiro[6][1] == "X" and tabuleiro[6][2] == "X" and tabuleiro[6][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][1] == "X" and tabuleiro[6][2] == "X" and tabuleiro[6][3] == "X" and tabuleiro[6][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][2] == "X" and tabuleiro[6][3] == "X" and tabuleiro[6][4] == "X" and tabuleiro[6][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[6][3] == "X" and tabuleiro[6][4] == "X" and tabuleiro[6][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][2] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][1] =="X" and tabuleiro[1][2] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][2] =="X" and tabuleiro[2][3] == "X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] =="X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][2] =="X" and tabuleiro[1][3] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] =="X" and tabuleiro[2][4] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] =="X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] =="X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][3] =="X" and tabuleiro[1][4] == "X" and tabuleiro[2][5] == "X" and tabuleiro[3][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] =="X" and tabuleiro[2][4] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] =="X" and tabuleiro[3][4] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] =="X" and tabuleiro[4][4] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][6] == "X" and tabuleiro[1][5] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][5] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][4] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][5] == "X" and tabuleiro[1][4] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][4] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][4] == "X" and tabuleiro[1][3] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][1] == "X" and tabuleiro[4][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X" and tabuleiro[3][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X" and tabuleiro[3][0] == "X" and tabuleiro[4][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][0] == "X" and tabuleiro[3][0] == "X" and tabuleiro[4][0] == "X" and tabuleiro[5][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][0] == "X" and tabuleiro[4][0] == "X" and tabuleiro[5][0] == "X" and tabuleiro[6][0] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X" and tabuleiro[3][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X" and tabuleiro[3][1] == "X" and tabuleiro[4][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][1] == "X" and tabuleiro[3][1] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][1] == "X" and tabuleiro[4][1] == "X" and tabuleiro[5][1] == "X" and tabuleiro[6][1] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][2] == "X" and tabuleiro[3][2] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][2] == "X" and tabuleiro[4][2] == "X" and tabuleiro[5][2] == "X" and tabuleiro[6][2] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][3] == "X" and tabuleiro[1][3] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][3] == "X" and tabuleiro[2][3] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][3] == "X" and tabuleiro[3][3] == "X" and tabuleiro[4][3] == "X" and tabuleiro[5][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][3] == "X" and tabuleiro[4][3] == "X" and tabuleiro[5][3] == "X" and tabuleiro[6][3] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][4] == "X" and tabuleiro[1][4] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][4] == "X" and tabuleiro[2][4] == "X" and tabuleiro[3][4] == "X" and tabuleiro[4][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][4] == "X" and tabuleiro[3][4] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][4] == "X" and tabuleiro[4][4] == "X" and tabuleiro[5][4] == "X" and tabuleiro[6][4] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][5] == "X" and tabuleiro[1][5] == "X" and tabuleiro[2][5] == "X" and tabuleiro[3][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][5] == "X" and tabuleiro[2][5] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][5] == "X" and tabuleiro[3][5] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][5] == "X" and tabuleiro[4][5] == "X" and tabuleiro[5][5] == "X" and tabuleiro[6][5] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][6] == "X" and tabuleiro[1][6] == "X" and tabuleiro[2][6] == "X" and tabuleiro[3][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[1][6] == "X" and tabuleiro[2][6] == "X" and tabuleiro[3][6] == "X" and tabuleiro[4][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[2][6] == "X" and tabuleiro[3][6] == "X" and tabuleiro[4][6] == "X" and tabuleiro[5][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[3][6] == "X" and tabuleiro[4][6] == "X" and tabuleiro[5][6] == "X" and tabuleiro[6][6] == "X":
            print("Jogador 1 venceu!")
            break
        if tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O" and tabuleiro[0][3] == "O": 
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O" and tabuleiro[0][3] == "O" and tabuleiro[0][4] == "O": 
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][2] == "O" and tabuleiro[0][3] == "O" and tabuleiro[0][4] == "O" and tabuleiro[0][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][3] == "O" and tabuleiro[0][4] == "O" and tabuleiro[0][5] == "O" and tabuleiro[0][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O" and tabuleiro[1][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O" and tabuleiro[1][3] == "O" and tabuleiro[1][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][2] == "O" and tabuleiro[1][3] == "O" and tabuleiro[1][4] == "O" and tabuleiro[1][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] == "O" and tabuleiro[1][4] == "O" and tabuleiro[1][5] == "O" and tabuleiro[1][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[2][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[2][3] == "O" and tabuleiro[2][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][2] == "O" and tabuleiro[2][3] == "O" and tabuleiro[2][4] == "O" and tabuleiro[2][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[2][4] == "O" and tabuleiro[2][5] == "O" and tabuleiro[2][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][0] == "O" and tabuleiro[3][1] == "O" and tabuleiro[3][2] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][1] == "O" and tabuleiro[3][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[3][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[3][4] == "O" and tabuleiro[3][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[3][4] == "O" and tabuleiro[3][5] == "O" and tabuleiro[3][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][0] == "O" and tabuleiro[4][1] == "O" and tabuleiro[4][2] == "O" and tabuleiro[4][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][1] == "O" and tabuleiro[4][2] == "O" and tabuleiro[4][3] == "O" and tabuleiro[4][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][2] == "O" and tabuleiro[4][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[4][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[4][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][0] == "O" and tabuleiro[5][1] == "O" and tabuleiro[5][2] == "O" and tabuleiro[5][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][1] == "O" and tabuleiro[5][2] == "O" and tabuleiro[5][3] == "O" and tabuleiro[5][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][2] == "O" and tabuleiro[5][3] == "O" and tabuleiro[5][4] == "O" and tabuleiro[5][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[5][3] == "O" and tabuleiro[5][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][0] == "O" and tabuleiro[6][1] == "O" and tabuleiro[6][2] == "O" and tabuleiro[6][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][1] == "O" and tabuleiro[6][2] == "O" and tabuleiro[6][3] == "O" and tabuleiro[6][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][2] == "O" and tabuleiro[6][3] == "O" and tabuleiro[6][4] == "O" and tabuleiro[6][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[6][3] == "O" and tabuleiro[6][4] == "O" and tabuleiro[6][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][2] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][1] =="O" and tabuleiro[1][2] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][2] =="O" and tabuleiro[2][3] == "O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] =="O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][2] =="O" and tabuleiro[1][3] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] =="O" and tabuleiro[2][4] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] =="O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] =="O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][3] =="O" and tabuleiro[1][4] == "O" and tabuleiro[2][5] == "O" and tabuleiro[3][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] =="O" and tabuleiro[2][4] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] =="O" and tabuleiro[3][4] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] =="O" and tabuleiro[4][4] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][6] == "O" and tabuleiro[1][5] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][5] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][4] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][5] == "O" and tabuleiro[1][4] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][4] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][4] == "O" and tabuleiro[1][3] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][1] == "O" and tabuleiro[4][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O" and tabuleiro[3][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O" and tabuleiro[3][0] == "O" and tabuleiro[4][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][0] == "O" and tabuleiro[3][0] == "O" and tabuleiro[4][0] == "O" and tabuleiro[5][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][0] == "O" and tabuleiro[4][0] == "O" and tabuleiro[5][0] == "O" and tabuleiro[6][0] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O" and tabuleiro[3][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O" and tabuleiro[3][1] == "O" and tabuleiro[4][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][1] == "O" and tabuleiro[3][1] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][1] == "O" and tabuleiro[4][1] == "O" and tabuleiro[5][1] == "O" and tabuleiro[6][1] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][2] == "O" and tabuleiro[3][2] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][2] == "O" and tabuleiro[4][2] == "O" and tabuleiro[5][2] == "O" and tabuleiro[6][2] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][3] == "O" and tabuleiro[1][3] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][3] == "O" and tabuleiro[2][3] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][3] == "O" and tabuleiro[3][3] == "O" and tabuleiro[4][3] == "O" and tabuleiro[5][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][3] == "O" and tabuleiro[4][3] == "O" and tabuleiro[5][3] == "O" and tabuleiro[6][3] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][4] == "O" and tabuleiro[1][4] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][4] == "O" and tabuleiro[2][4] == "O" and tabuleiro[3][4] == "O" and tabuleiro[4][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][4] == "O" and tabuleiro[3][4] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][4] == "O" and tabuleiro[4][4] == "O" and tabuleiro[5][4] == "O" and tabuleiro[6][4] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][5] == "O" and tabuleiro[1][5] == "O" and tabuleiro[2][5] == "O" and tabuleiro[3][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][5] == "O" and tabuleiro[2][5] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][5] == "O" and tabuleiro[3][5] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][5] == "O" and tabuleiro[4][5] == "O" and tabuleiro[5][5] == "O" and tabuleiro[6][5] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[0][6] == "O" and tabuleiro[1][6] == "O" and tabuleiro[2][6] == "O" and tabuleiro[3][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[1][6] == "O" and tabuleiro[2][6] == "O" and tabuleiro[3][6] == "O" and tabuleiro[4][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[2][6] == "O" and tabuleiro[3][6] == "O" and tabuleiro[4][6] == "O" and tabuleiro[5][6] == "O":
            print("Jogador 2 venceu!")
            break
        if tabuleiro[3][6] == "O" and tabuleiro[4][6] == "O" and tabuleiro[5][6] == "O" and tabuleiro[6][6] == "O":
            print("Jogador 2 venceu!")
            break
        
        
elif opcao == "2":
    print("Em Desenvolvimento...")
elif opcao == "3":
    print("Em Desenvolvimento...")
elif opcao == "4":
    print("Saindo do jogo...")
    exit()
    