input = open("input1.txt", "r")
output = open("output1b.txt", "w")

line1 = input.readline().split()

n = int(line1[0])
target = int(line1[1])
numbers = input.readline().split()

left = 0
right = len(numbers) - 1
while left < right:
  sum = int(numbers[left]) + int(numbers[right])
  if sum == target:
    output.write(str(left+1) + " " + str(right+1))
    output.close()
    exit()
  elif sum < target:
    left += 1
  else:
    right -= 1
output.write("IMPOSSIBLE")
output.close()