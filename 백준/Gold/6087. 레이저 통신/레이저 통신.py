#6087. 레이저 통신(골3)
# 한방향으로 쭉 탐색

import sys, heapq
input = lambda: sys.stdin.readline().strip('\n')

def dijkstra(start, end):
  INF = sys.maxsize
  #동서남북 3차원 배열
  distance=[[[INF] * m for _ in range(n)] for _ in range(4)]
  q=[]
  for i in range(4):
    distance[i][start[0]][start[1]]=0
    heapq.heappush(q, (0, i, start[0], start[1]))
  
  while(q):
    cost, dist, x, y = heapq.heappop(q)
    
    if cost > distance[dist][x][y]:
      continue
    
    for i in range(4):
      nx= x+dx[i]
      ny= y+dy[i]
      
      #범위 초과 혹은 벽이면 탐색 중지
      if nx<0 or ny<0 or nx>=n or ny>=m or data[nx][ny]=="*":
          continue

      #왔던 방향이면 그대로, 꺾으면 +1 
      if i==dist:
        next_cost=cost
      else:
        next_cost=cost+1
    
      if distance[i][nx][ny] > next_cost:
        distance[i][nx][ny]= next_cost
        heapq.heappush(q, (next_cost, i, nx, ny))
  
  ex= end[0]
  ey= end[1]
  result=[distance[0][ex][ey], distance[1][ex][ey], distance[2][ex][ey], distance[3][ex][ey]]
  return min(result)


dx=[0,0,-1,1]
dy=[-1,1,0,0]

m,n = map(int, input().split())
data= []
point=[]

for i in range(n):
  temp = list(input())
  if "C" in temp:
    for idx, k in enumerate(temp):
      if k=="C":
        point.append((i, idx))
  data.append(temp)


print(dijkstra(point[0], point[1]))


