input = open("input1.txt", "r")
output = open("output1a.txt", "a")
l1 = list(map(int,input.readline().split()))
a = l1[0]
b = l1[1]
dic = {}
for i in range(l1[0]+1):
  dic[i] = []
for i in range(l1[1]):
  arr1 = list(map(int,input.readline().split()))
  dic[arr1[0]].append(arr1[1])


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
def has_cycle(graph, visited, path, current_vertex, parent):
  visited[current_vertex] = True
  path[current_vertex] = True

  if current_vertex in graph:
      for neighbor in graph[current_vertex]:
          if not visited[neighbor]:
              if has_cycle(graph, visited, path, neighbor, current_vertex):
                  return True
          elif path[neighbor] and neighbor != parent:
              return True

  path[current_vertex] = False
  return False

visited=[None]*(a+1)
path=[None]*(a+1)
chck = True
for i in range(1,a+1):
  if(not visited[i]):
      if has_cycle(dic, visited, path, i, None):
        output.write("IMPOSSIBLE")
        chck = False
        break



if chck:

  for i in range(1,a+1):
    if visit[i] == 0:
      now = dfs2(n,visit,dic,i)
  now.reverse()
  for i in range(len(now)):
    output.write(str(now[i]) + " ")