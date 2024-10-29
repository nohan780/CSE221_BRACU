from heapq import heapify, heappush, heappop

input_file = open("input3.txt", "r")
output_file = open("output3.txt", "w")

line = input_file.readline()
n = int(line)

f1 = 1
f2 = 2
res = 0
for i in range(n-2):
  res = f1 + f2
  f1 = f2
  f2 = res

output_file.write(f"{res}\n")


input_file.close()
output_file.close()