from collections import defaultdict
nums= defaultdict(int)
nums['+']=1
nums['-']=1
nums['*']=0
nums['/']=0
nums['(']=-1
nums[')']=-1

stack=[]

alpha_start= ord('A')
alpha_end = ord('Z')
k = list(input())
result=""

for i in k:
  if alpha_start<=ord(i)<=alpha_end:
    result+=i
  else:
    if i=="(":
      stack.append(i)
    elif i==")":
      while(stack[-1]!="("):
        result+=stack.pop()
      stack.pop()
    else:
      while(stack and nums[stack[-1]]<=nums[i] and stack[-1]!="("):
        result+=stack.pop()
      stack.append(i)

while(stack):
  result+=stack.pop()
print(result)