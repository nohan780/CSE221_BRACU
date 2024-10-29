

def merge(a, b):
  c = []
  i = 0
  j = 0
  while i < len(a) and j < len(b):
      if a[i] < b[j]:
          c.append(a[i])
          i += 1
      else:
          c.append(b[j])
          j += 1
  while i < len(a):
      c.append(a[i])
      i += 1
  while j < len(b):
      c.append(b[j])
      j += 1
  return c

def mergeSort(arr):
  if len(arr) <= 1:
      return arr
  else:
      mid = len(arr) // 2
      a1 = mergeSort(arr[:mid])
      a2 = mergeSort(arr[mid:])  
      return merge(a1, a2)          

input = open("input1.txt", "r")
output = open("output1.txt", "a")

n1 = input.readline().split()
arr1 = list(map(int,input.readline().split()))

a = mergeSort(arr1)
for i in a:
  output.write(str(i) + " ")

