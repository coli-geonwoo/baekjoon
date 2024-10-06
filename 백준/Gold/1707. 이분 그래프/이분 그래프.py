from collections import deque

def bfs():
    color[1] = 1
    q = deque([1])
    cnt=0

    while (cnt!=n):
        if len(q)==0:
            flag=True
            for i in range(1,n+1):
                if color[i]==0:
                    color[i]=1
                    q.append(i)
                    flag=False
                    break
            if flag:
                break

        node = q.popleft()

        for next_node in graph[node]:
            if color[next_node] == color[node]:
                return False

            if color[next_node] == 0:
                if color[node] == 1:
                    color[next_node] = 2
                    q.append(next_node)
                if color[node] == 2:
                    color[next_node] = 1
                    q.append(next_node)
        cnt+=1

    return True

t= int(input())

for _ in range(t):
    n,m= map(int, input().split())

    graph = [[] for _ in range(n+1)]

    #인접한 정점의 색깔이 달라야 한다
    color = [0]*(n+1)

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    if(bfs()):
        print("YES")
    else:
        print("NO")








