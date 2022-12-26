from matriz_sudoku import print_celda_color
from os import system  # solamente se usa en la linea siguiente
system("")  # habilitar secuencias de escape ANSI (para colores)


def print_caracter_marco():
    COLOR_MARCO = "\033[0;36m"
    print(COLOR_MARCO, "|", end="", sep="")


def print_marco_linea_horizontal():
    COLOR_MARCO = "\033[0;36m"
    separador_horizontal = "+-------+-------+-------+"
    print(COLOR_MARCO, separador_horizontal, sep="")


def desactivar_color():
    COLOR_OFF = "\033[0;0m"
    print(COLOR_OFF)  # para apagar los colores


def print_fila_sudoku(fila):
    print_caracter_marco()
    for c, celda in enumerate(fila):
        print_celda_color(celda)
        if c % 3 == 2:  # cada 3 celdas imprimir separador
            print(" ", end="")
            print_caracter_marco()
    print(" ")  # salto de linea


def print_sudoku(matriz_sudoku):
    print_marco_linea_horizontal()
    for f, fila in enumerate(matriz_sudoku):
        print_fila_sudoku(fila)
        if f % 3 == 2:  # cada 3 filas, imprimir separador
            print_marco_linea_horizontal()
    desactivar_color()



