# 14621. 나만 안되는 연애


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b



# 학교, 도로
n, m = map(int, input().split())

gender = ['N'] + list(map(str, input().split()))
parent = [i for i in range(n + 1)]

edges = []
for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((cost, start, end))

edges.sort()

result = 0
cnt=0

for cost, sn, en in edges:
    if gender[sn] == gender[en]:
        continue
    
    if(find_parent(sn) != find_parent(en)):
        union_parent(sn, en)
        result+=cost
        cnt+=1

if cnt!= n-1:
    print(-1)
else:
    print(result)