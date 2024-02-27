n= int(input())
books= [int(input()) for _ in range(n)]

idx= books.index(max(books))

temp= books[:idx][::-1] # 최대값보다 왼쪽에 있는 친구들 중 오름차순 확인을 위해 뒤집음

cnt=n-idx-1 # 최대값보다 오른쪽에 있는 애들은 어차피 올려야 한다.

num= max(books)-1

for i in temp:
  if i==num:
    num-=1
  else:
    cnt+=1

print(cnt)
