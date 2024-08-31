import sys
import math
from collections import deque
from collections import defaultdict

input = lambda: sys.stdin.readline().strip('\n')

def distance(x1,y1, x2, y2):
    return math.sqrt(abs(x1-x2) **2 + abs(y1-y2)**2)

take = defaultdict(int)

#친구의 수, 에어드롭의 최대 거리, 최대 휴대폰 버전 차이
n,k,t = map(int, input().split())
px,py, pv = map(int, input().split())
visited = [0]*(n)
friends = []

for i in range(n):
    f = list(map(int, input().split()))
    #사진 찍음
    if(f[-1]==1):
        take[i]=1
    friends.append(f)

q=deque([(px, py, pv)])

while(q):
    nx, ny, nv = q.popleft()

    for i, f_node in enumerate(friends):
        fx,fy,fv, ft= f_node
        if (fx==nx and fy==ny) or visited[i]==1:
            continue

        if(distance(nx, ny, fx, fy) <=k and abs(nv-fv)<=t):
            visited[i]=1
            q.append((fx,fy,fv))


result=[]
for i in range(n):
    if(visited[i]==1 and take[i]==1):
        result.append(i+1)

if(len(result)==0):
    print(0)
else:
    print(*result)