#차이를 M이상으로

# 조건을 만족하지 않는 케이스에 대하여 1 - n까지 검사

n,m= map(int, input().split())
nums = list(map(int, input().split()))
check = [False] * n
cnt=0

for i in range(1, n):
    diff = nums[i] - nums[i-1]
    if check[i-1] ==False and abs(diff) <m:
        check[i]=True
        cnt+=1

print(cnt)