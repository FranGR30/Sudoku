from matriz_sudoku import actualizar_matriz

# opciones de navegacion durante el juego
OPCION_INGRESO_NUM = 1
OPCION_MENU_IN_GAME = 2

def input_valor_sudoku(matriz_sudoku):
    """
    funcion para recibir ingreso del usuario durante el juego.
    el usuario puede escribir 'menu' para ir al menu in-game
    o ingresar una tupla de 3 valores: fila, columna y valor de celda.
    """
    print("\nRecuerde que puede abrir el menu del juego, escribiendo 'menu' ")
    opcion = None
    i, j, val = 0, 0, 0

    ingreso = input("ingrese la fila, la columna y el valor (Ej: 1,9,5): ")
    try:
        if ingreso == "menu":
            opcion = OPCION_MENU_IN_GAME
        else:
            opcion = OPCION_INGRESO_NUM
            ingreso = ingreso.replace(' ', '')
            i, j, val = ingreso.split(",")
    except ValueError:
        raise ValueError(
            "Error en el ingreso. No se pudo comprender su orden. Enter para continuar...")

    if opcion == OPCION_INGRESO_NUM:
        f, c = int(i) - 1, int(j) - 1
        if f not in range(9):
            raise ValueError(
                "Error en el ingreso. Las filas van de 1 a 9. Enter para continuar...")

        if c not in range(9):
            raise ValueError(
                "Error en el ingreso. Las columnas van de 1 a 9. Enter para continuar...")
        try:
            actualizar_matriz(matriz_sudoku, f, c, val)
        except ValueError as msg:
            raise ValueError(f"Error en el ingreso. {msg} Enter para continuar...")

    return opcion
