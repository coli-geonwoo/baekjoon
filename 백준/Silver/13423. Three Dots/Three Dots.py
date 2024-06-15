from collections import defaultdict
t= int(input())
for _ in range(t):
  distinct = defaultdict(bool)
  n= int(input())
  nums = list(map(int, input().split()))
  for i in nums:
    distinct[i] =True

  cnt=0

  for i in range(n-1):
    for j in range(i+1, n):
      if (nums[i]+nums[j])%2!=0:
        continue
      if distinct[(nums[i]+nums[j])//2]:
        cnt+=1

  print(cnt)

        