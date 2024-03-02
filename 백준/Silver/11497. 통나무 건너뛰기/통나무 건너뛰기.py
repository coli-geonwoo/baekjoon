from collections import deque

t= int(input())

for _ in range(t):
  tree_number= int(input())
  tree_heights = list(map(int, input().split())) #통나무 높이들을 받아옴
  tree_heights.sort(reverse=True)
  q= deque()

  for idx, i in enumerate(tree_heights):
    if idx%2==0:
      q.appendleft(i)
    else:
      q.append(i)
  #print(q)
  max_num=abs(q[-1]- q[0])
  for i in range(0, tree_number-1):
    max_num= max(max_num, abs(q[i+1]- q[i]))
  
  print(max_num)