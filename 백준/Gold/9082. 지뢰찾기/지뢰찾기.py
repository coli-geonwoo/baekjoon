import copy

def bomb_on(bomb, i, n):
  for j in [i-1, i, i+1]:
      if j>=0 and j<n:
        bomb[j]-=1


def range_check(bomb, i, n):
  if i==0:
    if bomb[i]>0 and bomb[i+1]>0:
      return True
  elif i==n-1:
    if bomb[i]>0 and bomb[i-1]>0:
      return True
  else:
    if bomb[i]>0 and bomb[i-1]>0 and bomb[i+1]>0:
      return True

for _ in range(int(input())):
    n= int(input())

    number1=list(map(int, list(input())))
    number2= copy.deepcopy(number1)
    bombs= list(input())

    result1=0
    result2=1

    if n==1:
      print(number1[0])
      continue

    #첫번째에 폭탄이 없을 때
    for i in range(1, n):
      if bombs[i]=="*" or (range_check(number1, i,n)):
        result1+=1
        bomb_on(number1, i, n)
        #print(number1)

    bomb_on(number2, 0, n)
    for i in range(1, n):
        if bombs[i]=="*" or (range_check(number2, i,n)):
          result2+=1
          bomb_on(number2, i, n)
          #print(number2)


    flag1=False
    flag2=False

    number1 = list(set(number1))
    number2 = list(set(number2))

    if len(number1)==1 and number1[0]==0:
      flag1=True
    if len(number2)==1 and number2[0]==0:
      flag2=True

    if flag1==True and flag2==True:
      print(max(result1, result2))
    elif flag1==True:
      print(result1)
    else:
      print(result2)
