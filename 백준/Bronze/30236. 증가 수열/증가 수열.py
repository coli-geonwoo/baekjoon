
def make_good_sequence(n, a_sequence):
  temp = [0]+[i for i in range(1, n+1)]
  before=a_sequence[0]

  for i in range(1, n+1):
    while(True):
      if a_sequence[i]!=temp[i] and temp[i-1]<temp[i]:
        break
      temp[i]+=1
  
  return temp

for _ in range(int(input())):
  n= int(input())
  a= [0]+list(map(int, input().split()))
  temp = make_good_sequence(n, a)
  print(temp[n])
