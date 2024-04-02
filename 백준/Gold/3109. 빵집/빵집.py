#빵집(골2)

n, m = map(int, input().split())

root = [list(input()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

dx=[-1,0,1]


def progress(x,y):
  #끝에 다다랐으면 결과+1
  if y==m-1:
    return True
    
  ny= y+1
  for i in range(3):
    nx= x+dx[i]
    if nx<0 or nx>=n or ny>=m:
      continue
    if root[nx][ny]!="x" and visited[nx][ny]==0:
      visited[nx][ny]=1
      if(progress(nx, ny)):
          return True
  return False

result=0 
for i in range(n):
    if(progress(i,0)):
      result+=1
    
print(result)