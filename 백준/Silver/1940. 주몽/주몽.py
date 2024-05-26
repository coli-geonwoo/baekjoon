
import heapq
n= int(input())
m= int(input())
nums = list(map(int, input().split()))
q=[]
for i in nums:
  heapq.heappush(q, i)

cnt=0

while(q):
  num = heapq.heappop(q)
  if m-num in q:
    cnt+=1
print(cnt)