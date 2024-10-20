from collections import deque

cat_num, weight= map(int, input().split())
cat_weights= deque(sorted(list(map(int, input().split()))))
result=0

#2개 이하로 남을 때까지 양 끝을 매칭
while(len(cat_weights)>=2):
  if(cat_weights[0]+cat_weights[-1]<=weight):
    cat_weights.pop()
    cat_weights.popleft()
    result+=1
  else:
    cat_weights.pop()

print(result)