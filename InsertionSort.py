lista = [1,4,7,2,5,9,3]

def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i] 
        j = i - 1  

        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]  
            j -= 1  

        lista[j + 1] = clave

    return lista

print("La lista ordenada con el algoritmo InsertionSort es:", ordenamiento_insercion(lista))