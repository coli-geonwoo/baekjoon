#9440. 숫자 더하기(실2)

# 숫자들을 활용해 만든 두 숫자를 더해 만든 가장 작은 수
while(1):
    number = list(map(int, input().split()))
    
    if(len(number))==1:
      break
    
    number= number[1:]  
    num1=[]
    num2=[]

    number.sort()
    zero_cnt=0
    flag=True

    for i in number:
      if(i==0):
        zero_cnt+=1
        continue

      if(flag):
        num1.append(str(i))
      else:
        num2.append(str(i))
      flag = not flag
    
    
    for i in range(zero_cnt):
      if(flag):
        num1.insert(1,"0")
      else:
        num2.insert(1,"0")
      flag= not flag

    result = int("".join(num1))+ int("".join(num2))

    print(result)