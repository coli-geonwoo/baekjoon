def solution(n, times):
    left= 0
    right= max(times)*n
    answer=0
    while(left<=right):
        mid= (left+right)//2
        temp=sum([mid//i for i in times])
        
        #시간 줄여도 됨
        if temp>=n:
            answer=mid
            right= mid-1
        else:
            left= mid+1
    
    
    return answer