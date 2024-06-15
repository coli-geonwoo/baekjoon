n,a,b = map(int, input().split())

data = [["."]*n for _ in range(n)]

answer1 = []
answer2 = []

for i in range(n):
  if i%2==0:
    answer1.append("v."*(n//2) + "v"*(n%2))
    answer2.append(".v"*(n//2) + "."*(n%2))
  else:
    answer2.append("v."*(n//2) + "v"*(n%2))
    answer1.append(".v"*(n//2) + "."*(n%2))

if answer1[a-1][b-1]=="v":
  print(*answer1, sep="\n")
else:
  print(*answer2, sep="\n")

