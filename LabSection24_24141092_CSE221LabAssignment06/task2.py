input = open("input2.txt", "r")
output = open("output2.txt", "a")
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

alice, bob = list(map(int, input.readline().split()))

def dijkstra(graph, start):
  minimum_distance={}
  unvisited = graph.copy()

  for i in unvisited:
    minimum_distance[i]= float('inf')
  minimum_distance[start]=0

  while unvisited:

    min_distance_node=None

    for j in unvisited:
      if min_distance_node is None:
        min_distance_node= j
      elif minimum_distance[j]< minimum_distance[min_distance_node]:
        min_distance_node= j

    adj_routes =graph[min_distance_node].items()

    for child, cost in adj_routes:

      if cost + minimum_distance[min_distance_node] < minimum_distance[child]:
          minimum_distance[child]= cost+ minimum_distance[min_distance_node]

    unvisited.pop(min_distance_node)
  return minimum_distance

x=dijkstra(graph1, alice)
y=dijkstra(graph1, bob)
meeting= -1
shortest_distance=float('inf')
distance= None
alice=[]
bob=[]

for u,v in x.items():
  alice.append(v)
for u, v in y.items():
  bob.append(v)

for i in range(1, node):
  if alice[i] != float('inf') and bob[i] != float('inf'):
    distance =max(alice[i], bob[i])
    if distance< shortest_distance:
      shortest_distance= distance
      meeting= i+1

if distance == None:
  output.write("IMPOSSIBLE")
else:
  output.write("Time: " + str(shortest_distance) + "\n")
  output.write("Node: " + str(meeting))