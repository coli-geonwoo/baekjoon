def dfs(x,y, cnt):
  global health, visited, result,h
  cost = abs(sx-x) + abs(sy-y)
  if(cost<=health):
    result = max(result, cnt)
  
  for i,j in milk:
    if visited[i][j]==1:
      continue
    
    d = abs(x-i) + abs(y-j) #필요한 체력
    if d>health:
      continue

    health-=d
    health+=h
    visited[i][j]=1
    dfs(i,j, cnt+1)
    visited[i][j]=0
    health+=d
    health-=h


dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 판의 크기, 초기체력, 체력회복
n,m,h = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
sx=sy=0
health= m

result=0
milk= []

for i in range(n):
  for j in range(n):
    if data[i][j]==1:
      sx= i
      sy=j
    elif data[i][j]==2:
      milk.append((i,j))


dfs(sx, sy, 0)
print(result)