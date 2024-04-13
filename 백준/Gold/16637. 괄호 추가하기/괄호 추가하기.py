import sys

def cal(idx, temp):
  global result, n
  if n==idx:
    result= max(result, int(temp))
    return
  #괄호를 사용해야할 때
  if idx+4<=n:
    temp_bracket= str(eval(''.join([temp, exp[idx], str(eval(''.join(exp[idx+1:idx+4])))])))
    cal(idx+4, temp_bracket)
  if idx+2<=n:
    cal(idx+2, str(eval(''.join([temp]+ exp[idx:idx+2]))))

n= int(input())
exp = list(input())
result = -sys.maxsize


cal(1, exp[0])
print(result)