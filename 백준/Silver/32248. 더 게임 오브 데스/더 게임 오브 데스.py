n,m= map(int, input().split())

link = [0]+ list(map(int, input().split()))
idx=1
result=0

visited = [-1] *(n+1) #방문했는지

for i in range(1,m+1):
    result = link[idx]
    if(visited[result]!=-1):
        cnt = i - visited[result]
        idx= result
        for j in range((m-i)%cnt):
            result = link[idx]
            idx= result
        break
    visited[result]=i
    idx= result

print(result)
