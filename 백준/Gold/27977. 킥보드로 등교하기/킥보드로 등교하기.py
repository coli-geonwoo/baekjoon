from bisect import bisect_left

n,m,k= map(int, input().split())
road = [0]+ list(map(int, input().split()))  + [n]
distance=[]
for i in range(1, m+2):
  distance.append(road[i]- road[i-1])

left=0
right= n
result=0

road=road[1:]

while(left<=right):
  mid = (left+right)//2
  flag=False

  before_idx=-1
  cnt=0
  place=mid
  
  while(1):
    # 더 많이 방문했다면 break
    if cnt>k:
      break
    if place>=n:
      flag=True
      break

    idx = bisect_left(road, place)
    #print(idx, mid, place, road)
    
    if place==road[idx]:
      place+=mid
    else:
      if idx<=0:
        break
      place= road[idx-1]+mid
      idx= idx-1

    if before_idx==idx:
      break

    before_idx=idx
    cnt+=1

  #print(place, flag, mid)
  if flag:
    result=mid
    right=mid-1
  else:
    left=mid+1


print(result)