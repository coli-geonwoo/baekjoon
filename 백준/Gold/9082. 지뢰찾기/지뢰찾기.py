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
    bombs= list(input())

    result=0

    #첫번째에 폭탄이 없을 때
    for i in range(n):
      if bombs[i]=="*" or (range_check(number1, i, n)):
        result+=1
        bomb_on(number1, i, n)
        #print(number1)

    print(result)