input = open("input2.txt", "r")
output = open("output2.txt", "a")

l1 = list(map(int,input.readline().split()))
a = l1[0]
b = l1[1]
l2 = [] * (a+1)
l3 = [0] * (a+1)
s = 1
for i in range(a + 1):
  l2.append([0]*(a+1))
for i in range(b):
  arr = list(map(int,input.readline().split()))
  l2[arr[0]][arr[1]] = 1
def bfs(g1,g2,s):
  q = []
  out = []
  q.append(s)
  g2[s] = 1
  while q:
    u = q.pop(0)
    out.append(u)
    for i in range(len(g1[u])):
      if g1[u][i] != 0 and g2[i] == 0:
        q.append(i)
        g2[i] = 1
  return out
now = bfs(l2,l3,s)
for i in now:
  output.write(str(i) + " ")