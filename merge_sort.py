import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

element_sizes = [10**2, 10**3, 10**4]
print("Calculating processing time in Merge Sort:")

for size in element_sizes:
    arr = []
    inputs = random.randint(1, 1000)
    for i in range(size):
        arr.append(inputs)
    
    start_time = time.time()
    merge_sort(arr)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"For {size} elements: {execution_time:.7f} seconds")
