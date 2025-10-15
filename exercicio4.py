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
    
    linha1 = [" ", " ", " "]
    linha2 = [" ", " ", " "]
    linha3 = [" ", " ", " "]
    tabuleiro = [linha1, linha2, linha3]
    
    while True:
    
        print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])
        print("---------")
        print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])
        print("---------")
        print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])
        
        while True:
            jogador_primario_linha = int(input("Jogador 1, escolha a linha (0, 1 ou 2): "))
            jogador_primario_coluna = int(input("Jogador 1, escolha a coluna (0, 1 ou 2): "))
            
            if tabuleiro[jogador_primario_linha][jogador_primario_coluna] == " " :
                tabuleiro[jogador_primario_linha][jogador_primario_coluna] = "X"
                break
            else:
                print("Posição já ocupada, escolha outra.")
        
        print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])
        print("---------")
        print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])
        print("---------")
        print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])
        
        if tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X":
            print("\nJogador 1 venceu!")
            break
        elif tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X":
            print("\nJogador 1 venceu!")
            break
        elif tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X":
            print("\nJogador 1 venceu!")
            break
        elif tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X":
            print("\nJogador 1 venceu!")
            break
        elif tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X":
            print("\nJogador 1 venceu!")
            break
        elif tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
            print("\nJogador 1 venceu!")
            break
        elif tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X":
            print("\nJogador 1 venceu!")
            break
        elif tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O":
            print("\nJogador 2 venceu!")
            break
        elif tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O":
            print("\nJogador 2 venceu!")
            break
        elif tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O":
            print("\nJogador 2 venceu!")
            break
        elif tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O":
            print("\nJogador 2 venceu!")
            break
        elif tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O":
            print("\nJogador 2 venceu!")
            break
        elif tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O":
            print("\nJogador 2 venceu!")
            break
        elif tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O":
            print("\nJogador 2 venceu!")
            break
        elif tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O":
            print("\nJogador 2 venceu!")
            break
        
        
        while True:
            
            jogador_secundario_linha = int(input("Jogador 2, escolha a linha (0, 1 ou 2): "))
            jogador_secundario_coluna = int(input("Jogador 2, escolha a coluna (0, 1 ou 2): "))
            
            if tabuleiro[jogador_secundario_linha][jogador_secundario_coluna] == " " :
                tabuleiro[jogador_secundario_linha][jogador_secundario_coluna] = "O"
                break
            else:
                print("Posição já ocupada, escolha outra.")

        if tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X":
            print("Jogador 1 venceu!")
            break
        elif tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O":
            print("Jogador 2 venceu!")
            break
        elif tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O":
            print("Jogador 2 venceu!")
            break
        elif tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O":
            print("Jogador 2 venceu!")
            break
        elif tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O":
            print("Jogador 2 venceu!")
            break
        elif tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O":
            print("Jogador 2 venceu!")
            break
        elif tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O":
            print("Jogador 2 venceu!")
            break
        elif tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O":
            print("Jogador 2 venceu!")
            break
        elif tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O":
            print("Jogador 2 venceu!")
            break
        
elif opcao == "2":
    print("Em Desenvolvimento...")
elif opcao == "3":
    print("Em Desenvolvimento...")
elif opcao == "4":
    print("Saindo do jogo...")
    exit()
    