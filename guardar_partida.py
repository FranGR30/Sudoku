from matriz_sudoku import *

ARCHIVO_DE_GUARDADO = "partida_guardada.txt"


def guardar_partida(matriz_sudoku, dificultad, cantidad_jugados):
    guardado_ok = False
    try:
        archivo_sudoku = open(ARCHIVO_DE_GUARDADO, "wt")
        archivo_sudoku.write(f"{dificultad},{cantidad_jugados}\n")
        for fila in matriz_sudoku:
            for celda in fila:
                archivo_sudoku.write(celda_formato_guardado(celda))
    except FileNotFoundError as mensaje:
        print("No se pudo abrir el archivo: ", mensaje)
    except OSError as mensaje:
        print("OSError: ", mensaje)
    except ValueError as mensaje:
        print("Error procesando el archivo.\n", mensaje)
    finally:
        try:
            archivo_sudoku.close()
            guardado_ok = True
        except NameError:
            pass
    return guardado_ok

def convertir_primera_linea(linea):
    dificultad, cantidad = linea.rstrip("\n").split(",")
    return int(dificultad), int(cantidad)

def cargar_partida():
    matriz_sudoku = None
    dificultad = None
    cantidad_movimientos = None
    try:
        matriz_sudoku = crear_matriz_sudoku()
        archivo_sudoku = open(ARCHIVO_DE_GUARDADO, "rt")
        dificultad, cantidad_movimientos = convertir_primera_linea(archivo_sudoku.readline())
        for line in archivo_sudoku:
            cargar_celda_formato_guardado(matriz_sudoku, line)
        if not dimensiones_correctas(matriz_sudoku):
            raise ValueError("Error en dimensiones de matriz.")
    except FileNotFoundError as mensaje:
        print("No hay partida guardada")
        raise ValueError()
    except OSError as mensaje:
        print("Error de OS inesperado: ", mensaje)
        raise ValueError()
    except ValueError as mensaje:
        print("Error procesando el archivo.\n", mensaje)
        raise ValueError()
    finally:
        try:
            archivo_sudoku.close()
        except NameError:
            pass
    return matriz_sudoku, dificultad, cantidad_movimientos
