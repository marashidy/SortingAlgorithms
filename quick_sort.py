import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

element_sizes = [10**2, 10**3, 10**4]
print("Calculating processing time in Quick Sort:")

for size in element_sizes:
    arr = []
    inputs = random.randint(1, 1000)
    for i in range(size):
        arr.append(inputs)
    
    start_time = time.time()
    quick_sort(arr)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"For {size} elements: {execution_time:.7f} seconds")
