import sys

sys.setrecursionlimit(1000)

def find_parent(x):
    if x!= parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a= find_parent(a)
    b= find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m = map(int, input().split())

edges=[]
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()

cnt=0
result=0
for i in range(m):
    if cnt==n-1:
        break
    cost, a,b = edges[i]

    if(find_parent(a) == find_parent(b)):
        continue

    union_parent(a,b)
    result+=cost
    cnt+=1

print(result)