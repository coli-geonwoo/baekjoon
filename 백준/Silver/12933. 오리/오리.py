#12933. 오리(실2)
# quack이 완성되지 않았을 때

answer= "quack"

result=[]

k= list(input())

answer_flag=False
for i in k:
  idx= answer.index(i)
  flag=False
  for case_ in result:
    if i=="q" and case_[-1]=="k":
      case_.append(i)
      flag=True
      break

    if answer.index(case_[-1])+1 == idx:
      flag=True
      case_.append(i)
      break
  
  if i=="q" and flag==False:
    result.append([i])
    continue
  if flag==False:
    answer_flag=True
    break

for i in result:
  if i[-1]!="k":
    answer_flag=True
    break

if answer_flag:
  print(-1)
else:
  print(len(result))
  