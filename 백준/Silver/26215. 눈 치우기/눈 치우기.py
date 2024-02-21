import heapq

n = int(input())

k= [-i for i in list(map(int, input().split()))]
snow=[]

for i in k:
  heapq.heappush(snow, i)
time=0
impossibleFlag=False

while(1):
  if len(snow)<2:
    time-= heapq.heappop(snow)
  else:
    biggest = -heapq.heappop(snow)
    second_biggest = -heapq.heappop(snow)
    time += second_biggest
    heapq.heappush(snow, second_biggest-biggest)
  
  if time>1440:
    impossibleFlag=True
    break
  
  if len(snow)==0:
    break

if impossibleFlag:
  print(-1)
else:
  print(time)