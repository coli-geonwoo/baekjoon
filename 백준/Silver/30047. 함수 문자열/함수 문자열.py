stack=[]

command = list(input())
command = command[::-1]
flag=True
for c in command:
  if c=="x":
    stack.append(0)
  if c=="g":
    if len(stack)==0:
      flag=False
      break
    stack[-1]+=1
  if c=="f":
    if len(stack)<2:
      flag=False
      break
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(min(n1, n2))

if len(stack)!=1:
  flag=False

if flag:
  print(stack[0])
else:
  print(-1)

