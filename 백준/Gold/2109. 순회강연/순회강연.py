
import heapq
n= int(input())
q=[]
for _ in range(n):
  price, day= map(int, input().split())
  heapq.heappush(q, (day, price))
result=[]

while(q):
  day, price = heapq.heappop(q)
  heapq.heappush(result, (price))
  if len(result) > day:
    heapq.heappop(result)
  #print(result)
print(sum(result))