n= int(input())
nums = [0] + list(map(int, input().split())) + [0]
before_node =[i for i in range(n+2)]
dp = [0]*(n+2)

for i in range(1, n+2):
    for j in range(1,i):
        if(nums[j] < nums[i]) and dp[j]+1> dp[i]:
            dp[i] = dp[j]+1
            before_node[i] = j

# print(*dp)
# print(*before_node)

idx = dp.index(max(dp))

if idx==0:
    result= [nums[1]]
else:
    result=[nums[idx]]
    k = before_node[idx]
    while(True):
        if(k==before_node[k]):
            if k!=0:
                result.append(nums[k])
            break
        result.append(nums[k])
        k= before_node[k]

result = result[::-1]
print(len(result))
print(*result)