# 조 짜기

# 나이 순서대로 
# 차이가 많은 조가 가장 좋음


n= int(input())
nums =  list(map(int, input().split()))

#i-j일때 최대, 최소값
nums_min= [[0]*(n+1) for _ in range(n+1)]
nums_max= [[0]*(n+1) for _ in range(n+1)]


dp=[0]*(n+1)

# i-j번째까지의 최대, 최솟값
for i in range(1,n+1):
  num= nums[i-1]
  nums_min[i][i]=num
  nums_max[i][i]= num
  for j in range(i+1,n+1):
    nums_min[i][j]= min(nums_min[i][j-1], nums[j-1])
    nums_max[i][j]= max(nums_max[i][j-1], nums[j-1])


# i번째까지의 최대값

for i in range(1,n+1):
    #포함안하는 경우
    dp[i] =dp[i-1]

    #포함 하는 경우 : 어디까지 i번째를 포함하는 조로 보는 것이 최대인가
    for k in range(1,i):
      dp[i]= max(dp[i], dp[i-k-1]+ nums_max[i-k][i] - nums_min[i-k][i])

print(dp[n])



