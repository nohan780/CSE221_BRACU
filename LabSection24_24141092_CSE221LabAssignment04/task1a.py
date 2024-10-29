import numpy as np
input = open("input1a.txt", "r")
output = open("output1a.txt", "a")

l1 = list(map(int,input.readline().split()))
arr = np.zeros((l1[0]+1,l1[0]+1), dtype=int)
for i in range(l1[1]):
  arr1 = list(map(int,input.readline().split()))
  arr[arr1[0],arr1[1]] = arr1[2]
for i in range(l1[0]+1):
  for j in range(l1[0]+1):
    output.write(str(arr[i][j]) + " ")
  output.write("\n")
input.close()