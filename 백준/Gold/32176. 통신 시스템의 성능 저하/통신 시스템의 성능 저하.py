import sys
from itertools import combinations

def find_case(k):
    if(k==0):
        return 0
    cases = list(combinations(indexs, k))
    result = 0

    for c in cases:
        temp = [nodes[i] for i in c]
        d=0
        for node in temp:
            d += distance(gijiguk, node)
        u = square(temp)
        result = max(result, d-u)
    return result

def square(nodes):
    minX = sys.maxsize
    maxX = -sys.maxsize
    minY = sys.maxsize
    maxY = -sys.maxsize

    for x,y in nodes:
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)

    return (maxX- minX+1)*(maxY-minY+1)


#거리 구하기
def distance(node1, node2):
    return abs(node1[0]- node2[0]) + abs(node1[1]- node2[1])


n,m, k1, k2 = map(int, input().split())

data = [list(input()) for _ in range(n)]
gijiguk = -1 #기지국
nodes =[] # 노드들

for i in range(n):
    for j in range(n):
        if data[i][j] =="B":
            gijiguk = (i,j)
        if(data[i][j] =="N"):
            nodes.append((i,j))


indexs = [i for i in range(m)]

print(find_case(k1))
print(find_case(k2))