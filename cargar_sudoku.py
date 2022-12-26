from matriz_sudoku import crear_matriz_sudoku, cargar_fila_sudoku, dimensiones_correctas


def cargar_matriz_sudoku(archivo):
    matriz_sudoku = crear_matriz_sudoku()
    for line in archivo:
        cargar_fila_sudoku(matriz_sudoku, line.rstrip("\n").split('|'))
    if not dimensiones_correctas(matriz_sudoku):
        raise ValueError("Archivo invalido. Error en dimensiones de matriz")
    return matriz_sudoku


def cargar_archivo(nombre_archivo):
    """
    Manejo de archivo.
    """
    matriz_sudoku = None
    try:
        archivo_sudoku = open(nombre_archivo, "rt")
        matriz_sudoku = cargar_matriz_sudoku(archivo_sudoku)
    except FileNotFoundError as mensaje:
        print("No se pudo abrir el archivo: ", mensaje)
    except OSError as mensaje:
        print("OSError: ", mensaje)
    except ValueError as mensaje:
        print("Error procesando el archivo.\n", mensaje)
    finally:
        try:
            archivo_sudoku.close()
        except NameError:
            pass
    if matriz_sudoku is None:
        raise ValueError("Error durante la carga del archivo")
    return matriz_sudoku
