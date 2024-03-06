#16112. 5차 전직(실2)

n,k = map(int, input().split())

nums= list(map(int, input().split()))
nums.sort()

reward=[]
result=0

for i in nums:
  result+= min(len(reward),k)*i
  reward.append(i)

print(result)