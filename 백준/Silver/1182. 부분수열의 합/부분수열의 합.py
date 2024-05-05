from itertools import combinations 

n,s= map(int, input().split())
nums= list(map(int, input().split()))

cnt=0

for i in range(1, n+1):
  cases=list(combinations(nums, i))
  answer =[ c for c in cases if sum(c)==s]
  cnt+=len(answer)

print(cnt)