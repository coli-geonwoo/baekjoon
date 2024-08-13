#1935. 후위 표기식2

n= int(input())
sen = list(input())
nums = [int(input()) for _ in range(n)]
q=[]


for i in sen:
  if i>="A" and i<="Z":
    q.append(nums[ord(i)-ord("A")])
  else:
    a= str(q.pop())
    b= str(q.pop())
    q.append(eval(b+i+a))

print(format(q[0], ".2f"))

