#위에서부터 내려오기

import heapq
import copy
import sys

input = lambda: sys.stdin.readline().strip('\n')

def getCount(q):
  global graph, height
  dp = [0]*n #거쳐갈 수 있는 등산로

  while(q): 
    h, num = heapq.heappop(q)
    h=-h
    temp=[]

    if len(graph[num])==0: #연결된 쉼터가 하나도 없다면 = 1
      dp[num]= 1
    else:
      for next_place in graph[num]:
        temp.append(dp[next_place]) #연결된 쉼터 중 최대값
      dp[num]= max(temp)+1

  return dp

n,m= map(int, input().split())
graph=[[] for _ in range(n)]
height = list(map(int, input().split()))
q=[]

for _ in range(m):
  a,b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

for i in range(n):
  heapq.heappush(q, (-height[i], i))

result= getCount(q)

print(*result,sep="\n")
  