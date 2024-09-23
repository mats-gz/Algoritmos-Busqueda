def ordenamiento_fusion(lista):
    if len(lista) <= 1:
        return lista

    # Dividimos la lista en dos mitades
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Ordenamos cada mitad recursivamente
    izquierda = ordenamiento_fusion(izquierda)
    derecha = ordenamiento_fusion(derecha)

    # Fusionamos las mitades ordenadas
    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    # Comparar elementos y fusionarlos en orden
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar cualquier elemento restante de las mitades
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Ejemplo de uso
lista = [4, 7, 2, 8, 1, 3, 5]
print("La lista ordenada con el algoritmo MergeSort es:", ordenamiento_fusion(lista))
