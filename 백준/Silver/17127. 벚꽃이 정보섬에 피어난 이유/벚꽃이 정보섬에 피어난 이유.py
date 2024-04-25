#벚꽃이 정보섬에 피어난 이유

def getSum(a):
  result=1
  for i in a:
    result*=i
  return result


n = int(input())
nums= list(map(int, input().split()))
result=0
for i in range(1, n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      part1= getSum(nums[:i])
      part2= getSum(nums[i:j])
      part3= getSum(nums[j:k])
      part4= getSum(nums[k:])
      result= max(result, part1+part2+part3+part4)

print(result)