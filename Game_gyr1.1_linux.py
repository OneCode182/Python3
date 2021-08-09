# *** RECURSOS ***

import time
import random as ran
from os import system


# *** FUNCIONES BASE *** 

def clean(): # Limpia la consola
    system("clear")

def time1(var): # Pausa de tiempo
    time.sleep(var)



# *** DATOS ***

# Intro

intro =     ("El juego consiste en un tablero donde está el Gato y el Raton",
            "Ambos aparecen al inicio de forma aleatoria",
            "Gato puede estar en las esquinas inferiores",
            "Raton en la primer fila",
            "Gato se mueve en diagonal y en una ruta unica depende de su posicion inicial",
            "Raton se mueve en cruz",
            "Gato se puede quedar dormido, si es asi, se queda quieto hasta despertar",
            "Si raton intenta moverse fuera del tablero, se hace un chichon y no se mueve hasta la siguiente jugada",   
            "Si gato y raton estan en la misma casilla, pero gato esta dormido, no pasa nada...",        
            "Si al contrario, esta despierto, raton es comido por gato, y se pierde la partida",
            "Tambien se pierde si se acaban los intentos...",
            "Para ganar, raton debe llegar a la salida antes de que se lo coman",
            "!!! Suerte !!!"
)

# General
c = 0
mensaje_f = 0
mensaje_f2 = "Se han acabado los intentos"
mensaje_f3 = "Gato se ha comido al Raton"
mensaje_f4 = "Raton ha llegado a la salida"
mensaje_st = 0
final_st = True # T => Juego Ganado, F => Juego Perdido
g_r = False # Gato despierto y raton en misma casilla
s_r = False # Raton en salida
t = [] # Tablero

# Gato 
gato_x, gato_y = 0, 0 # Coordenadas
gato_pos = 0 # Posicion Inicial (1 = esquina inf izq, 2 == esquina inf der)
gato_st = True # T = Despierto, F = Dormido
gato_symbol = 0 # Simbolo Real
gato_symbol2 = 0 # Simbolo Estadistica

# Raton
raton_x, raton_y = 0, 0 # Coordenadas
raton_ch = 0 # Chichones
raton_st = True # T = Normal, F = Noqueado
raton_symbol = 0 # Simbolo Real
raton_symbol2 = 0 # Simbolo Estadistica

# Salida
salida_x, salida_y = 0, 0 # Coordenadas
salida_symbol = "S" # Simbolo




# *** JUEGO *** 

# Intro
clean()
print("*** Bienvenido al juego del Gato y el Raton! ***")

# Omitir intro
while True:

    intro_in = input("Omitir intro? (S/n) => ")
    intro_r = intro_in.lower()
    clean()

    if (intro_r != "s") and (intro_r != "n"):
        print("Escribe un valor correcto...")
        continue

    elif intro_r == "s":
        break

    elif intro_r == "n":
        for i in intro:
            time1(3)
            print(f"{i}\n")

        print("Presiona enter para continuar", end="")
        a22 = input()
        break



while True:

    clean()
    # Entradas de dimension del tablero e intentos
    dimension_r = False
    intentos_r = False

    while (dimension_r and intentos_r) == False:
        try:
            if dimension_r == False:
                dimension_t = int(input("Ingresa la dimensión del tablero (entre 4 a 10) ==> "))
                if (dimension_t >= 4) and (dimension_t <= 10):
                    dimension_r = True
                else:
                    clean()
                    print("Escribe un numero entre 4 a 10...")
                        
            if intentos_r == False and dimension_r == True:
                intentos = int(input("Ingresa la cantidad de intentos (entre 10 a 250) ==> "))
                if (intentos >= 10) and (intentos <= 250):
                    intentos_r = True
                else:
                    clean()
                    print("Escribe un numero entre 10 a 250...")
                
        except ValueError:
            clean()
            print("Escribe un numero, no un caracter...")
    
    clean()
        


    # Creacion de la matriz
    for i in range(dimension_t): 
        t.append([])
        for j in range(dimension_t):
            t[i].append("*")


    # Coordenadas iniciales
    gato_x, gato_y = ran.choice([1, dimension_t]), dimension_t # Random Gato
    raton_x, raton_y = ran.randint(1, dimension_t), 1 # Random Raton


    # Random salida
    salida_y = dimension_t
    if gato_x == 1:
        salida_x = ran.randint(2, dimension_t)
        gato_pos = 1
    else:
        salida_x = ran.randint(1, (dimension_t - 1))
        gato_pos = 2



    while True:

        b = ran.choice([True, False]) # Random mov de gato
        r = ran.choice([1, 2, 3, 4]) # Random mov de Raton

        # Movimientos Gato (En diagonal)
        if c == 1 and gato_st == True: # Comprueba desde 2da vuelta, y si gato está despierto
            if gato_pos == 1: # Ruta barra invertida \
                if (gato_x == 1) and (gato_y == dimension_t): # Esquina Inferior Izquierda
                    # Diagonal arriba derecha
                    gato_x += 1
                    gato_y -= 1

                elif (gato_x == dimension_t) and (gato_y == 1): # Esquina Superior Derecha
                    # Diagonal abajo izquierda
                    gato_x -= 1
                    gato_y += 1
                
                else: # Si no esta en las esquinas, pero en la ruta \
                    # Movimiento random
                    if b == True:
                        # Diagonal arriba derecha
                        gato_x += 1
                        gato_y -= 1
                    else:
                        # Diagonal abajo izquierda
                        gato_x -= 1
                        gato_y += 1

            else: # Ruta barra derecha /
                if (gato_x and gato_y) == dimension_t: # Esquina Inferior Derecha
                    # Diagonal arriba izquierda
                    gato_x -= 1
                    gato_y -= 1

                elif (gato_x and gato_y) == 1: # Esquina Superior Izquierda
                    # Diagonal abajo derecha
                    gato_x += 1
                    gato_y += 1
                
                else: # Si no esta en las esquinas, pero en la ruta /
                    # Movimiento random
                    if b == True:
                        # Diagonal arriba izquierda
                        gato_x -= 1
                        gato_y -= 1
                    else:
                        # Diagonal abajo derecha
                        gato_x += 1
                        gato_y += 1
        
        
        # Movimientos Raton (En cruz)
        if c == 1 and raton_st == True: # Comprueba desde 2da vuelta, y si raton está bien
            if r == 1: # Intenta ir hacia arriba
                if raton_y == 1: # Si no puede, chichon +1 y se queda quieto
                    raton_ch += 1
                    raton_st = False
                else: # Si puede, se mueve
                    raton_y -= 1

            elif r == 3: # Intenta ir hacia la derecha
                if raton_x == dimension_t: # Si no puede, chichon +1 y se queda quieto
                    raton_ch += 1
                    raton_st = False
                else: # Si puede, se mueve
                    raton_x += 1

            elif r == 2: # Intenta ir hacia abajo
                if raton_y == dimension_t: # Si no puede, chichon +1 y se queda quieto
                    raton_ch += 1
                    raton_st = False
                else: # Si puede, se mueve
                    raton_y += 1

            elif r == 4: # Intenta ir hacia la izquierda
                if raton_x == 1: # Si no puede, chichon +1, y se queda quieto
                    raton_ch += 1
                    raton_st = False
                else: # Si puede, se mueve
                    raton_x -= 1

        if c == 0:
            c += 1 # Hace que Gato y Raton se muevan despues de la 1ra vuelta
            

        
        # Comprobamos Estado Gato
        if gato_st == True:
            gato_symbol = "G"
            gato_symbol2 = "Despierto"
        else:
            gato_symbol = "g" 
            gato_symbol2 = "Dormido"
        

        # Comprobamos Estado Raton
        if raton_st == True:
            raton_symbol = "R"
            raton_symbol2 = "Normal"
        else:
            raton_symbol = "r"
            raton_symbol2 = "Noqueado"




        # Actualizando Tablero
        t[gato_y-1][gato_x-1] = gato_symbol # Gato
        t[salida_y-1][salida_x-1] = salida_symbol # Salida

        # Raton
        if (gato_x == raton_x) and (gato_y == raton_y): # Comprueba si gato y raton en misma coordenada
            t[raton_y - 1][raton_x - 1] = f"{gato_symbol}*{raton_symbol}" # Los imprime como (G*R)
            if gato_st == True:
                g_r = True
        
        elif (raton_x == salida_x) and (raton_y == salida_y):
            t[raton_y - 1][raton_x - 1] = f"{salida_symbol}*{raton_symbol}"
            s_r = True

        else: # Si estan en diferente coordenada
            t[raton_y - 1][raton_x - 1] = raton_symbol

        


        # Estadisticas
        a = [   "Juego\n",
                f"Intentos => {intentos}",
                f"Tablero => {dimension_t}x{dimension_t}",
                "- " * 20,
                "Gato\n",
                f"Coordenadas => ({gato_x},{gato_y})",
                f"Estado => {gato_symbol2}",
                "- " * 20,
                "Raton\n",
                f"Coordenadas => ({raton_x},{raton_y})",
                f"Estado => {raton_symbol2}",
                f"Chichones => {raton_ch}"
            ]
        

        # Impresion del tablero
        for i in range(dimension_t):
            for j in range(dimension_t):
                print(f"\t{t[i][j]}", end="")
            print("\n\n")


        # Impresion de las estadisticas
        for i in a:
            print(f"\t{i}")


        # Actualizando Estados
        gato_st = ran.choice([True, False, True]) # Gato
        raton_st = True
        
        # Borrando Simbolos
        t[gato_y - 1][gato_x - 1] = "*" 
        t[raton_y - 1][raton_x - 1] = "*"
        


        
            
        # Espera y limpieza
        time1(1)
        clean()


        # Logica Final
        if g_r == False:
            if intentos == 0:
                mensaje_f = mensaje_f2
                final_st = False
                break
            elif intentos > 0:
                intentos -= 1
        else:
            mensaje_f = mensaje_f3
            final_st = False
            break

        if s_r == True:
            mensaje_f = mensaje_f4
            final_st = True
            break



    # *** Fin de la partida ***

    # Logica de Juego Ganado/Perdido
    if final_st == True:
        mensaje_st = "Haz ganado"
    else:
        mensaje_st = "Haz perdido"

    print("\n=" + "=" * 39)
    print(f"{mensaje_f} !\n\n{mensaje_st} !")
    time1(4)

    while True: 
        final_q = input("Desea jugar de nuevo? (S/n) => ")
        final_r = final_q.lower()
        clean()

        if (final_r != "s") and (final_r != "n"):
            print("Escribe una opcion valida...")
            continue

        else:
            break
    

    # Verificacion de si desea jugar de nuevo
    if final_r == "s":

        # Reset de estadisticas
        t[salida_y - 1][salida_x - 1] = "*"
        c, mensaje_f ,mensaje_st = 0, 0, 0
        final_st, g_r, s_r = True, False, False
        t = []
        gato_x, gato_y, raton_x, raton_y = 0, 0, 0, 0
        raton_ch, raton_symbol, raton_symbol2 = 0, 0, 0
        gato_pos, gato_symbol, gato_symbol2  = 0, 0, 0
        gato_st, raton_st = True, True
        salida_x, salida_y = 0, 0

        continue

    else:
        break




# *** FIN DEL JUEGO ***
print("*** JUEGO TERMINADO ***")
time1(3)



