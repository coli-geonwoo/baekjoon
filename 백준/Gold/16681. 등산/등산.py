import heapq
import sys

input = lambda: sys.stdin.readline().strip('\n')
def dijkstra(start):
  q= []
  distance=[INF] * (node+1)
  distance[start]=0
  heapq.heappush(q, (0,start))

  while(q):
    d, current_node = heapq.heappop(q)

    #이미 작은 것 찾았다면 스킵 
    if distance[current_node]<d:
      continue

    for next_node, next_distance in graph[current_node]:
      #오르기만 가능
      if heights[current_node] >= heights[next_node]:
          continue

      if distance[next_node]> d+next_distance:
        distance[next_node]= d+next_distance
        heapq.heappush(q, (distance[next_node], next_node))
  
  return distance

#power : 거리당 소모되는 체력
#money : 높이당 가질 수 있는 성취
node, edge, power, money = map(int, input().split())
graph=[[] for _ in range(node+1)]
heights = [0]+ list(map(int, input().split()))
INF = sys.maxsize

for _ in range(edge):
  a,b,k= map(int, input().split())
  if a==b:
    continue

  graph[a].append((b,k))
  graph[b].append((a,k))

#출발점에서 갈 수 있는 최소거리
start_distance =  dijkstra(1)

#고려대에서 갈 수 있는 최소거리
end_distance = dijkstra(node)

result=[]

for i in range(1, node+1):
  if start_distance[i]!=INF and end_distance[i]!=INF:
    result.append(money * heights[i] - (start_distance[i]+end_distance[i])*power)

#print(result)

if len(result)==0:
  print("Impossible")
else:
  print(max(result))
