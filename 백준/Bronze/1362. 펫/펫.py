cnt=1
while(1):
    normal, weight = map(int, input().split())
    if (normal, weight) ==(0,0):
      break

    #작업 받기
    while(1):
      k, n =input().split()
      n= int(n)
      if k=="#":
        break
      if weight<=0:
        continue
    
      if k=="F":
        weight+=n
      if k=="E":
        weight-=n

      #print(weight, normal)
    if weight > normal/2 and normal*2> weight:
      print("{} :-)".format(cnt))
    elif weight<=0:
      print("{} RIP".format(cnt))
    else:
      print("{} :-(".format(cnt))
    cnt+=1
