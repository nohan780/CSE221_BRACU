input = open("input4.txt", "r")
output = open("output4.txt", "w")
n1 = list(map(int,input.readline().split()))
arr = [0] * n1[1]
l = []
for i in range(int(n1[0])):
  l.append(tuple(map(int,input.readline().split())))
for i in range(len(l)):
  for j in range(i, len(l)):
    if l[i][1] > l[j][1]:
      l[i],l[j] = l[j],l[i]


arr[0] = l[0]

count = 1
for i in range(1,len(l)):
  l2 = []
  chck = False
  for j in range(len(arr)):
    if arr[j] == 0:
      arr[j] = l[i]
      count += 1

      break
    else:
      diff = l[i][0] - arr[j][1]
      if diff >= 0:
        l2.append(diff)
        chck = True

  if chck == True:   
    mini = min(l2)
    indx = l2.index(mini)
    arr[indx] = l[i]
    count += 1
output.write(str(count))
output.close()