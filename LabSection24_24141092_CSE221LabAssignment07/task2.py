from heapq import heapify, heappush, heappop

p = {}

def FindSet(j):
  if(p[j] == j):
    return j
  else:
    res = FindSet(p[j])
    p[j] = res
    return res

input_file = open("input2.txt", "r")
output_file = open("output2.txt", "w")

line = input_file.readline()
line = line.split()
n = int(line[0])
m = int(line[1])

edges = []
rank = [1]*(n+1)

for i in range(n+1):
  p[i] = i

for i in range(m):
  line = input_file.readline()
  line = line.split()
  u = int(line[0])
  v = int(line[1])
  w = int(line[2])
  if(u > v):
    u,v = v,u
  edges.append((w,u,v))

edges.sort()
minCost = 0

for i in range(m):
  u = edges[i][1]
  v = edges[i][2]
  x = FindSet(u)
  y = FindSet(v)
  if(x != y):
    if(rank[x] > rank[y]):
      rank[x] += rank[y]
      p[y] = x
    else:
      rank[y] += rank[x]
      p[x] = y
    minCost += edges[i][0]

output_file.write(f"{minCost}\n")

input_file.close()
output_file.close()