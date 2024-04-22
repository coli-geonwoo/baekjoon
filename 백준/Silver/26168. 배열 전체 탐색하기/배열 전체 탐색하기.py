from bisect import bisect_left, bisect_right

def func(op, k):
  global nums
  if len(list(k.split()))==1:
    k= int(k)
    if op==1:
      idx = bisect_left(nums, k)
      return n-idx
    elif op==2:
      idx = bisect_right(nums, k)
      return n-idx
  else:
    a1,a2 = map(int, k.split())
    return func2(a1, a2)

def func2(a1, a2):
  global nums 
  idx1 = bisect_left(nums, a1)
  cnt1 = n-idx1
  idx2= bisect_right(nums, a2)
  return max(idx2-idx1,0)



n,m= map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for _ in range(m):
  ops = input()
  print(func(int(ops[0]), ops[2:]))

