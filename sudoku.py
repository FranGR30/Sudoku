from cargar_sudoku import cargar_archivo
from guardar_partida import cargar_partida, guardar_partida
from imprimir_sudoku import print_sudoku
from menu import *
from ingreso import input_valor_sudoku, OPCION_INGRESO_NUM, OPCION_MENU_IN_GAME
from validacion import validar_sudoku
from leaderboard import leaderboard, ganador

# diccionario que mapea dificultad, a nombre de archivo.
SUDOKUS_POR_DIFICULTAD = {
    "FACIL": "sudokuFacil.txt",
    "MEDIO": "sudokuMedio.txt",
    "DIFICIL": "sudokuDificil.txt",
}


def manejo_opcion_menu_ingame(opcion, matriz_sudoku, dificultad, cantidad_jugados):
    """
    resuelve la logica de la opcion escogida en el menu in-game
    """
    continuar_juego = True
    if opcion == MENU_IN_GAME_VOLVER:
        print("Volviendo al juego...")
    elif opcion == MENU_IN_GAME_GUARDAR_Y_SALIR:
        guardado_ok = guardar_partida(matriz_sudoku, dificultad, cantidad_jugados)
        if guardado_ok:
            input("Partida se guardó correctamente. Presione Enter para salir...")
        else:
            input("Ocurrio un error al intentar guardar... Presione Enter para salir...")
        continuar_juego = False
    elif opcion == MENU_IN_GAME_SALIR:
        print("Saliendo del juego...")
        continuar_juego = False
    return continuar_juego


def juego(matriz_sudoku, dificultad, cantidad_jugados=0):
    """
    funcion principal del juego.
    imprime el sudoku, y pide ingreso de usuario en cada ciclo.
    """
    continuar_juego = True
    while continuar_juego:
        limpiar_pantalla()
        print_sudoku(matriz_sudoku)
        try:
            opcion = input_valor_sudoku(matriz_sudoku)
            if opcion == OPCION_INGRESO_NUM:
                cantidad_jugados = cantidad_jugados+1
                resuelto = validar_sudoku(matriz_sudoku)
                if resuelto:
                    print("El sudoku se ha resuelto!")
                    ganador(cantidad_jugados, dificultad)
                    input("Presione Enter para salir...")
                    continuar_juego = False
            elif opcion == OPCION_MENU_IN_GAME:
                opcion_mig = menu_in_game()
                continuar_juego = manejo_opcion_menu_ingame(
                    opcion_mig, matriz_sudoku, dificultad, cantidad_jugados)

        except ValueError as msg:
            input(msg)


def nueva_partida():
    """
    funcion para derivar el nivel de dificultad
    """
    opcion = menu_nueva_partida()
    if opcion == MENU_NUEVA_PARTIDA_FACIL:
        juego(cargar_archivo(SUDOKUS_POR_DIFICULTAD["FACIL"]), opcion)
    elif opcion == MENU_NUEVA_PARTIDA_MEDIO:
        juego(cargar_archivo(SUDOKUS_POR_DIFICULTAD["MEDIO"]), opcion)
    elif opcion == MENU_NUEVA_PARTIDA_DIFICIL:
        juego(cargar_archivo(SUDOKUS_POR_DIFICULTAD["DIFICIL"]), opcion)
    elif opcion == MENU_NUEVA_PARTIDA_ATRAS:
        print("Volviendo al menu anterior...")


def iniciar():
    """
    punto de inicio.
    invoca al menu principal del juego, y deriva segun la opcion elegida.
    """
    opcion = None
    while opcion != MENU_INICIAL_SALIR:
        opcion = menu_inicial()
        if opcion == MENU_INICIAL_NUEVA_PARTIDA:
            nueva_partida()
        elif opcion == MENU_INICIAL_CONTINUAR_PARTIDA:
            try:
                juego(*cargar_partida())
            except ValueError:
                input("Presione Enter para volver...")
        elif opcion == MENU_INICIAL_LEADERBOARD:
            leaderboard()
        elif opcion == MENU_INICIAL_SALIR:
            limpiar_pantalla()
            print("¡Gracias por jugar!")
