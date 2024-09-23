lista = [1,4,7,2,5,9,3]

def ordenamiento_burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  
    
    return lista

#print("La lista ordenada con el algoritmo BubbleSort es:", ordenamiento_burbuja(lista))
print("La lista ordenada con el algoritmo BubbleSort es:", ordenamiento_burbuja(lista))