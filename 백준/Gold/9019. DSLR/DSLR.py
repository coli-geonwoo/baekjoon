from collections import deque

#input = lambda: sys.stdin.readline().strip('\n')


def cal(a, i):
  if i==0:
    return (a*2)%10000

  if i==1:
    if a==0:
      return 9999
    else:
      return a-1

  if i==2:
    a = str(a)
    if len(a)<4:
      return int(a+"0")

    return int(a[1:] + ("0"*(4-len(a))) + a[0])
  
  if i==3:
    a= str(a)
    return int(a[-1] + ("0"*(4-len(a))) + a[:len(a)-1])

def bfs(start, end):
  global r
  q= deque([(start, "")])
  visited = [0]*10000
  result = "1"*10000
  while(q):
    num, path = q.popleft()

    if num==end and len(path)<len(result):
      result = path
    
    for i in range(4):
      c = cal(num, i)
      if visited[c]==1:
        continue
      
      visited[c]=1
      q.append((c, path+r[i]))
  
  return result

r = ["D", "S", "L", "R"]

n= int(input())
for i in range(n):
  a,b= map(int, input().split())
  print(bfs(a,b))



