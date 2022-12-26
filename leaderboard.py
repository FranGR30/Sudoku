from menu import *

facil=["carlos","juan"]
movimientosfacil=[60,70]
medio=["mercedes","rocio",]
movimientosmedio=[60,70]
dificil=["nico","nacho"]
movimientosdificil=[60,70]
 


def ganador(cant,dif):
    nombre=input("Felicitaciones, ingrese su nombre: ")
    if dif==1:
        movimientosfacil.append(cant)
        movimientosfacil.sort()
        facil.insert(movimientosfacil.index(cant),nombre)
        
        
    elif dif==2:
        movimientosmedio.append(cant)
        movimientosmedio.sort()
        medio.insert(movimientosmedio.index(cant),nombre)
        
    else:
        movimientosdificil.append(cant)
        movimientosdificil.sort()
        dificil.insert(movimientosdificil.index(cant),nombre)


def tabla(dificultad,movimientos):
    for i, lista in enumerate(dificultad):
        print(i+1,"--",dificultad[i],"----",movimientos[i],"movimientos")
    input("\nPresione Enter para volver al menú...")

def leaderboard():
    opcion= menu_leaderboard()
    limpiar_pantalla()
    if opcion == leaderboard_facil:
        print("--------------SUDOKU--------------")
        print("------------Leaderboard-----------")
        print("---------------Facil--------------")
        tabla(facil,movimientosfacil)
    elif opcion == leaderboard_medio:
        print("--------------SUDOKU--------------")
        print("------------Leaderboard-----------")
        print("---------------Medio--------------")
        tabla(medio,movimientosmedio)
    elif opcion == leaderboard_dificil:
        print("--------------SUDOKU--------------")
        print("------------Leaderboard-----------")
        print("--------------Dificil-------------")
        tabla(dificil,movimientosdificil)
    elif opcion == leaderboard_atras:
        print("Volviendo al menu anterior...")
    return


"""cantidad_jugados=cantidad_jugados+1"""
