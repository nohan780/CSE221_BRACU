input = open("input1.txt", "r")
output = open("output1a.txt", "w")

line1 = input.readline().split()

n = int(line1[0])
target = int(line1[1])
numbers = input.readline().split()

for i in range(n):
  for j in range(i+1, n):
    sum = int(numbers[i]) + int(numbers[j])
    if sum == target:
      output.write(str(i+1) + " " + str(j+1))
      output.close()
      exit()
output.write("IMPOSSIBLE")
output.close()