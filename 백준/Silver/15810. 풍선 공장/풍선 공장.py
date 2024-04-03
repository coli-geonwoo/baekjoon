import sys
input = lambda: sys.stdin.readline().strip('\n')
baloon_cnt, result =map(int, input().split())
speed = list(map(int, input().split()))
speed.sort()

left =0
right =speed[0]*result
m=0

while(left<=right):
  mid = (left+right)//2
  total=0
  flag=True
  for i in speed:
    total+= mid//i
    if total>=result:
      flag=False
      break
  
  if flag:
    left= mid+1
  else:
    #시간 줄이기
    right= mid-1
    m=mid


print(m)

