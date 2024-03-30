import heapq

n= int(input())
number = [int(input()) for _ in range(n)]

total=0
zero_cnt=0
minus=[]
plus=[]

for i in number:
  if i<0:
    heapq.heappush(minus, i)
  elif i==1:
    total+=1
  elif i==0:
    zero_cnt+=1
  else:
    heapq.heappush(plus, -i)


while(minus):
  if len(minus)==1:
    if zero_cnt==0:
      total += heapq.heappop(minus)
    else:
      total+= heapq.heappop(minus)*0
  else:
    total+= heapq.heappop(minus) * heapq.heappop(minus)

while(plus):
  if len(plus)==1:
    total -= heapq.heappop(plus)
  else:
    total += heapq.heappop(plus) * heapq.heappop(plus)

print(total)