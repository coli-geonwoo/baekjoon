n= input()

stack=[]

for i in n:
  stack.append(i)
  while(len(stack)>=4 and ''.join(stack[-4:]) =="PPAP"):
    for i in range(4):
      stack.pop()
    stack.append("P")

if len(stack)==1 and stack[0]=="P":
  print("PPAP")
else:
  print("NP")