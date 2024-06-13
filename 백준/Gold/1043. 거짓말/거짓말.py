#1043. 거짓말(골4)
import sys
import heapq

INF = sys.maxsize
n,m= map(int, input().split())

graph=[[] for _ in range(n+1)]
party=[]
know = list(map(int, input().split()))

if len(know)==1:
  print(m)
else:
  know = know[1:]

  for _ in range(m):
    nums = list(map(int, input().split()))
    party.append(nums[1:])
    for j in nums[1:]:
      for k in nums[1:]:
        if j==k:
          continue
        graph[j].append(k)

  #print(graph)
  def dijkstra():
    distance= [INF] * (n+1)
    q=[]
    for i in know:
      distance[i]=0
      heapq.heappush(q, (0, i))
    
    while(q):
      dist, now = heapq.heappop(q)

      for next_node in graph[now]:
        if dist+1 < distance[next_node]:
          distance[next_node]= dist+1
          heapq.heappush(q, (dist+1, next_node))
    
    result=[]
    #print(distance)
    for i in range(1, n+1):
      if distance[i]==INF:
        result.append(i)
    return result

  result = dijkstra()

  cnt=0
  for p in party:
    flag=True
    for i in p:
      if i not in result:
        flag=False
        break
    
    if flag:
      cnt+=1

  print(cnt)

    