from celda import *

# creacion de matriz


def crear_matriz_sudoku():
    return []


def cargar_fila_sudoku(matriz, datos_fila):
    fila = []
    for dato in datos_fila:
        fila.append(crear_celda(dato))
    if len(fila) != 9:
        raise ValueError("Fila de tamaño invalido: ", datos_fila)
    matriz.append(fila)


def dimensiones_filas_correctas(matriz, f):
    # recursividad.
    # la idea es que se invoque con 0, y por recursividad se llame a 1, 2, ..., 8.
    # cuando el numero de fila sea 8, significa que llegamos al final.
    if f == 8: # caso base: la ultima fila.
        return len(matriz[f]) == 9
    return (len(matriz[f]) == 9) and dimensiones_filas_correctas(matriz, f + 1)   

def dimensiones_correctas(matriz):
    return (len(matriz) == 9) and dimensiones_filas_correctas(matriz, 0)

# obtencion de valores en rango

def obtener_valores_fila(matriz, f):
    return [obtener_valor(celda) for celda in matriz[f]]


def obtener_valores_columna(matriz, c):
    return [obtener_valor(fila[c]) for fila in matriz]


def obtener_valores_cuadrante(matriz, c1, c2):
    return [obtener_valor(matriz[f][c])
            for f in range(3*c1, 3*c1 + 3)
            for c in range(3*c2, 3*c2 + 3)]


def obtener_conteos(lista_valores):
    return {k: lista_valores.count(k) for k in VALORES_VALIDOS}


def celda_formato_guardado(celda):
    return f"{obtener_valor(celda)},{str(obtener_estado(celda))}\n"


def cargar_celda_formato_guardado(matriz_sudoku, line):
    valor, estado = line.rstrip("\n").split(",")
    if len(matriz_sudoku) == 0 or len(matriz_sudoku[-1]) == 9:
        matriz_sudoku.append([])  # nueva fila
    celda = crear_celda_con_estado(valor, int(estado))
    matriz_sudoku[-1].append(celda)  # al final de la matriz


def contar_vacios_y_errores(matriz):
    cantidad_vacios = 0
    cantidad_errores = 0
    for fila in matriz:
        for celda in fila:
            if es_celda_vacia(celda):
                cantidad_vacios += 1
            elif es_celda_invalida(celda):
                cantidad_errores += 1
    return cantidad_vacios, cantidad_errores

# actualizar celda en matriz


def actualizar_matriz(matriz, f, c, val):
    actualizar_valor_celda(matriz[f][c], val)


def reiniciar_estado_sudoku(matriz_sudoku):
    for fila in matriz_sudoku:
        for celda in fila:
            reiniciar_estado_celda(celda)


def controlar_estado_celda(celda, conteos):
    # conteos es un diccionario:  valor celda -> cantidad de apariciones.
    apariciones = conteos[obtener_valor(celda)]
    if apariciones >= 2:
        invalidar_estado_celda(celda)

# for's especializados para fila, columna y cuadrante.


def for_celda_en_fila(matriz_sudoku, f, func):
    for celda in matriz_sudoku[f]:
        func(celda)


def for_celda_en_columna(matriz_sudoku, c, func):
    for fila in matriz_sudoku:
        func(fila[c])


def for_celda_en_cuadrante(matriz_sudoku, c1, c2, func):
    for f in range(3*c1, 3*c1 + 3):
        for c in range(3*c2, 3*c2 + 3):
            func(matriz_sudoku[f][c])

# formato impresion celda


def print_celda_color(celda):
    print(COLOR_CELDA[obtener_estado(celda)], " ",
          obtener_valor(celda), sep="", end="")
