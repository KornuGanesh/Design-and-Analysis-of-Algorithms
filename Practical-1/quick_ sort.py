import time
arr = list(map(int, input("Enter elements: ").split()))
start = time.perf_counter()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = quick_sort(arr)
print("Sorted array:", arr)
end = time.perf_counter()

print(f"Execution Time: {end-start:.5f} seconds")