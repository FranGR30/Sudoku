from matriz_sudoku import *


def validar_sudoku_fila(matriz_sudoku, f):
    conteos = obtener_conteos(obtener_valores_fila(matriz_sudoku, f))
    for_celda_en_fila(matriz_sudoku, f,
                      lambda x: controlar_estado_celda(x, conteos))


def validar_sudoku_columna(matriz_sudoku, c):
    conteos = obtener_conteos(obtener_valores_columna(matriz_sudoku, c))
    for_celda_en_columna(matriz_sudoku, c,
                         lambda x: controlar_estado_celda(x, conteos))


def validar_sudoku_cuadrante(matriz_sudoku, c1, c2):
    conteos = obtener_conteos(obtener_valores_cuadrante(matriz_sudoku, c1, c2))
    for_celda_en_cuadrante(matriz_sudoku, c1, c2,
                           lambda x: controlar_estado_celda(x, conteos))


def controlar_sudoku_completo(matriz_sudoku):
    cantidad_vacios, cantidad_errores = contar_vacios_y_errores(matriz_sudoku)
    return cantidad_vacios == 0 and cantidad_errores == 0


def validar_sudoku(matriz_sudoku):
    # reiniciamos el estado al iniciar la validacion
    reiniciar_estado_sudoku(matriz_sudoku)
    for f in range(9):
        validar_sudoku_fila(matriz_sudoku, f)
    for c in range(9):
        validar_sudoku_columna(matriz_sudoku, c)
    for c1 in range(3):
        for c2 in range(3):
            validar_sudoku_cuadrante(matriz_sudoku, c1, c2)
    return controlar_sudoku_completo(matriz_sudoku)
