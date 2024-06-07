import sys
input = lambda: sys.stdin.readline().strip('\n')

for _ in range(int(input())):
    n,m,money = map(int, input().split())

    
    nums = list(map(int, input().split()))

    if n==m:
      if sum(nums) <money:
        print(1)
      else:
        print(0)
      continue
    
    nums = [0]+ nums + nums[:m-1]

    for i in range(1, len(nums)):
      nums[i]+=nums[i-1]

    left=0
    right= m

    cnt=0
    for i in range(m, n+m):
      if nums[i] - nums[i-m] < money:
        cnt+=1

    print(cnt)  
