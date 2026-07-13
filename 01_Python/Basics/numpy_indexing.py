import numpy as np
#Indexing starts from 0 like (0,1,2,3,4)
arr = np.array([10, 20, 30, 40, 50])

# print(arr[0])    # 10
# print(arr[-1])   # 50 (negative indexing)
# print(arr[2])    # 30

# #------------Slicing----------------
# arr = np.array([10,20,30,40,50,60])

# print(arr[1:4])
# print(arr[:3])
# print(arr[3:])
# print(arr[::2])



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # For odd numbers
# odd_numbers = numbers[::2]
# print(odd_numbers) 

# #For Even numbers
# even_numbers = numbers[1::2]
# print(even_numbers) 

#--------2D arrays-------
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matrix[0])
print(matrix[1,2])
print(matrix[:,1])
print(matrix[1,:])

# extracting column from 2D list
column = [row[0] for row in matrix]
print(column)
print(type(column[0])) 
# converting this o/p in normal integer
column = [row[0] for row in matrix]

result = [int(x) for x in column]

print(result)
print(type(result[0]))