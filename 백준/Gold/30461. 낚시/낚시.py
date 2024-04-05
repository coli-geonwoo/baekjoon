#30461. 낚시(골4)

import sys
input = lambda: sys.stdin.readline().strip('\n')


def getsum(x,y):
  global data,n,m
  x+=1
  y+=1
  while(True):
    if x>n-1 or y>m-1:
      break
    data[x][y]+=data[x-1][y-1]
    x+=1
    y+=1

n,m,t= map(int, input().split())

data= [list(map(int, input().split())) for _ in range(n)]

if n>1:
  for i in range(1,n):
    for j in range(m):
      data[i][j] += data[i-1][j]
  for i in range(m):
    getsum(0,i)
  
  for i in range(1, n):
    getsum(i,0)

for _ in range(t):
  x,y= map(int, input().split())  
  print(data[x-1][y-1])