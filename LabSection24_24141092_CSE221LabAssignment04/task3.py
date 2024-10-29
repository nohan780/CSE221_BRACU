input = open("input3.txt", "r")
output = open("output3.txt", "a")

l1 = list(map(int,input.readline().split()))
a = l1[0]
b = l1[1]
dic = {}
for i in range(a + 1):
  dic[i] = []
for i in range(b):
  arr = list(map(int,input.readline().split()))
  dic[arr[0]].append(arr[1])
  dic[arr[1]].append(arr[0])
out = []
visit = [0] * (a + 1)

def dfs(visit,dic,v):
  if visit[v] == 0:
    visit[v] = 1
    out.append(v)
    for i in dic[v]:
      dfs(visit,dic,i)
  return out
now = dfs(visit,dic,1)

for i in now:
  output.write(str(i) + " ")
