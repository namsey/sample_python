array1 = [1,2,3]
array2 = [4,5,6]
result = [0] * (len(array1) + len(array2))

i = 0
for element in array1:
    result[i] = element
    i+=1
for element in array2:
    result[i] = element
    i+=1

print("Merged array: ")
for element in result:
    print(str(element) + " ", end = "")
