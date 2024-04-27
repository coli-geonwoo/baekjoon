import sys

sys.setrecursionlimit(10000)

def dfs(start, before, node,cost):
  global result
  
  if node!=start and len(graph[node])==1:
    result = max(result, cost)
    return
  
  for next_node, next_cost in graph[node]:
    if next_node==start or next_node==before:
      continue

    dfs(start, node, next_node, cost+next_cost)



n= int(input())

graph =[[] for _ in range(n+1)]

for _ in range(n-1):
  a,b,c= map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))


starts=[]

for i in range(1, n+1):
  if len(graph[i])==1:
    starts.append(i)


result= 0

for start in starts:
  dfs(start, start, start, 0)


print(result)