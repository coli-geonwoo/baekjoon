#17487. 타자연습

left= ["q","w","e","r","t","y","a","s","d","f","g", "z","x","c","v","b"]

s= list(input())

l_cnt, r_cnt= 0,0
cnt=0

for i in s:
  if i==" ":
    cnt+=1
    continue

  if i.isupper():
    cnt+=1

  if i.lower() in left:
    l_cnt+=1
  else:
    r_cnt+=1

while(cnt!=0):
  if l_cnt <=r_cnt:
    l_cnt+=1
    cnt-=1
  else:
    r_cnt+=1
    cnt-=1

print(l_cnt, r_cnt)