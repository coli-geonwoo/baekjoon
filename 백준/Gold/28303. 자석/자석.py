n,k= map(int, input().split())

nums = list(map(int, input().split()))

ns = [0]* (n-1)
sn = [0] * (n-1)

for i in range(1,n):
  ns[i-1] = nums[i-1]- nums[i]-k
  sn[i-1] = nums[i] - nums[i-1] -k

result_ns = [0]* (n-1)
result_sn = [0] * (n-1)

result_ns[0] = ns[0]
result_sn[0] = sn[0]

#print(ns, sn)
result=max(ns[0], sn[0])
for i in range(1,n-1):
  result_ns[i] = max(result_ns[i-1],0) + ns[i]
  result_sn[i] = max(result_sn[i-1],0) + sn[i]
  result= max(result, result_ns[i], result_sn[i])

print(result)
