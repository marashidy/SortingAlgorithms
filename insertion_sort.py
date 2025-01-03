import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

element_sizes = [10**2, 10**3, 10**4]
print("Calculating processing time in Insertion Sort:")

for size in element_sizes:
    arr = []
    inputs = random.randint(1, 1000)
    for i in range(size):
        arr.append(inputs)
    
    start_time = time.time()
    insertion_sort(arr)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"For {size} elements: {execution_time:.7f} seconds")
