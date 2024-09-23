# 🍁 - Algoritmos Búsqueda

### 🪨 - BubbleSort
Funciona comparando elementos adyacentes y realizando intercambios si están en el orden incorrecto. Este enfoque provoca un número elevado de comparaciones, especialmente en listas grandes, lo que resulta en una complejidad de O(n²). Este algoritmo es más eficiente en listas pequeñas o en aquellas que ya están casi ordenadas, donde el número de intercambios se reduce.

### 🪨 - SelectionSort
Busca el elemento más pequeño en cada iteración y lo coloca en su posición correcta. Aunque realiza menos intercambios que Bubble Sort, también presenta una complejidad de O(n²), lo que lo hace ineficiente para listas grandes. Sin embargo, es más adecuado cuando el espacio de memoria es limitado, ya que no requiere almacenamiento adicional para sus operaciones.

### 🪨 - InsertionSort
Este algoritmo construye la lista ordenada tomando un elemento a la vez y colocándolo en la posición correcta dentro de la porción ordenada. A medida que avanza, compara el elemento actual con los anteriores, desplazando los más grandes a la derecha para insertar el nuevo elemento. Es más eficiente que otros algoritmos cuadráticos en listas pequeñas o parcialmente ordenadas. Su simplicidad y eficiencia en estos escenarios lo hacen útil en aplicaciones donde el costo de la reordenación es bajo.

### 🪨 - QuickSort
QuickSort es un algoritmo que organiza una lista dividiéndola en dos partes usando un pivote. Los elementos más pequeños que el pivote van a la izquierda, y los más grandes, a la derecha. Luego, se repite el proceso en cada parte hasta que toda la lista está ordenada. Es rápido y eficiente para listas grandes.

### 🪨 - MergeSort
MergeSort organiza una lista dividiéndola en partes más pequeñas hasta que cada una tiene un solo elemento. Luego, va combinando estas partes pequeñas, fusionándolas en el orden correcto hasta que toda la lista esté ordenada. Es muy útil para ordenar grandes cantidades de datos de manera eficiente.








