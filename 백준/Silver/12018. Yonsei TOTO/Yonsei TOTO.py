n, score = map(int, input().split())

min_score=[]

for _ in range(n):
    people_num, max_number = map(int, input().split())
    p= list(map(int, input().split()))
    p.sort()
    if people_num>max_number:
      min_score.append(p[-max_number])
    else:
      min_score.append(1)

min_score.sort()
result=0

for i in range(n):
  score-= min_score[i]
  if score>=0:
    result+=1
  else:
    break

print(result)
