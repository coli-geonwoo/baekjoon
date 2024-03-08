#30 
# 남자와 여자의 수는 거의 비슷해야 한다
# 차이가 더이상 크면 안됨
# 사람의 수의 최대값


max_remember= int(input())

gender=(list(input()))
gender.reverse()

women_cnt=0
man_cnt=0
flag=False
while(gender):
  #여자가 더 적을 때
  if women_cnt<man_cnt:
    if(len(gender)>1 and gender[-1]=="M"):
      gender[-1], gender[-2] = gender[-2], gender[-1]
    
    if(gender.pop()=="M"):
      man_cnt+=1
    else:
      women_cnt+=1
  else:
    if(len(gender)>1 and gender[-1]=="W"):
      gender[-1], gender[-2] = gender[-2], gender[-1]
    
    if(gender.pop()=="M"):
      man_cnt+=1
    else:
      women_cnt+=1
  
  if(abs(women_cnt-man_cnt) >max_remember):
    flag=True
    break
  
if flag:
  print(women_cnt+man_cnt-1)
else:
  print(women_cnt+man_cnt)
