from collections import defaultdict

n= int(input())
nums = list(map(int, input().split()))

nums = nums[::-1]
result= []
cnt = defaultdict(int)
stack = []

for i in nums:
    cnt[i]+=1

for i in range(n):
    num = nums[i]
    flag=True
    while(stack):
        if cnt[stack[-1]] > cnt[num]:
            result.append(stack[-1])
            stack.append(num)
            flag=False
            break

        stack.pop()

    if flag:
        result.append(-1)
        stack.append(num)

result = result[::-1]

print(*result)





