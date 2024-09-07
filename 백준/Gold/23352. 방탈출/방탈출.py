from collections import deque

dx= [-1, 1, 0, 0]
dy= [0,0,-1,1]

def bfs(a,b):
    visited = [[0] * m for _ in range(n)]
    visited[a][b]=1
    q= deque([(0, a,b)])

    points=[(0,0)]

    while(q):
        route, x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m or data[nx][ny]==0 or visited[nx][ny]==1:
                continue
            visited[nx][ny] = 1
            q.append((route+1, nx, ny))
            points.append((route+1, data[nx][ny]))

    points.sort(key= lambda x : (-x[0], -x[1]))
    return (points[0][0], data[a][b]+ points[0][1])

n,m= map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
results = []

for i in range(n):
    for j in range(m):
        if data[i][j] != 0:
            results.append(bfs(i,j))

results.sort(key = lambda x: (-x[0], -x[1]))

print(results[0][1])

