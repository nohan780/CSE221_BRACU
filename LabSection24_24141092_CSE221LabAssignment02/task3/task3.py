input = open("input3.txt", "r")
output = open("output3.txt", "a")
l = []
n1 = input.readline().split()
for i in range(int(n1[0])):
  l.append(tuple(map(int,input.readline().split())))
for i in range(len(l)):
  for j in range(i, len(l)):
    if l[i][1] > l[j][1]:
      l[i],l[j] = l[j],l[i]
count = 1
new = []
i = 0
j = 1


new.append(l[0])
while j < len(l):
  if l[i][1] <= l[j][0]:
    new.append(l[j])
    count += 1
    i = j
    j += 1

  else:
    j+=1
output.write(str(count)+"\n")
for i in new:
  output.write(str(i[0]) + " " + str(i[1]) + "\n")

