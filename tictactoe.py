def menu():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1], tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1], tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1], tabuleiro[2][2]))


def validarVitoria(rodada):
     global parar
     if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        menu()
        print("O Jogador em {} Venceu o jogo!".format(rodada))
        parar = True

     if(tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][2] == rodada):
            menu()
            print("O Jogador em {} Venceu o jogo!".format(rodada))
            parar = True

     if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
            menu()
            print("O Jogador em {} Venceu o jogo!".format(rodada))
            parar = True

     if(tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada):
            menu()
            print("O Jogador em {} Venceu o jogo!".format(rodada))
            parar = True

     if(tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][1] == rodada):
                menu()
                print("O Jogador em {} Venceu o jogo!".format(rodada))
                parar = True

     if(tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro[2][2] == rodada):
                    menu()
                    print("O Jogador em {} Venceu o jogo!".format(rodada))
                    parar = True

     if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada):
                    menu()
                    print("O Jogador em {} Venceu o jogo!".format(rodada))
                    parar = True

     if(tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[0][2] == rodada):
                    menu()
                    print("O Jogador em {} Venceu o jogo!".format(rodada))
                    parar = True

tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
              [" ", " ", " "]]

parar = False
rodada = "X"
jogadas = 0

while parar == False:
    if jogadas == 9:
            menu()
            print("Jogo Empatado!")
            parar = True

    menu()

    linha = int(input("Digite a sua linha escolhida>"))
    coluna = int(input("Digite a sua coluna escolhida>"))

    if rodada == "X":
        tabuleiro [linha][coluna] = "X"
        validarVitoria(rodada)
        jogadas += 1
        rodada = "O"

    elif rodada == "O":
        tabuleiro [linha][coluna] = "O"
        validarVitoria(rodada)
        jogadas += 1
        rodada = "X"


print("Jogo Encerrado.")