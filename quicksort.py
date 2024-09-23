def ordenamiento_rapido(lista):
    # Caso base: Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    else:
        # Elegimos el pivote como el primer elemento de la lista
        pivote = lista[0]
        
        # Sublista de elementos menores o iguales al pivote
        menores = [x for x in lista[1:] if x <= pivote]
        
        # Sublista de elementos mayores que el pivote
        mayores = [x for x in lista[1:] if x > pivote]
        
        # Recursivamente ordenamos las sublistas y las combinamos
        return ordenamiento_rapido(menores) + [pivote] + ordenamiento_rapido(mayores)
    
lista = [1,4,7,2,5,9,3]
print("La lista ordenada con el algoritmo Quicksort es:", ordenamiento_rapido(lista))