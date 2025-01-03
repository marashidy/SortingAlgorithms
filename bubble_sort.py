import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

element_sizes = [10**2, 10**3, 10**4]
print("Calculating processing time in Bubble Sort:")

for size in element_sizes:
    arr = []
    inputs = random.randint(1, 1000)
    for i in range(size):
        arr.append(inputs)
    
    start_time = time.time()
    bubble_sort(arr)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"For {size} elements: {execution_time:.7f} seconds")
