input = open("input1.txt", "r")
output = open("output1.txt", "a")
l1 = list(map(int,input.readline().split()))
node=l1[0]
edge=l1[1]
graph1={}
for i in range(1, node+1):
  if i not in graph1:
    graph1[i]={}

for i in range(edge):
  array1=list(map(int,input.readline().split()))
  if array1[0] in graph1:
    graph1[array1[0]].update({array1[1]: array1[2]})
source=input.readline().strip()

def dijkstra(graph, start, destination):
  d={}


  for i in graph:
    d[i]= float('inf')
  d[start]=0

  while graph:

    d_node=None

    for j in graph:
      if d_node is None:
        d_node= j
      elif d[j]< d[d_node]:
        d_node= j

    adj_routes =graph[d_node].items()

    for child, cost in adj_routes:

      if cost+ d[d_node] < d[child]:
          d[child]= cost+ d[d_node]

    graph.pop(d_node)
  return d
m = dijkstra(graph1, int(source), i)

for i,j in m.items():
  if j == float('inf'):
    output.write(str(-1) + " ")
  else:
    output.write(str(j) + " ")



