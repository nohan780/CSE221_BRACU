def merge(a, b):
  c = []
  i = 0
  j = 0
  count = 0
  while i < len(a) and j < len(b):
      if a[i] < b[j]:
          c.append(a[i])
          i += 1
      else:
          c.append(b[j])
          j += 1
          count += (len(a)-i)
  while i < len(a):
      c.append(a[i])
      i += 1
  while j < len(b):
      c.append(b[j])
      j += 1
  return list((c,count))

def mergeSort(arr):
  count = 0
  if len(arr) <= 1:
      return list((arr, count))
  else:
      mid = len(arr) // 2
      a1 = mergeSort(arr[:mid])
      count += a1[1]
      a2 = mergeSort(arr[mid:])  
      count += a2[1]
      a3 = merge(a1[0], a2[0])
      count += a3[1]
      return list((a3[0], count))


input = open("input3.txt", "r")
output = open("output3.txt", "w")

n1 = input.readline().split()
arr1 = list(map(int,input.readline().split()))

a = mergeSort(arr1)
output.write(str(a[1]))
