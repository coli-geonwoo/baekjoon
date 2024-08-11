k = list(input())

n= len(k)

b_count = k.count("B")
ab_count = 0
bc_count =0

a_count=0
for i in k:
  if i=="A":
    a_count+=1
  elif i=="B" and a_count!=0:
    ab_count+=1
    a_count-=1

temp=0

for i in k:
  if i=="B":
    temp +=1
  if i=="C" and temp!=0:
    temp-=1
    bc_count+=1

print(min(bc_count+ab_count, b_count))
  
