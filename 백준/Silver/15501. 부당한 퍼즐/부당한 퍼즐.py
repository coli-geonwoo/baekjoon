#15501. 부당한 퍼즐(실2)

#두개의 파트로 나뉘어져야 함

n= int(input())
flag=True
answer = list(map(int, input().split()))
answer2 = answer[::-1]
nums = list(map(int, input().split()))
 
if n!=1:
  n1 = nums[nums.index(answer[0]):] + nums[:nums.index(answer[0])]
  n2 = nums[nums.index(answer[-1]):] + nums[: nums.index(answer[-1])]
  access1=True
  access2=True
  for i in range(n):
    if access1==False and access2==False:
      flag=False
      break
    if n1[i] != answer[i]:
      access1=False
    if n2[i] != answer2[i]:
      access2=False

if flag:
  print("good puzzle")
else:
  print("bad puzzle")