lista = [1,4,7,2,5,9,3]

def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]  # Intercambia
    return lista

print("La lista ordenada con el algoritmo SelectionSort es:", ordenamiento_seleccion(lista))