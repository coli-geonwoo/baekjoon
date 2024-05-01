n= int(input())
score=list(map(int, input().split()))

dp=[1]*n

for i in range(1, n):
  for j in range(0,i):
   if score[j]<score[i]:
    dp[i]= max(dp[i], dp[j]+1)

print(max(dp))