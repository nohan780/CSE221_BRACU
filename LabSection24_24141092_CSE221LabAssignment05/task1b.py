input = open("input1.txt", "r")
output = open("output1b.txt", "a")
l1 = list(map(int,input.readline().split()))
a = l1[0]
b = l1[1]
dic = {}
dic2 = {}
for i in range(l1[0]+1):
  dic[i] = []
  dic2[i] = []
for i in range(l1[1]):
  arr1 = list(map(int,input.readline().split()))
  dic[arr1[0]].append(arr1[1])
  dic2[arr1[1]].append(arr1[0])

a = [-1] * (a + 1)
for i, j in dic2.items():
  a[i] = len(j)

def bfs(g1, g2):
  q = []
  out = []

  for i in range(1,len(a)):
    if a[i] == 0:
      q.append(i)

  while q:
    u = q.pop(0)
    out.append(u)

    for i in range(len(g1[u])):
      g2[g1[u][i]] -= 1
      if g2[g1[u][i]] == 0:
        q.append(g1[u][i])
  return out

now = bfs(dic, a)

if len(a) - 1 != len(now):
  output.write("IMPOSSIBLE")
else:
  for i in range(len(now)):
    output.write(str(now[i]) + " ")

