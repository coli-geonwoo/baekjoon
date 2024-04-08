import copy
import sys

input = lambda: sys.stdin.readline().strip('\n')

def makeResult(result, lens, remain_zero, remain_one, remain_two):
  global n

  if n==1:
    if(result[0]%3 !=0):
      return result
    else:
      return []
  before = result[0]

  flag=True
  for _ in range(n-1):
    #print(result)
    if before%3==0:
      if lens[1]==0 and lens[2]==0:
        flag=False
        break
      if lens[1] <lens[2]:
        result.append(remain_two.pop())
        lens[2]-=1
        before=2
      else:
        result.append(remain_one.pop())
        lens[1]-=1
        before=1
    elif before%3==1:
      if lens[1]==0 and lens[0]==0:
        flag=False
        break
      if lens[1] <lens[0]:
        result.append(remain_zero.pop())
        lens[0]-=1
        before=0
      else:
        result.append(remain_one.pop())
        lens[1]-=1
        before=1
    else:
      if lens[0]==0 and lens[2]==0:
        flag=False
        break
      if lens[0] <lens[2]:
        result.append(remain_two.pop())
        lens[2]-=1
        before=2
      else:
        result.append(remain_zero.pop())
        lens[0]-=1
        before=0

  if flag==False:
    return []
  else:
    return result


n= int(input())
nums= list(map(int, input().split()))
remain_zero  = [i for i in nums if i%3==0]
remain_one  = [i for i in nums if i%3==1]
remain_two  = [i for i in nums if i%3==2]

remains= [remain_zero, remain_one, remain_two]

lens= [len(remain_zero), len(remain_one), len(remain_two)]


idxs = [0,1,2]

flag=False
for idx in idxs:
  if lens[idx]==0:
    continue

  aa= remains[idx].pop()
  temp = [aa]
  lens_copy= copy.deepcopy(lens)
  lens_copy[idx]-=1
  result = makeResult(temp, lens_copy, copy.deepcopy(remains[0]), copy.deepcopy(remains[1]), copy.deepcopy(remains[2]))
  remains[idx].append(aa)

  if len(result) >0:
    print(*result)
    flag=True
    break

if flag==False:
  print(-1)