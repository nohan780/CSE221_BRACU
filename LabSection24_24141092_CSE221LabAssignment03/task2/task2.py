def divide(arr):
  if len(arr) <= 1:
      return arr
  else:
      mid = len(arr) // 2
      a1 = divide(arr[:mid])   
      a2 = divide(arr[mid:])  
      maxi = max(a1,a2)
      return maxi         


input = open("input2.txt", "r")
output = open("output2.txt", "w")

n1 = input.readline().split()
arr1 = list(map(int,input.readline().split()))
a = divide(arr1)

output.write(str(a[0]))