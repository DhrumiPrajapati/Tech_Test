arr = []
number = int(input("Enter the number of elements in the array : "))
print("Enter the elements: ")
for i in range(0, number):
    element = int(input())
    arr.append(element)

print(arr)

print("Maximum is: " + str(max(arr)))
print("Minimum is: " + str(min(arr)))