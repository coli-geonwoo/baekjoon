
def canWatch(times, check_cnt):
    n= len(times)
    p=0
    cnt=0
    temp=0
    
    while(p<n):
      #k개 모두 볼 수 있을 때
      if(p+k<n and times[p]+temp<=m):
        cnt+=k
        temp+=times[p]
        p+=k
        continue
    
      #시간이 넘을 때
      if(p+k<n and times[p]+temp >m):
        p+=1
        continue
    
      #포인터가 밖으로 나갈때
      if(p+k>=n and times[p]+temp<=m):
        cnt+= n-p
        temp+=times[p]
        break
    
      if(p+k>=n and times[p]+temp>m):
        p+=1
        continue
    
    if(cnt >= check_cnt):
      return True

    return False


n,m,k= map(int, input().split())
times = list(map(int, input().split()))

times.sort(reverse=True)

left=0
right = n
result=0
while(left<=right):
  mid = (left+right)//2
  if(canWatch(times[-mid:], mid)):
    left= mid+1
    result = mid
  else:
    right = mid-1

print(result)
                 