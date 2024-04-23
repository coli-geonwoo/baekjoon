import sys

INF= sys.maxsize
n,m= map(int, input().split())
dp = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a,b= map(int, input().split())
  dp[a][b]=1

#대각선 0으로
for i in range(1,n+1):
  for j in range(1, n+1):
    if i==j:
      dp[i][j]=0

#연결되어 있는 건 1로

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      if dp[a][b]>dp[a][k]+ dp[k][b]: 
        dp[a][b]= dp[a][k]+dp[k][b]


for i in range(1, n+1):
  for j in range(1, n+1):
    #대칭으로 판단가능한지 판단
    dp[i][j]= min(dp[i][j], dp[j][i])

cnt=0
for i in range(1, n+1):
  if INF not in dp[i][1:]:
    cnt+=1
print(cnt)