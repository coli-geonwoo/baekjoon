for _ in range(int(input())):
    string1 = input()
    n= len(string1)
    left=0
    right= n-1
    flag=0

    while(left<right):
      if string1[left]==string1[right]:
        left+=1
        right-=1
      else:
        if left+1<=right:
          temp = string1[:left]+string1[left+1:]
          if temp[:]==temp[::-1]:
            flag=1
            break
        if left <= right-1:
          temp = string1[:right]+ string1[right+1:]
          if temp[:]==temp[::-1] :
            flag=1
            break
        flag=2
        break
    
    print(flag)