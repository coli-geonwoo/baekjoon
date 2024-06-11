#9659. 돌게임 5

#1개 혹은 3개 가져갈 수 있음

n= int(input())

if n%4 in [1,3]:
  print("SK")
elif n%4 in [0,2]:
  print("CY")
