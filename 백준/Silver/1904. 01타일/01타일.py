n = int(input())
dp= [0]*2
dp[0]=0
dp[1]=1

for i in range(n):
  temp=dp[1]
  dp[1]= (dp[0]+temp)%15746
  dp[0]=temp

print(dp[1])