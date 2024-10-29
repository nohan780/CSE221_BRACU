input = open("input5.txt", "r")
output = open("output5.txt", "w")

l1 = list(map(int,input.readline().split()))
a = l1[0]
b = l1[1]
c = l1[2]
l2 = [] * (a+1)
l3 = [-1] * (a+1)
s = 1
for i in range(a + 1):
  l2.append([0]*(a+1))
for i in range(b):
  arr = list(map(int,input.readline().split()))
  l2[arr[0]][arr[1]] = 1
  l2[arr[1]][arr[0]] = 1
def bfs(g1,g2,s):
  anc = [0] * (a+1)
  q = []
  out = []
  q.append(s)
  g2[s] = 0
  while q:
    u = q.pop(0)
    out.append(u)
    for i in range(len(g1[u])):
      if g1[u][i] != 0 and g2[i] == -1:
        g2[i] = g2[u] + 1
        q.append(i)
        anc[i] = u
  return g2, anc
now,anc = bfs(l2,l3,s)
time = now[c]
path=[]
path.append(c)
x=anc[c]
path.append(x)
while anc[x]!=0:
  x=anc[x]
  path.append(x)
path.reverse()
if time == 0:
  path = [path[1]]
output.write("Time: " + str(time) + "\n")
output.write("Shortest Path: ")
for i in path:
  output.write(str(i) + " ")