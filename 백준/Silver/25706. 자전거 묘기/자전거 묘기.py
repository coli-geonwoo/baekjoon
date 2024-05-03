import sys

input = lambda: sys.stdin.readline().strip('\n')

n= int(input())
road = list(map(int, input().split()))

dp= [n]*n

dp[n-1]=1

for i in range(n-2, -1, -1):
  #점프대가 있다면
  if road[i]!=0:
    if (i+road[i]+1)>=n:
      dp[i]=1
    else:
      dp[i]= dp[i+road[i]+1]+1
  else:
    dp[i]= min(dp[i], dp[i+1]+1)
  
print(*dp)
 