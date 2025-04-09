import matplotlib.pyplot as plt
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [random.randint(0, 1000) for _ in range(1000)]

times_insertion = []
times_bubble = []
times_selection = []
sizes = []

for size in range(10, 1001, 10):
    sublist = arr[:size]
    start_time = time.time()
    insertion_sort(sublist)
    end_time = time.time()
    times_insertion.append(end_time - start_time)

    start_time = time.time()
    bubble_sort(sublist)
    end_time = time.time()
    times_bubble.append(end_time - start_time)

    start_time = time.time()
    selection_sort(sublist)
    end_time = time.time()
    times_selection.append(end_time - start_time)

    sizes.append(size)

plt.plot(sizes, times_insertion, label='Insertion Sort')
plt.plot(sizes, times_bubble, label='Bubble Sort')
plt.plot(sizes, times_selection, label='Selection Sort')
plt.xlabel('Ilość elementów w tablicy')
plt.ylabel('Czas sortowania (s)')
plt.title('Czas sortowania różnymi algorytmami')
plt.legend()
plt.show()
