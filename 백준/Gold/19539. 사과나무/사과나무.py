import heapq

n= int(input())

tree=list(map(int, input().split()))


if sum(tree)%3!=0:
  print('NO')
else:
  #전체 걸리는 일수
  day = sum(tree)//3
  # 2틀이상 줄 수 있는 개수>=전체 일수
  more_than_two = [i//2 for i in tree]
  if sum(more_than_two) >=day:
    print("YES")
  else:
    print("NO")
