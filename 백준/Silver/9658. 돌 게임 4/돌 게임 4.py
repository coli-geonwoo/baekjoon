#9658. 돌게임4

#1, 3, 4 마지막 돌을 가져가는 사람이 진다.

n= int(input())

dp=[0] * (max(n+1, 6))

#상근이 먼저 시작
dp[1]=1
dp[3]=1
dp[4]=0

for i in range(5, n+1):
  if (dp[i-1]==1 or dp[i-3]==1 or dp[i-4]==1):
    dp[i]=0
  else:
    dp[i]=1

if dp[n]==1:
  print("CY")
else:
  print("SK")
    