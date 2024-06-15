#자연수 색칠하기
import math

n= int(input())
color =[-1]*(n+1)

color[1]=1
cnt=2
for i in range(2, int(math.sqrt(n))+1):
  if color[i]==-1:
    for j in range(i, n+1, i):
      color[j]=cnt
    cnt+=1

for i in range(2, n+1):
  if color[i]== -1:
    color[i]=cnt
    cnt+=1

print(len(set(color[1:])))
print(*color[1:])

