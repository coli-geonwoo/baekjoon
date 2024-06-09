#1577. 도로의 개수(골5)

from collections import defaultdict

n,m= map(int, input().split())
k= int(input())

dp=[[0]*(m+1) for _ in range(n+1)]

broken_roads = defaultdict(list)

for _ in range(k):
  a,b,c,d= map(int, input().split())
  broken_roads[(c,d)].append((a,b))
  broken_roads[(a,b)].append((c,d))


for i in range(n+1):
  for j in range(m+1):
    if i==0 and j==0:
      dp[i][j]=1
      continue

    from_left= (i, j-1)
    from_up = (i-1, j)
    now= (i,j)

    if i==0:
      if from_left not in broken_roads[now]:
        dp[i][j]=dp[i][j-1]
      continue

    if j==0:
      if from_up not in broken_roads[now]:
        dp[i][j]=dp[i-1][j]
      continue

    if from_left not in broken_roads[now]:
      dp[i][j]+=dp[i][j-1]

    if from_up not in broken_roads[now]:
      dp[i][j]+=dp[i-1][j]

print(dp[n][m])
