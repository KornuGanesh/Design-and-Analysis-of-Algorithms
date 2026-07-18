import time
arr = list(map(int, input("Enter the array of elements: ").split()))
start = time.perf_counter()
for i in range(len(arr)-1):
    for j in range (len(arr)-1-i):
        if arr[j]>arr [j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            print("swapping",arr[j], "and", arr[j+1])
            print("sorted array:",arr)
            end = time.perf_counter()
print(f"Execution Time: {end - start:.5f} seconds")