#32. 카드합체놀이(실1)

import heapq

n,m= map(int, input().split())
number = list(map(int, input().split()))
q=[]
for i in number:
  heapq.heappush(q, i)

for _ in range(m):
  a= heapq.heappop(q)
  b= heapq.heappop(q)
  heapq.heappush(q, (a+b))
  heapq.heappush(q, (a+b))

print(sum(q))