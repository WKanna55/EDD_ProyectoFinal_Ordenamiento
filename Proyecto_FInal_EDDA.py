import time
import random
import matplotlib.pyplot as plt
"""Implementacion 01: Bubble Sort(inicio)"""
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        #variable para saber si se hizo algún intercambio
        intercambio = False
        for j in range(0, n-i-1):
            # ver si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j+1] :
                # Intercambiamos los elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]
                # Marcamos que se hizo un intercambio
                intercambio = True
        # Si no se hizo ningún intercambio en la iteración, la lista está ordenada termina
        if not intercambio:
            break
    return lista
"""Implementacion 01: Bubble Sort(fin)"""

"""Implementacion 02: Selection Sort(inicio)"""
def selection_sort(array):
    for i in range(len(array) - 1):
        min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j

        temp = array[i]
        array[i] = array[min]
        array[min] = temp
"""Implementacion 02: Selection Sort(fin)"""

"""Implementacion 03: Insertion Sort(inicio)"""
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
"""Implementacion 03: Insertion Sort(fin)"""

"""Implementacion 04: Merge Sort(inicio)"""
def Merge(left_arr, right_arr):
    arr_result = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_result.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_result.append(left_arr[0])
            left_arr.pop(0)

    while len(left_arr) > 0:
        arr_result.append(left_arr[0])
        left_arr.pop(0)

    while len(right_arr) > 0:
        arr_result.append(right_arr[0])
        right_arr.pop(0)

    return arr_result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    sorted_leftarray = merge_sort(left_arr)
    sorted_rightarray = merge_sort(right_arr)

    return Merge(sorted_leftarray, sorted_rightarray)
"""Implementacion 04: Merge Sort(fin)"""

"""Implementacion 05: Quick Sort(inicio)"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)
"""Implementacion 05: Quick Sort(fin)"""

"""Implementacion 06: Counting Sort(inicio)"""
def counting_sort(arr):
    max_value = max(arr)

    output = [0] * len(arr)
    count = [0] * (max_value + 1)

    for i in arr:
        count[i] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output
"""Implementacion 06: Counting Sort(fin)"""

"""Implementacion 07: Bucket Sort(inicio)"""
def bucket_sort(array):
    num_buckets = (len(array)//2)
    max_val = max(array)  # o(n)
    min_val = min(array)  # o(n)

    bucketRango = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in array: # insertar los numeros de entrada en los buckets || O(n)
        indiceHash = int((num / bucketRango).__floor__())
        if indiceHash >= len(buckets):
            indiceHash = len(buckets) - 1
        buckets[indiceHash].append(num)

    for i in range(num_buckets):
        buckets[i].sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array = sorted_array + bucket

    return sorted_array
def bucket_sort_peor(array):
    num_buckets = (len(array) // 2)
    max_val = max(array)  # o(n)
    min_val = min(array)  # o(n)

    bucketRango = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in array:  # insertar los numeros de entrada en los buckets || O(n)
        buckets[0].append(num)

    for i in range(num_buckets):
        buckets[i].sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array = sorted_array + bucket

    return sorted_array
"""Implementacion 07: Bucket Sort(fin)"""

"""Inicio de BenchMarking"""
""" grafica lineal, acepta varios arrays de entrada """

array_sizes = [10, 100, 1000, 2000, 3000, 5000, 7000, 10000]

""" Peor caso grafica lineal """
def medir_tiempo(algoritmo_ordenamiento, array):
    start_time = time.time()
    algoritmo_ordenamiento(array.copy())  # Usar una copia para no afectar el arreglo original
    end_time = time.time()
    return end_time - start_time

algoritmos_ordenamiento = [
    bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, counting_sort, bucket_sort
]

""" Worst Cases """
##   worst_case_times = [[] for _ in algoritmos_ordenamiento]
##
##           #worstcases
##   for size in array_sizes:
##       #arr_best = list(range(size))
##       arr_worst = list(range(size, 0, -1))
##       i = 0
##       for algoritmo in algoritmos_ordenamiento:
##           tiempo = medir_tiempo(algoritmo, arr_worst)
##           worst_case_times[i].append(tiempo)
##           i += 1
##
##   for i in range(len(worst_case_times)):
##       plt.plot(array_sizes, worst_case_times[i], label=f'{algoritmos_ordenamiento[i].__name__}')
##
##   plt.xlabel('Tamaño del array')
##   plt.ylabel('Tiempo (segundos)')
##   plt.title('Algoritmos peor caso')
##   plt.legend()
##   plt.show()
##

""" Mejor caso grafica lineal """
best_case_times = [[] for _ in algoritmos_ordenamiento]
     #BestCases
for size in array_sizes:
    arr_best = list(range(size))
    #arr_worst = list(range(size, 0, -1))
    i = 0
    for algoritmo in algoritmos_ordenamiento:
        tiempo = medir_tiempo(algoritmo, arr_best)
        best_case_times[i].append(tiempo)
        i += 1

for i in range(len(best_case_times)):
    plt.plot(array_sizes, best_case_times[i], label=f'{algoritmos_ordenamiento[i].__name__}')

plt.xlabel('Tamaño del array')
plt.ylabel('Tiempo (segundos)')
plt.title('Algoritmos mejor caso')
plt.legend()
plt.show()

"""Compara cada algoritmo segun 1 array y grafico de barras"""

#  # Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
#  def medir_tiempo(algoritmo_ordenamiento, array):
#      start_time = time.time()
#      algoritmo_ordenamiento(array.copy())  # Usar una copia para no afectar el arreglo original
#      end_time = time.time()
#      return end_time - start_time
#
#  # Parámetro: tamaño del arreglo
#  array_size = 10000
#
#  # Generar dos arreglos de números ascendente y descendentes
#  arr_best = list(range(array_size))
#  arr_worst = list(range(array_size, 0, -1))
#
#  # Lista para almacenar los tiempos de ejecución de cada algoritmo
#  tiempos = []
#
#  # Algoritmos de ordenamiento a probar
#  algoritmos_ordenamiento = [
#      bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, counting_sort, bucket_sort
#  ]
#
#  # Medir el tiempo de ejecución para cada algoritmo
#  for algoritmo in algoritmos_ordenamiento:
#      tiempo = medir_tiempo(algoritmo, arr_worst)
#      tiempos.append(tiempo)
#      print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")
#
#  # Visualizar gráficamente los tiempos de ejecución
#  nombres_algoritmos = [algoritmo.__name__ for algoritmo in algoritmos_ordenamiento]
#  plt.bar(nombres_algoritmos, tiempos)
#  plt.title('Tiempo de ejecución de diferentes algoritmos de ordenamiento')
#  plt.xlabel('Algoritmo')
#  plt.ylabel('Tiempo (segundos)')
#  plt.show()