input = open("input6.txt", "r")
output = open("output6.txt", "w")

l1 = list(map(int,input.readline().split()))
row = l1[0]
col = l1[1]
g = []
for i in range(row):
  g.append([])
c = 0
while c < row:
  l1 = input.readline().split()
  for i in l1:
    for j in range(len(i)):
      g[c].append(i[j])
  c += 1


def valid(x,y,R,H):
  return 0 <= x < R and 0 <= y < H

def floodFill(grid,x,y,visited):
  if not valid(x,y,len(grid),len(grid[0])) or grid[x][y] == "#" or visited[x][y] == True:
    return 0

  visited[x][y] = True
  diamonds = 0

  if grid[x][y] == "D":
    diamonds = 1

  for a, b in [(1,0),(-1,0),(0,1),(0,-1)]:
    diamonds += floodFill(grid,x+a,y+b,visited)
  return diamonds


def findMax(grid):
  R, H = len(grid), len(grid[0])
  maxDiamonds = 0

  for x in range(R):
    for y in range(H):
      if grid[x][y] == ".":
        visited = [[False for i in range(H)] for j in range(R)]

        diamonds = floodFill(grid,x,y,visited)
        maxDiamonds = max(maxDiamonds,diamonds)

  return maxDiamonds

out = findMax(g)
output.write(str(out))
output.close()