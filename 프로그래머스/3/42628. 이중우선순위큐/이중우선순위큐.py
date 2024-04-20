import heapq

def solution(operations):
    max_heapq = []
    min_heapq = []
    
    for i in operations:
        op, num = i.split()
        num = int(num)
        
        if op=="D" and num==1:
            if len(max_heapq)==0:
                continue
            k= heapq.heappop(max_heapq)
            min_heapq.remove(-k)
        elif op=="D" and num==-1:
            if len(min_heapq)==0:
                continue
            k= heapq.heappop(min_heapq)
            max_heapq.remove(-k)
        else:
            heapq.heappush(max_heapq, -num)
            heapq.heappush(min_heapq, num)
    
    if len(min_heapq)<1:
        return [0,0]
    else:
        return [-heapq.heappop(max_heapq), heapq.heappop(min_heapq)]
        
    
