#줄임말
from collections import defaultdict
from bisect import bisect_right

target = list(input())
source = list(input())

nums_idx=defaultdict(list)

for idx,i in enumerate(source):
  nums_idx[i].append(idx)


result=1
before_index = -1
current_index =-1
flag=True

for c in target:  
  if len(nums_idx[c])==0:
    flag=False
    break
  
  flag2=True
  current_index = bisect_right(nums_idx[c], before_index)
  if current_index >= len(nums_idx[c]):
      result+=1
      current_index = 0

  before_index = nums_idx[c][current_index]


if flag:
  print(result)
else:
  print(-1)


