
import sys
flag=False
n,k= map(int, input().split())
INF = sys.maxsize
dp= [INF] * 1000002
dp[0]=0

for i in range(n+1):
  if i+1 <=n:
    dp[i+1] = min(dp[i]+1, dp[i+1])
  
  if i+int(i/2) <=n:
    dp[i+int(i/2)] = min(dp[i+int(i/2)], dp[i]+1)

  
if dp[n]<=k:
  print("minigimbob")
else:
  print("water")