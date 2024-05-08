import sys

INF = sys.maxsize

n = int(input())
data = list(map(int, input().split()))
dp = [INF] *n
dp[0]=0

for i in range(n):
  jump = data[i]
  for j in range(1,1+jump):
    if i+j >=n:
      break
    dp[i+j] = min(dp[i+j], dp[i]+1)

  #print(dp)
  #print()

if dp[n-1]==INF:
  print(-1)
else:
  print(dp[n-1])