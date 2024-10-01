import py5

lista = [1, 4, 7, 2, 5, 9, 3]

#Variables de indíces para controlar los algoritmos
i = 0
j = 0
ancho_barra = 40  # Ancho de cada barra
espacio_barra = 5  # Espacio entre las barras

def setup():
    py5.size(600, 400) #Definir tamaño canva
    py5.frame_rate(1) #Controlar la velocidad de la animación, a cuantos frames x segundo se va a actualizar el draw.

def draw():
    global i, j, lista #Global para acceder a las variables de manera global y permitir su modificación en el código de manera local (en una función)
    py5.background(200) # Establece el color de fondo 

    # Dibujar las barras de la lista
    for index, value in enumerate(lista):
        x = index * (ancho_barra + espacio_barra) + 50  # Posición en X
        altura = value * 10  # La altura de la barra es proporcional al valor
        py5.fill(100, 150, 255)  # Color estándar de las barras
        
        # Resaltar los elementos que están siendo comparados en amarillo
        if index == j or index == j + 1:
            py5.fill(255, 255, 100)  # Amarillo para resaltar la comparación actual

        # Zona ordenada (verde)
        if index >= len(lista) - i:
            py5.fill(100, 255, 100)  # Verde para la parte ya ordenada

        # Dibujar cada barra
        py5.rect(x, py5.height - altura, ancho_barra, altura)
    
    # Mostrar la zona ordenada con una línea verde
    py5.stroke(0, 200, 0)
    py5.line((len(lista) - i) * (ancho_barra + espacio_barra) + 50, 0, (len(lista) - i) * (ancho_barra + espacio_barra) + 50, py5.height)

    # Implementación paso a paso del algoritmo Bubble Sort
    if i < len(lista):
        if j < len(lista) - 1 - i:
            if lista[j] > lista[j + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1
        else:
            j = 0
            i += 1
    else:
        py5.no_loop()  # Detener la animación cuando esté ordenado

py5.run_sketch()

#Cada iteración muestra qué barras se están comparando (en amarillo).
#Las barras que ya han sido ordenadas se vuelven verdes para indicar que ya están en su posición final.
#La línea verde avanza de derecha a izquierda mostrando el progreso del ordenamiento.