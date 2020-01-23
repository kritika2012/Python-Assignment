#first way
matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix.append(j)
print(matrix)
print('\n\n\n')

#List Comprehension
mat=[[j for j in range(5)] for i in range(5)]
print(matrix)
print()

#flater to a given 2D list
list1=[]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
      for j in range(3):
          list1.append(matrix[i][j])
print(list1)
print()

#Through List comprehension
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatter=[]
flatter=[val for sublist in matrix for val in sublist]
print(flatter)
print()

#using the if condition with List Comprehension
flatter=[val for sublist in matrix for val in sublist if val>3]
print(flatter)
