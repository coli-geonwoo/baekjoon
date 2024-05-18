dist, length = map(int, input().split())
mod = 1000000007
dp=[[0]*27 for _ in range(length+1)]

dp[1]= [1]*27

for i in range(2, length+1):
  for j in range(1, 27):
    temp=0
    for k in range(1, 27):
      #dist이상의 차이가 나는 케이스를 모두 더함
      if abs(j-k)>=dist: 
        temp=(temp+dp[i-1][k])%mod
    dp[i][j]=temp

print(sum(dp[length])%mod)