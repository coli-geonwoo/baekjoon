#16947. 서울 지하철 2호선
import sys
import heapq

def find_parent(x):

    if(parent[x]!= x):
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a= find_parent(a)
    b= find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


def dijkstra(start, end, op):
    q = [(0, start)]

    while (q):
        cost, node = heapq.heappop(q)

        if distance[node] < cost:
            continue

        if op==0 and node == end:
            return

        for next_node in graph[node]:
            if op==0:
                if visited[next_node] == 0 and distance[next_node] > cost + 1:
                    visited[next_node] = 1
                    before_node[next_node] = node
                    distance[next_node] = cost + 1
                    heapq.heappush(q, (cost + 1, next_node))
            if (op == 1):
                if visited[next_node] ==0:
                    visited[next_node] =1
                    if cycle[next_node]== True and distance[next_node] > cost:
                        heapq.heappush(q, (cost, next_node))
                        distance[next_node] = cost
                    if cycle[next_node] == False and distance[next_node] > cost+1:
                        heapq.heappush(q, (cost + 1, next_node))
                        distance[next_node] = cost+1

    return distance



n= int(input())
graph= [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
before_node = [0] *(n+1)


#두 사이클 노드 찾기
cycle_start=-1
cycle_end= -1

for _ in range(n):
    a,b = map(int, input().split())

    if find_parent(a) == find_parent(b):
        cycle_start = a
        cycle_end = b
        continue

    union_parent(a,b)
    graph[a].append(b)
    graph[b].append(a)

before_node[cycle_start] = cycle_start

visited = [0] * (n + 1)
visited[cycle_start] = 1
distance = [n+1] * (n + 1)
distance[cycle_start]=0

dijkstra(cycle_start, cycle_end, 0)


cycle= [False]*(n+1)
current_node = cycle_end
cycle[cycle_start] = True
cycle[cycle_end] = True

while(current_node!= cycle_start):
    cycle[current_node] = True
    current_node = before_node[current_node]

visited = [0] * (n + 1)
visited[cycle_start] = 1
distance = [n+1] * (n + 1)
distance[cycle_start]=0
result = dijkstra(cycle_start, cycle_end, 1)
print(*result[1:])






