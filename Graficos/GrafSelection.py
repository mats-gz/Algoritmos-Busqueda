import py5

# Lista de valores para ordenar
lista = [1, 4, 7, 2, 5, 9, 3]

# Variables de control para el algoritmo
i = 0
j = 1
minimo = 0
ancho_barra = 40  # Ancho de cada barra
espacio_barra = 5  # Espacio entre las barras

def setup():
    py5.size(500, 400)  # Tamaño amplio para mejor visualización
    py5.frame_rate(1)  # Controla la velocidad de la animación (1 frame por segundo)

def draw():
    global i, j, minimo, lista
    py5.background(220)  # Fondo claro para mayor contraste

    # Dibujar las barras de la lista
    for index, value in enumerate(lista):
        x = index * (ancho_barra + espacio_barra) + 50  # Posición en X
        altura = value * 10  # La altura de la barra es proporcional al valor
        py5.fill(100, 150, 255)  # Color estándar de las barras

        # Resaltar el mínimo actual (barra azul) y las comparaciones (barra amarilla)
        if index == minimo:
            py5.fill(100, 100, 255)  # Azul para el mínimo actual
        elif index == j:
            py5.fill(255, 255, 100)  # Amarillo para la comparación actual

        # Zona ordenada (verde)
        if index < i:
            py5.fill(100, 255, 100)  # Verde para la parte ya ordenada

        # Dibujar cada barra
        py5.rect(x, py5.height - altura, ancho_barra, altura)

    # Mostrar la zona ordenada con una línea verde
    py5.stroke(0, 200, 0)
    py5.line(i * (ancho_barra + espacio_barra) + 50, 0, i * (ancho_barra + espacio_barra) + 50, py5.height)

    # Implementación paso a paso del algoritmo Selection Sort
    if i < len(lista) - 1:
        if j < len(lista):
            if lista[j] < lista[minimo]:
                minimo = j  # Actualizar el índice del mínimo
            j += 1
        else:
            # Intercambiar el mínimo encontrado con el elemento en la posición i
            lista[i], lista[minimo] = lista[minimo], lista[i]
            i += 1  # Avanzar al siguiente índice
            j = i + 1  # Reiniciar la búsqueda desde el siguiente elemento
            minimo = i  # Suponer que el nuevo mínimo es el siguiente
    else:
        py5.no_loop()  # Detener la animación cuando esté ordenado

py5.run_sketch()

#El algoritmo recorre toda la lista, buscando el valor más pequeño en cada pasada, y lo coloca en la posición correspondiente.
#Las barras amarillas muestran las comparaciones, y la barra azul resalta el mínimo encontrado durante cada iteración.
#Las barras verdes representan los elementos que ya están en su posición final.
