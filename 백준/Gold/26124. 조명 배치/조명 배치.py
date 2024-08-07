#26124

flag =True
n,m= map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cnt=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]


for i in range(n):
  for j in range(m):
    if(flag==False):
      break

    if(data[i][j]>0):
      light=True
      for k in range(4):
        nx = i+dx[k]
        ny = j +dy[k]

        if(nx<0 or ny<0 or nx>=n or ny>=m or data[nx][ny]==-1):
          continue

        if(abs(data[nx][ny]- data[i][j])>1):
          flag=False
          cnt=-1
          break
        
        #4방향 모두 이것보다 작으면
        if(data[nx][ny]>data[i][j]):
          light=False
          break
      if(light):
        cnt+=1
  if(flag==False):
    break

if(flag):
  print(cnt)  
else:
  print(-1)
      

