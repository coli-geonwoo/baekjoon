n= int(input())
number= list(map(int, input().split()))
max_num=0
min_num=number[0]
temp=0

result=[]

for i in number:
  
  #가장 작은 수가 들어왔을 때 -> min_num 갱신
  if i<=min_num:
    min_num= min(i, min_num)
  elif i>=max_num:
    max_num=i
    temp= max_num-min_num
  #중간 수가 들어왔을 때 -> 사이값 갱신
  else:
    temp= max(temp, i-min_num)
  result.append(temp)
  #print(i, min_num, max_num)

print(*result)