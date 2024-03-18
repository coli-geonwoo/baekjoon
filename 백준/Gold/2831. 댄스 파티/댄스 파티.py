from bisect import bisect_left, bisect_right

# 자신보다 키가 큰 여자
# 자신보다 키가 작은 유형
# 키가 같은 사람들끼리는 아님

# 양수 -> 키가 큰 여자와 추고 싶음
# 음수 -> 키가 작은 여자와 추고 싶음

# 키가 작은 남자를 찾아 

# 양수 -> 키가 큰 남자와 추고 싶음
# 음수 -> 키가 작은 남자와 추고 싶음

n= int(input())
man= list(map(int, input().split()))
woman = list(map(int, input().split()))

woman_prefer_small = [-i for i in woman if i<0]
woman_prefer_big = [i for i in woman if i>0]
woman_prefer_small.sort()
woman_prefer_big.sort()

cnt=0

for i in man:
  #키가 작은 여자를 선호할 때
  if i<0:
    idx = bisect_left(woman_prefer_big, -i)
    if idx==0:
      continue
    cnt+=1
    #print(idx)
    woman_prefer_big.remove(woman_prefer_big[idx-1])
  #키가 큰 여자를 선호할 때
  else:
    idx = bisect_right(woman_prefer_small, i)
    if idx==len(woman_prefer_small):
      continue
    cnt+=1
    #print(idx)
    woman_prefer_small.remove(woman_prefer_small[idx])

print(cnt)
