input = open("input2.txt", "r")
output = open("output2b.txt", "a")

n1 = input.readline().split()
arr1 = input.readline().split()
n2 = input.readline().split()
arr2 = input.readline().split()

new = []

first = 0
second = 0
while first < len(arr1) or second < len(arr2):
  if first < len(arr1) and second == len(arr2):
    new.append(int(arr1[first]))
    first += 1
  elif first == len(arr1) and second < len(arr2):
    new.append(int(arr2[second]))
    second += 1

  elif int(arr1[first]) < int(arr2[second]):
    new.append(int(arr1[first]))
    first += 1
  else:
    new.append(int(arr2[second]))
    second += 1

for i in new:
  output.write(str(i) + " ")