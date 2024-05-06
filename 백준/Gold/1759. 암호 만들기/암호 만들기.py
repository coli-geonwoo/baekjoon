#1759. 암호 만들기(골5)

from itertools import permutations, combinations
from collections import defaultdict

password_length, alphabet_nums= map(int, input().split())
m =["a", "e", "i", "o", "u"]
alphabets = list(map(str, input().split()))

mo=[]
ja=[]

for i in alphabets:
  if i in m:
    mo.append(i)
  else:
    ja.append(i)
    
#1개의 모음 + 2개의 자음
result=set()

mo_dict=defaultdict(list)
ja_dict = defaultdict(list)

for mo_num in range(1, len(mo)+1):
    ja_num= password_length-mo_num

    if ja_num<2:
      break
    
    #없으면 모음 조합 케이스 저장
    if len(mo_dict[mo_num])==0:
      mo_dict[mo_num] = list(combinations(mo, mo_num))
    mo_cases= mo_dict[mo_num]

    #없으면 자음 조합 케이스 저장
    if len(ja_dict[ja_num])==0:
      ja_dict[ja_num] = list(combinations(ja, ja_num))
    ja_cases = ja_dict[ja_num]

    for mo_case in mo_cases:
      for ja_case in ja_cases:
        result.add(''.join(sorted(mo_case+ja_case)))

result = sorted(list(result))

print(*result, sep="\n")