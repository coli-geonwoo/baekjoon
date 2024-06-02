#7795. 먹을 것인가 먹힐 것인가

from bisect import bisect_left

t= int(input())

for _ in range(t):
  a_num, b_num = list(map(int, input().split()))

  a= list(map(int, input().split()))
  b= list(map(int, input().split()))
  result=0

  b.sort()

  for i in a:
    idx= bisect_left(b, i)
    result+=idx
  
  print(result)