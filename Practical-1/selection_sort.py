import time
arr = list(map(int, input("Enter the array of elements: ").split()))
start = time .perf_counter()
for i in range(len(arr)):
  min_index = i
  for j in range(i + 1, len(arr)):
    if arr[j] < arr[min_index]:
     min_index = j
  arr[i], arr[min_index] = arr[min_index], arr[i]
print("Sorted array:", arr)
end = time.perf_counter()
print(f"Execution Time: {end - start:.5f} seconds")