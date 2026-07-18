import time
arr = list(map(int, input("Enter the array of elements: ").split()))
start = time.perf_counter()
for i in range (1, len(arr)):
   key=arr[i]
   j=i-1
   while j>=0 and arr[j]>key:
    arr[j+1]=arr[j]
    j=j-1
    arr[j+1]=key 
print ("sorted array:", arr)
end = time.perf_counter()
print(f"Execution Time: {end - start:.5f} seconds")