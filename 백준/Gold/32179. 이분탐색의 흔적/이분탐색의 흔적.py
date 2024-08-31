import math
import sys

input = lambda: sys.stdin.readline().strip('\n')

n,m= map(int, input().split())
nums= [-1]*(n) #숫자
left =0
right = n-1

#숫자 채우기
bi_nums = list(map(int, input().split()))

#초반 1개의 숫자
mid= (left + right)//2
nums[mid]=bi_nums[0]
before = bi_nums[0]


#뒤의 숫자들 채우기
for b in bi_nums[1:]:
    if before <b:
        left= mid+1
        mid= (left+right)//2
        nums[mid]=b
    else:
        right = mid-1
        mid = (left + right) // 2
        nums[mid] = b
    before =b

s=0
answer = 1
cnt=0
mod = 1000000007

for i in nums:
    # 숫자가 없으면 골라야 하는 cnt값 +1
    if i==-1:
        cnt+=1
        continue

    # 골라야 하는 조합의 개수가 없다면 더하지 않음
    if(cnt!=0):
        answer = (answer*math.comb(i-1-s,cnt))%mod
    s=i
    cnt=0

if(nums[-1]==-1):
    answer = (answer*math.comb(100-s,cnt))%mod

print(answer)