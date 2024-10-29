def quicksort(arr, p, r):
  if p < r:
    q = partition(arr, p, r)
    quicksort(arr, p, q - 1)
    quicksort(arr, q + 1, r)
  return arr
def partition(arr, p, r):
  x = arr[r]
  i = p - 1
  for j in range(p, r):
    if arr[j] <= x:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[r] = arr[r], arr[i + 1]
  return i + 1


input = open("input5.txt", "r")
output = open("output5.txt", "a")

n1 = input.readline().split()
arr1 = list(map(int,input.readline().split()))
a = quicksort(arr1, 0, len(arr1) - 1)
for i in a:
  output.write(str(i) + " ")