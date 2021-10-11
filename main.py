import json
from interface import *

boards = []
mainBoard = -1
gameBoard = [[]]

def loadData(filename):
    with open(filename) as jsonFile:
        boards = json.load(jsonFile)
        jsonFile.close()
    return boards

def __init__():
    global boards
    boards = loadData("data.json")
    print("Datos cargados!")
    print("Buena suerte!")
    menu()

def menu():

    while True:
        print("\nMENU PRINCIPAL: \n")
        print("1. Escoger tablero")
        print("2. Reglas del juego")
        print("3. Puntuaciones")
        print("4. Salir")

        opt = int(input("\nSeleccione una opcion: "))

        if opt == 1:
            boardsMenu()
        #end if
        if opt == 2:
            rules()
        #end if
        if opt == 3:
            topTimes()
        #end if
        if opt == 4:
            endGame()
            break
        #end if
#end def

def boardsMenu():
    global boards, mainBoard, gameBoard
    print("\nBOARDS MENU: \n")

    for i in range(len(boards)):
        print("Tablero: ",i+1, "Tamanio: ", boards[i]['tamanio'], "Dificultad: ", boards[i]['dificultad'])
    
    while True:
        opc = int(input("Seleccione un tablero: "))

        if opc > 1 or opc < len(boards):
            mainBoard = opc
            break
        else:
            print("Opcion no valida, intente de nuevo")
    
    tam = boards[opc-1]['tamanio']
    gameBoard = [[" "*3 for i in range(tam)]for j in range(tam)]
    printBoard(boards[opc-1]['parametrosX'], boards[opc-1]['parametrosY'], tam, gameBoard)

    game(boards[opc-1])



def fillCell(board):
    global gameBoard
    tam = int(board['tamanio'])
    opc = ""

    while True:
        opc = input("Desea agregar una X(X), llenar una celda (F), limpiar una celda (D): ")

        if opc != "X" and opc != "F" and opc != "D":
            print("Ingrese la opcion nuevamente")
        else:
            break

    cent = True

    while cent:
        cent = False
        col = int(input("Ingrese el numero de la columna: "))
        row = int(input("Ingrese el numero de la fila: "))
        if col < 0 or col > tam:
            print("Se ingresaron mal las columnas")
            cent = True
        if row < 0 or row > tam:
            print("Se ingresaron mal las filas")
            cent = True
        
    if opc == "X":
        gameBoard[row][col] = " X "
    elif opc == "F":
        gameBoard[row][col] = "███"
    else:
        gameBoard[row][col] = "   "
    
    printBoard(board['parametrosX'], board['parametrosY'], tam, gameBoard)
    game(board)

def game(board):
    global gameBoard

    opc = input("Desea continuar con el juego? S/N ")
    if opc == "S":
        fillCell(board)
    else:
        print("Su tiempo fue de: ")
        tam = board['tamanio']
        gameBoard = [[" "*3 for i in range(tam)]for j in range(tam)]
        menu()

def rules():
    print("\nREGLAS: \n")
    print("=================================OBJETIVO=================================")
    print("= El objetivo del juego es rellenar la cuadrícula con cuadrados negros   =")
    print("= para que los números de cuadrados secuenciales rellenos coincidan con  =")
    print("= los números en la parte superior e izquierda.                          =")
    print("==========================================================================")
    print()
    print("==============================¿COMO EMPEZAR?==============================")
    print("= 1. Al iniciar el juego se cargan los parametros del archivo data.json. =")
    print("= 2. Existen tres posibles movimientos para los tableros cargados:       =")
    print("=           - X: Para marcar con una equis una celda.                    =")
    print("=           - F: Para llenar una celda.                                  =")
    print("=           - D: Para limpiar una celda.                                 =")
    print("= 3. Al momento de seleccionar N senialando que no va a continuar el     =")
    print("=   juego, el tablero sera borrado.                                      =")
    print("= 4. Para terminar con la ejecucion del juego basta con seleccionar la   =")
    print("=   de salir en el menu principal.                                       =")
    print("==========================================================================")

def topTimes():
    print("en construccion")

def endGame():
    print("Gracias por jugar!")
    exit()


__init__()