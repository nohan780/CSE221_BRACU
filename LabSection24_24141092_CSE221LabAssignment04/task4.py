input = open("input4.txt", "r")
output = open("output4.txt", "w")

l1 = list(map(int,input.readline().split()))
a = l1[0]
b = l1[1]
dic = {}





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



for i in range(b):
  arr = list(map(int,input.readline().split()))
  if arr[0] not in dic:
    dic[arr[0]] = [arr[1]]
  else:
    dic[arr[0]].append(arr[1])
visited=[None]*(a+1)
path=[None]*(a+1)
chck = True
for i in range(1,a+1):
  if(not visited[i]):
      if has_cycle(dic, visited, path, i, None):
        output.write("YES")
        chck = False
        break
if chck:
  output.write("NO")


