mod=1000000
nums = [0]+ list(map(int, list(input())))
dp=[0]*(len(nums))

flag=False
for idx, i in enumerate(nums):

  if idx==0 or (idx==1 and i!=0):
    dp[idx]=1
    continue
  
  if (i==0 and nums[idx-1] not in [1,2]):
    flag=True
    break

  if i==0:
    dp[idx]= dp[idx-2]
  elif (nums[idx-1]==1 and i>=1) or (i<=6 and nums[idx-1] ==2):
    dp[idx]= (dp[idx-2] + dp[idx-1])%mod
  else:
    dp[idx] = dp[idx-1]

#print(dp) 
if flag:
  print(0)
else:
  print(dp[len(nums)-1])