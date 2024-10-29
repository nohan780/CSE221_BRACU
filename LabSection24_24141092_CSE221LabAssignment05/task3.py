input = open("input3.txt", "r")
output = open("output3.txt", "a")
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



visit = [0] * (a + 1)
n = []
def dfs2(n,visit,dic,v):
  if visit[v] == 0:
    visit[v] = 1
    if len(dic[v]) == 0:
      n.append(v)
    else:
      for i in dic[v]:
        dfs2(n,visit,dic,i)
      n.append(v)
  return n
for i in range(1,a+1):
  if visit[i] == 0:
    now = dfs2(n,visit,dic,i)

def dfs(z,visit,dic,v):
  if visit[v] == 0:
    visit[v] = 1
    z.append(v)
    for i in dic[v]:
      dfs(z,visit,dic,i)
  return z
new = [0]*(a+1)
now.reverse()

visit2 = [0] * (a + 1)
for i in range(len(now)):
  z = []
  again = dfs(z,visit2,dic2,now[i])
  if len(again) != 0:
    m = again[0]
    new[m] = again
for i in new:
  if i != 0:
    i.sort()
for i in range(1,a+1):
  if new[i] == 0 or len(new[i]) == 0:
    continue
  else:
    output.write(str(new[i][0]))
    for j in range(1,len(new[i])):
      output.write(" " + str(new[i][j]))
    output.write("\n")