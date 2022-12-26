def limpiar_pantalla():
    CLEAR_SCREEN = "\033c"
    print(CLEAR_SCREEN, end="")

## menu inicial ##

MENU_INICIAL_NUEVA_PARTIDA = 1
MENU_INICIAL_CONTINUAR_PARTIDA = 2
MENU_INICIAL_LEADERBOARD = 3
MENU_INICIAL_SALIR = 4
OPCIONES_MENU_INICIAL = ("1", "2", "3", "4")

def print_menu_inicial():
    print("--------------SUDOKU--------------")
    print(" 1 - Comenzar nueva partida")
    print(" 2 - Continuar partida")
    print(" 3 - Leaderboard")
    print(" 4 - Salir")
    print("----------------------------------")

def input_opcion_menu_inicial():
    opcion = input("\nIngrese la opción escogida: ")
    while opcion not in OPCIONES_MENU_INICIAL:
        opcion = input("\nError. Ingrese una opción válida: ")
    return int(opcion)

def menu_inicial():
    limpiar_pantalla()
    print_menu_inicial()
    return input_opcion_menu_inicial()

## menu nueva partida ##

MENU_NUEVA_PARTIDA_FACIL = 1
MENU_NUEVA_PARTIDA_MEDIO = 2
MENU_NUEVA_PARTIDA_DIFICIL = 3
MENU_NUEVA_PARTIDA_ATRAS = 4
OPCIONES_MENU_NUEVA_PARTIDA = ("1", "2", "3", "4")

def print_menu_nueva_partida():
    print("--------------SUDOKU--------------")
    print(" Seleccione nivel de dificultad:")
    print(" 1 - Fácil")
    print(" 2 - Medio")
    print(" 3 - Dificil")
    print(" 4 - Atrás")
    print("----------------------------------")

def input_opcion_menu_nueva_partida():
    opcion = input("\nIngrese la opción escogida: ")
    while opcion not in OPCIONES_MENU_NUEVA_PARTIDA:
        opcion = input("Error. Ingrese una opción válida: ")
    return int(opcion)

def menu_nueva_partida():
    limpiar_pantalla()
    print_menu_nueva_partida()
    return input_opcion_menu_nueva_partida()

## menu_in_game

MENU_IN_GAME_VOLVER = 1
MENU_IN_GAME_GUARDAR_Y_SALIR = 2
MENU_IN_GAME_SALIR = 3
OPCIONES_MENU_IN_GAME = ("1", "2", "3")

def print_menu_in_game():
    print("--------------SUDOKU--------------")
    print(" Seleccione opcion:")
    print(" 1 - Volver al juego")
    print(" 2 - Guardar el juego y salir")
    print(" 3 - Salir al menu principal")
    print("----------------------------------")

def input_opcion_menu_in_game():
    opcion = input("\nIngrese la opción escogida: ")
    while opcion not in OPCIONES_MENU_IN_GAME:
        opcion = input("Error. Ingrese una opción válida: ")
    return int(opcion)

def menu_in_game():
    limpiar_pantalla()
    print_menu_in_game()
    return input_opcion_menu_in_game()

##  menu leaderboard

leaderboard_facil = 1
leaderboard_medio = 2
leaderboard_dificil = 3
leaderboard_atras = 4
leaderboard_lista = ("1", "2", "3", "4")

def print_leaderboard():
    print("--------------SUDOKU--------------")
    print("------------Leaderboard-----------")
    print(" Seleccione nivel de dificultad:")
    print(" 1 - Fácil")
    print(" 2 - Medio")
    print(" 3 - Dificil")
    print(" 4 - Atrás")
    print("----------------------------------")

def input_leaderboard():
    opcion = input("\nIngrese la opción escogida: ")
    while opcion not in leaderboard_lista:
        opcion = input("\nError. Ingrese una opción válida: ")
    return int(opcion)

def menu_leaderboard():
    limpiar_pantalla()
    print_leaderboard()
    return input_leaderboard()