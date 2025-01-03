import random
import time

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


element_sizes = [10**2, 10**3, 10**4]
print("Calculating processing time in Selection Sort:")
for size in element_sizes:
    arr = []
    inputs = random.randint(1, 1000)
    for i in range(size):
        arr.append(inputs)
    
    start_time = time.time()
    selection_sort(arr)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"For {size} elements: {execution_time:.7f} seconds")
