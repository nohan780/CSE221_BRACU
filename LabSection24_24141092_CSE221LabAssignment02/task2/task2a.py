input = open("input2.txt", "r")
output = open("output2a.txt", "a")

n1 = input.readline().split()
arr1 = input.readline().split()
n2 = input.readline().split()
arr2 = input.readline().split()

new = []
for i in arr1:
  new.append(int(i))
for i in arr2:
  new.append(int(i))

new.sort()

for i in new:
  output.write(str(i) + " ")


