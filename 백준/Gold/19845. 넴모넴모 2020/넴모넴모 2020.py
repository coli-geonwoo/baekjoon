import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline().strip('\n')

height, t= map(int, input().split())

nemo = list(map(int, input().split()))
max_nemo= max(nemo)
nemo_sorted = sorted(nemo)

for _ in range(t):
  x,y= map(int, input().split())

  if x>max_nemo or y>height:
    print(0)
    continue
  right = max(nemo[y-1] -x,0)
  cutline = bisect_left(nemo_sorted, x)
  cutline = height-cutline
  up =  max(cutline-(y-1),0)
  #print(up, right, cutline)
  print(up+right)