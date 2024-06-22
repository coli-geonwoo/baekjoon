#1167. 트리의 지름
#dfs

import sys

n= int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n):
  data = list(map(int, input().split()))
  s= data[0]
  temp = data[1:-1]
  for i in range(0, len(temp), 2):
    graph[s].append((temp[i], temp[i+1]))


def dfs(cost, node):
  global result, visited, max_node
  flag=True
  if cost> result:
    result = cost
    max_node = node
  for next_node, next_cost in graph[node]:
    if visited[next_node]==0:
      visited[next_node]=1
      dfs(cost+next_cost, next_node)


result=0
max_node=-1

visited = [0]*(n+1)
visited[1]=1
dfs(0, 1)

visited = [0]*(n+1)
visited[max_node]=1
dfs(0, max_node)

print(result)

