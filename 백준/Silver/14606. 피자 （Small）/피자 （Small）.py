#14606. 피자(실5)

n= int(input())

dp=[0]*(n+1)


for i in range(n, 0, -1):
  for j in range(1, i):
    dp[j]= max(dp[i]+j*(i-j), dp[j])

print(dp[1])