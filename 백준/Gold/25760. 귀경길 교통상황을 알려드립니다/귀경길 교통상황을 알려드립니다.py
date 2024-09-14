#25760. 귀경길 교통상황을 알려드립니다

#양방향 도로
# 1. 대기
# 2. 도로망 빠져나가기
# 3. 다른 지점으로 이동하기 대기/ 이동 차량 존재 시 x

import sys
import heapq
from collections import defaultdict

def dijkstra(start):
    distance[start] =0
    q= [(0, start)]
    while(q):
        d , current_node = heapq.heappop(q)

        if d> distance[current_node]:
            continue

        for next_node in graph[current_node]:
            next_cost = d+1
            if(next_cost < distance[next_node]):
                distance[next_node]= next_cost
                heapq.heappush(q, (next_cost, next_node))

INF = sys.maxsize
n= int(input())
distance =[INF]* (n+1)
graph =[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cars =[0] + list(map(int, input().split()))
car_with_level = defaultdict(list)
dijkstra(1)
for i in range(n+1):
    if(cars[i]==1):
        level = distance[i]
        if(level == INF):
            continue
        car_with_level[level].append(i)

result = 0
frontCarNum =0
levels = sorted(list(car_with_level.keys()), reverse=True)

for level in levels:
    cars= car_with_level[level]
    frontCarNum += len(cars)
    result = max(result, frontCarNum +level)
print(result)


