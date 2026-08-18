import time
n = int(input("Enter the number of elements:" ))
arr = []
print("Enter the elements in sorted order:")

for i in range(n):
    arr.append(int(input()))
key = int(input("Enter the element to search: "))
start = time.time()     
low = 0
high = n - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if found == False:
    print("Element not found")
end = time.time()      
print(f"Execution Time: {end-start:.5f} seconds")