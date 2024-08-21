
#방향/총 에너지 양
import sys

a,b,c,k = map(int, input().split())

dp=[[sys.maxsize]*(k+1) for _ in range(4)]

dp[0][0]=0

for i in range(k+1):
   for j in range(4):
    if i>=a:
      dp[j][i] = min(dp[j][i], dp[j-1][i-a]+1)
    
    if i>=b:
      dp[j][i] = min(dp[j][i], dp[j-3][i-b]+1)
    
    if i>=c:
      dp[j][i] = min(dp[j][i], dp[j-2][i-c]+1)


result = dp[0][k]

if(result ==sys.maxsize):
  print(-1)
else:
  print(result)



