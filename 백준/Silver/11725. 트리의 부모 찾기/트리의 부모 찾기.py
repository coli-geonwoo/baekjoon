
from collections import deque
n= int(input())
graph=[[] for _ in range(n+1)]
parent = [0]* (n+1)


for _ in range(n-1):
  a,b= map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited=[0]*(n+1)
visited[1]=1
q=deque([1])

while(q):
  v= q.popleft()
  for i in graph[v]:
    if visited[i]==0:
      parent[i]=v
      visited[i]=1
      q.append(i)

print(*parent[2:], sep="\n")