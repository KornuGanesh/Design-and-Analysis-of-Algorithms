import time
n = int(input("Enter the number of elements: " ))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter the element to search: "))
start = time.time()  
found = False
for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break
if found == False:
    print("Element not found")
end = time.time()        
print(f"Execution Time: {end-start:.5f} seconds")