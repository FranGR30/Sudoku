# una celda la estamos tomando como una lista de 2 elementos: Valor, y estado
VALOR, ESTADO = 0, 1

# tupla con valores validos para valores de celda
VALORES_VALIDOS = (" ", "1", "2", "3", "4", "5", "6", "7", "8", "9")

# Estados posibles de una celda
ESTADO_VACIO, ESTADO_COMPLETADO, ESTADO_FIJO, ESTADO_INVALIDO, ESTADO_FIJO_WARN = 0, 1, 2, 3, 4
ESTADOS_VALIDOS = (ESTADO_VACIO, ESTADO_COMPLETADO, ESTADO_FIJO, ESTADO_INVALIDO, ESTADO_FIJO_WARN)

# diccionario estado celda -> colores
COLOR_CELDA = {
    ESTADO_VACIO:       "\033[0;0m",   # 
    ESTADO_COMPLETADO:  "\033[0;0m",   # blanco
    ESTADO_INVALIDO:    "\033[0;31m",  # rojo
    ESTADO_FIJO:        "\033[0;32m",  # verde
    ESTADO_FIJO_WARN:   "\033[0;33m",  # amarillo
}

# crear celda

def crear_celda(valor):
    if valor not in VALORES_VALIDOS:
        raise ValueError(f"{valor} no es un valor valido.")
    estado = ESTADO_VACIO if (valor == ' ') else ESTADO_FIJO
    return [valor, estado]

def crear_celda_con_estado(valor, estado):
    if valor not in VALORES_VALIDOS:
        raise ValueError(f"{valor} no es un valor valido.")
    if estado not in ESTADOS_VALIDOS:
        raise ValueError(f"{estado} no es un estado valido.")
    return [valor, estado]

# obtener valor / estado

def obtener_estado(celda):
    return celda[ESTADO]


def obtener_valor(celda):
    return celda[VALOR]

# consultas de estado de la celda

def es_celda_vacia(celda):
    return celda[VALOR] == " "


def es_celda_invalida(celda):
    return celda[ESTADO] == ESTADO_INVALIDO


def es_celda_fija(celda):
    return celda[ESTADO] in (ESTADO_FIJO, ESTADO_FIJO_WARN)

# modificacion valor/estado de la celda

def actualizar_valor_celda(celda, valor):
    if valor not in VALORES_VALIDOS:
        raise ValueError(f"{valor} no es un valor valido.")
    if es_celda_fija(celda):
        raise ValueError("La celda es fija.")
    celda[VALOR] = valor

def reiniciar_estado_celda(celda):
    # valor default. se reajusta durante validaciones.
    if es_celda_vacia(celda):
        celda[ESTADO] = ESTADO_VACIO
    elif es_celda_fija(celda):
        celda[ESTADO] = ESTADO_FIJO
    else:
        celda[ESTADO] = ESTADO_COMPLETADO


def invalidar_estado_celda(celda):
    if es_celda_fija(celda):
        celda[ESTADO] = ESTADO_FIJO_WARN
    else:
        celda[ESTADO] = ESTADO_INVALIDO
