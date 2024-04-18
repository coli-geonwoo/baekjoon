#9251. LCS(골5)
a= list(input())
b= list(input())
n1 = len(a)
n2= len(b)
dp=[[0]*(n1+1) for _ in range(n2+1)]

for i in range(1, n2+1):
  for j in range(1, n1+1):
    if b[i-1]== a[j-1]:
      dp[i][j]= dp[i-1][j-1]+1
    else:
      dp[i][j]= max(dp[i][j-1], dp[i-1][j])

print(dp[n2][n1])