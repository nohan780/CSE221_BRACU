def kth_elem(arr, p, r, tar):
  if p == r:
    return arr[p]

  q = partition(arr, p, r)
  if q == tar:
    return arr[q]
  elif q > tar:
    return kth_elem(arr, p, q - 1,tar)
  else:
    return kth_elem(arr, q + 1, r,tar)
def partition(arr, p, r):
  x = arr[r]
  i = p - 1
  for j in range(p, r):
    if arr[j] <= x:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[r] = arr[r], arr[i + 1]
  return i + 1


input = open("input6.txt", "r")
output = open("output6.txt", "a")

n1 = input.readline().split()
arr1 = list(map(int,input.readline().split()))
que = input.readline().split()
for i in range(int(que[0])):
  t = input.readline().split()
  a = kth_elem(arr1, 0, len(arr1)-1, int(t[0])-1)
  output.write(str(a) + "\n")

