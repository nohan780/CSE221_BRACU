input = open("input1b.txt", "r")
output = open("output1b.txt", "a")
l1 = list(map(int,input.readline().split()))
dic = {}
for i in range(l1[0]+1):
  dic[i] = []
for i in range(l1[1]):
  arr1 = list(map(int,input.readline().split()))
  dic[arr1[0]].append((arr1[1],arr1[2]))
for i,j in dic.items():
  if len(j) == 0:
    output.write(str(i) + ":" + " ")
  else:
    output.write(str(i) + ":" + " ")
    for k in j:
      output.write("(" + str(k[0]) + "," + str(k[1]) + ") ")
  output.write("\n")
input.close()
