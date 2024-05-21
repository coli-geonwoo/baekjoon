from bisect import bisect_right
from collections import defaultdict
import sys
import math
input = lambda: sys.stdin.readline().strip('\n')

#좌표 구하는 함수
def getRange(x, y):
  if x>0 and y==0:
    return 0
  if x>0 and y>0:
    return 1
  if x==0 and y>0:
    return 2
  if x<0 and y>0:
    return 3
  if x<0 and y==0:
    return 4
  if x<0 and y<0:
    return 5
  if x==0 and y<0:
    return 6
  if x>0 and y<0:
    return 7

#기울기 구하는 함수
def calc(x,y):
  if x==0:
    return "x"
  if y==0:
    return "y"
  else:
    k= math.gcd(x,y)
    return (x//k, y//k)

def distance(x,y):
  return x**2+y**2

n,m= map(int, input().split())

#좌표 -> 기울기
data = defaultdict(lambda: defaultdict(list))
visited = defaultdict(int)

#과일들의 좌표
for _ in range(n):
  a,b= map(int, input().split())

  data[getRange(a,b)][calc(a,b)].append(distance(a,b)) #부동 소수점 오차 방지

for i in data.keys():
  for j in data[i].keys():
    data[i][j].sort()

result=0
for _ in range(m):
  a,b= map(int, input().split())
  if len(data[getRange(a,b)][calc(a,b)]) <=result:
    continue

  idx = bisect_right(data[getRange(a,b)][calc(a,b)], distance(a,b))
  result= max(result, idx)

print(result)