p = {}

def FindSet(j):
  if(p[j] == j):
    return j
  else:
    res = FindSet(p[j])
    p[j] = res
    return res

input_file = open("input1.txt", "r")
output_file = open("output1.txt", "w")

line = input_file.readline()
line = line.split()
n = int(line[0])
m = int(line[1])

rank = [1]*(n+2)

for i in range(n+2):
  p[i] = i

for i in range(m):
  line = input_file.readline()
  line = line.split()
  x = FindSet(int(line[0]))
  y = FindSet(int(line[1]))
  if(x != y):
    if(rank[x] > rank[y]):
      rank[x] += rank[y]
      p[y] = x
      output_file.write(f"{rank[x]}\n")
    else:
      rank[y] += rank[x]
      p[x] = y
      output_file.write(f"{rank[y]}\n")
  else:
    output_file.write(f"{rank[x]}\n")

input_file.close()
output_file.close()