import sys

input = lambda: sys.stdin.readline().strip('\n')

def dfs(x,y, dist):
  global n, answer
  if x<0 or y<0 or x>=n or y>=n or data[x][y]==1:
    return
  
  if x==n-1 and y==n-1:
    answer+=1
    return
  
  if dist==0:
    dfs(x, y+1, 0)
    if 0<=x+1<n and 0<=y+1<n and data[x+1][y]==0 and data[x][y+1]==0:
      dfs(x+1, y+1, 2)
  if dist==1:
    dfs(x+1, y, 1)
    if 0<=x+1<n and 0<=y+1<n and data[x+1][y]==0 and data[x][y+1]==0:
      dfs(x+1, y+1, 2)
  if dist==2:
    dfs(x, y+1, 0)
    dfs(x+1, y, 1)
    if 0<=x+1<n and 0<=y+1<n and data[x+1][y]==0 and data[x][y+1]==0:
      dfs(x+1, y+1, 2)

#가로, 세로, 대각선
n= int(input())
data= [list(map(int, input().split())) for _ in range(n)]
dp=[[[0]*n for _ in range(n)] for _ in range(3)]

answer=0

if data[n-1][n-1]==0 and data[0][2]==0:
  dfs(0,1,0)
print(answer)