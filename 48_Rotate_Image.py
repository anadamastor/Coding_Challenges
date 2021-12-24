# LEETCODE 48

# Rotate a matrix by 90 degres
import numpy as np

matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# Each element of the last child array becomes 
# the first item of each of the new child arrays
# Starting from last column

# First approach - not constant space
def rotate_matrix(arr):
  print("Using a second matrix: \n", np.matrix(matr))
  # Size of array is known - initialise it
  # Not constant space
  newArr = []
  for i in range(len(arr)):
    newArr.append([])

  pointer = -1

  print(arr)
  for n in range(len(arr)):
    counter = 0
    for x in arr[pointer]:
      newArr[counter].append(x)
      counter += 1
    pointer -= 1
  print("Rotated matrix: \n", np.matrix(newArr))
  return newArr

print(rotate_matrix(matr))

# In-place approach