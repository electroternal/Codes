import random
import os

#########################################################################
# La tabla en una lista para dibujar el juego
TTTboard = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n",
            " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " "]

#########################################################################
# Un diccionario con los indices de la tabla para cambiar los valores
DicGamSpace = {1:13, 2:17, 3:21, 4:61, 5:65, 6:69, 7:109, 8:113, 9:117}
ListGamSpace = [13, 17, 21, 61, 65, 69, 109, 113, 117]
checkWon = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9], 4:[1,4,7], 5:[2,5,8], 6:[3,6,9], 7:[1,5,9], 8:[3,5,7]}
#########################################################################
# Funciones
def BoardInstructions():
    # imprime las intrucciones para jugar
    os.system('cls')
    board = TTTboard
    Posboard = ""
    SelectNum = 1
    for x in ListGamSpace:
        board[x] = str(SelectNum)
        SelectNum += 1
    for x in board:
        Posboard += x
    return print(Posboard)

def SelRandPlayer(num):
    # Seleccionar el jugador aleatoreamente para iniciar
    randnum = 0
    if num == 1 or num == 2:
        randnum = random.randrange(1,3)
        if randnum == 1:
            print("Juega X Primero")
            return "Xply"
        else:
            print("Juega O Primero")
            return "Oply"
    else:
        return 0

def checkGame(num1):
    # Verificar si uno de los  jugadores ha ganado
    for x in checkWon:
        set1 = checkWon[x]
        set2 = set(num1) & set(set1)
        if len(set2) == 3:
            return "Won"
    return "lose"
    

def printXOtabla(value, player):
    #imprime X u O en la tabla dependiendo el indice y el jugador Xply o Oply
    if player == 'Xply':
        if value in DicGamSpace:
            TTTboard[DicGamSpace[value]] = "X"
        else:
            return print("input Number not between 1 to 9")
    elif player == "Oply":
        if value in DicGamSpace:
            TTTboard[DicGamSpace[value]] = "O"
        else:
            return print("input Number not between 1 to 9")
    boardA = ""
    for x in TTTboard:
        boardA += x
    return print(boardA)


GameOff = True
StartingGame = True
playedNum = []
Xplynum = []
Oplynum = []

while GameOff == True:

    if StartingGame == True:
        BoardInstructions()
        print("")
        InPutnumPly = int(input("Un jugador escriba 1 o 2 para seleccionar el que iniciará => "))
        player = SelRandPlayer(InPutnumPly)
        StartingGame = False

    elif player == "Xply" and GameOff == True and StartingGame == False:
        InPutnum = int(input("Turno para X, seleccionar del 1 al 9 => "))
        if InPutnum not in playedNum:
            playedNum.append(InPutnum)
            Xplynum.append(InPutnum)
            if len(playedNum) < 9:
                if len(Xplynum) >= 3 and checkGame(Xplynum) == "Won":
                    os.system('cls')
                    printXOtabla(InPutnum,player)
                    continueorNot = input("¡¡¡---X Won---!!!\nescribe ---yes--- para comenzar otra vez ---no--- para terminar => ")
                    if continueorNot.lower() == "yes":
                        GameOff = True
                        StartingGame = True
                        playedNum = []
                        Xplynum = []
                        Oplynum = []
                    else:
                        GameOff = False
                        StartingGame = True
                        playedNum = []
                        Xplynum = []
                        Oplynum = []
                os.system('cls')
                printXOtabla(InPutnum,player)
                player = "Oply"
            else:
                os.system('cls')
                printXOtabla(InPutnum,player)
                continueorNot = input("----Empate----\nescribe ---yes--- para comenzar otra vez ---no--- para terminar => ")
                if continueorNot.lower() == "yes":
                    GameOff = True
                    StartingGame = True
                    playedNum = []
                    Xplynum = []
                    Oplynum = []
                else:
                    GameOff = False
                    StartingGame = True
                    playedNum = []
                    Xplynum = []
                    Oplynum = []
        else:
            print("Ese espacio ya está Jugado")

    elif player == "Oply" and GameOff == True and StartingGame == False:
        InPutnum = int(input("Turno para O, seleccionar del 1 al 9 => "))
        if InPutnum not in playedNum:
            playedNum.append(InPutnum)
            Oplynum.append(InPutnum)
            if len(playedNum) < 9:
                if len(Oplynum) >= 3 and checkGame(Oplynum) == "Won":
                    os.system('cls')
                    printXOtabla(InPutnum,player)
                    continueorNot = input("¡¡¡---O Won---!!!\nescribe ---yes--- para comenzar otra vez ---no--- para terminar => ")
                    if continueorNot.lower() == "yes":
                        GameOff = True
                        StartingGame = True
                        playedNum = []
                        Xplynum = []
                        Oplynum = []
                    else:
                        GameOff = False
                        StartingGame = True
                        playedNum = []
                        Xplynum = []
                        Oplynum = []
                os.system('cls')
                printXOtabla(InPutnum,player)
                player = "Xply"
            else:
                os.system('cls')
                printXOtabla(InPutnum,player)
                continueorNot = input("----Empate----\nescribe ---yes--- para comenzar otra vez ---no--- para terminar => ")
                if continueorNot.lower() == "yes":
                    GameOff = True
                    StartingGame = True
                    playedNum = []
                    Xplynum = []
                    Oplynum = []
                else:
                    GameOff = False
                    StartingGame = True
                    playedNum = []
                    Xplynum = []
                    Oplynum = []
        else:
            print("Ese espacio ya está Jugado")

    else:
        if GameOff == False:
            print("End of Game")


    

