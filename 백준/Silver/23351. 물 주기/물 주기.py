n,k,a,b= map(int, input().split())

planet = [k]*n
day=0
while(0 not in planet):
  planet.sort()
  for i in range(a):
    planet[i]+=b
  planet = [i-1 for i in planet]
  day+=1

print(day)