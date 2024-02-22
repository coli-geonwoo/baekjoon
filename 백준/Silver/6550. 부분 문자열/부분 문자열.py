while(True):
  try:
    s,t= map(str, input().split())
    flag1=True
    flag2=True
    current_idx=-1

    #부분문자열의 길이가 더 길때
    if len(t)<len(s):
      flag1=False
    else:
      idx=[]

      for j in s:
        current_idx=t.find(j, current_idx+1)
        if current_idx ==-1:
          flag2=False
          break
        idx.append(current_idx)

    if flag1==False or flag2==False:
      print("No")
    elif(sorted(idx)==idx):
      print("Yes")
  except:
    break
