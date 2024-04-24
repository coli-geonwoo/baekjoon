#27968. 사사의 사차원 사탕봉지(실2)
import sys
from bisect import bisect_right

input = lambda: sys.stdin.readline().strip('\n')

n,m = map(int, input().split())

candy = list(map(int,input().split()))
total = sum(candy)
for i in range(1, len(candy)):
  candy[i]+=candy[i-1]

for i in range(n):
  demand = int(input())
  if demand>total:
    print("Go away!")
  else:
    idx= bisect_right(candy,demand)
    if idx==0 or candy[idx-1]<demand:
      print(idx+1)
    else:
      print(idx)