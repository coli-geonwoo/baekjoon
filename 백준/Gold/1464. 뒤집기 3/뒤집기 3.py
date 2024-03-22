#1464 . 뒤집기3(골4)

from collections import deque

n= [ord(i)-ord('A') for i in list(input())]
#print(n)

result=deque()

for i in n:
  if len(result)==0:
    result.append(i)
  else:
    if result[0]<i:
      result.append(i)
    else:
      result.appendleft(i)

result = [chr(i+ ord('A')) for i in result]
print(''.join(result))