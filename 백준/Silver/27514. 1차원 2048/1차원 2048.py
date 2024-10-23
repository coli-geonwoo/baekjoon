#27514
from collections import defaultdict
n= int(input())

cnt = defaultdict(int)

nums = list(map(int, input().split()))
result =0

for k in nums:
    if cnt[k]==0:
        cnt[k]+=1
        result = max(result, k)
        continue

    while(True):
        #1일 경우
        if cnt[k] ==0:
            cnt[k]+=1
            break
        cnt[k]-=1
        result = max(result, 2*k)
        k*=2

print(result)
