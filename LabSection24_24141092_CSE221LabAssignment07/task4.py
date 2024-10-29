from heapq import heapify, heappush, heappop

input_file = open("input4.txt", "r")
output_file = open("output4.txt", "w")

line = input_file.readline()
line = line.split()
n = int(line[0])
x = int(line[1])
inf = 1000000000
line = input_file.readline()
line = line.split()
coins = [0]*n

for i in range(n):
  coins[i] = int(line[i])

coins.sort()
coin = coins[n-1:0:-1]
coin.append(coins[0])

dp = [inf]*(x+1)
dp[0] = 0

for i in range(n):
  for j in range(coin[i],x+1):
    dp[j] = min(dp[j], dp[j-coin[i]] + 1)

if(dp[x] == inf):
  output_file.write(str(-1))
else:
  output_file.write(str(dp[x]))

input_file.close()
output_file.close()