#31848

from collections import defaultdict
from bisect import bisect_left, bisect_right
import sys

n= int(input())
m= list(map(int, input().split()))
holes=[]
hole_idx = defaultdict(list)

for idx, i in enumerate(m):
    holes.append((idx+i))
    hole_idx[idx+i].append(idx+1)

#print(holes)

holes.sort()

k= int(input())
dotori = list(map(int, input().split()))
result = []

min_idx = [0]*n

m= sys.maxsize

for i in range(n-1, -1, -1):
    m =  min(m, min(hole_idx[holes[i]]))
    min_idx[i] = m


for d in dotori:
    idx = bisect_left(holes, d)
    #print(d, idx, holes[idx+1], hole_idx[holes[idx+1]])
    result.append(min_idx[idx])

print(*result)
