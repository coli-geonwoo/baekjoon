from collections import defaultdict
def solution(participant, completion):
    cnt1 = defaultdict(int)
    cnt2= defaultdict(int)
    for i in range(len(participant)):
        if i== len(participant)-1:
            cnt1[participant[i]]+=1
            continue
        cnt1[participant[i]]+=1
        cnt2[completion[i]]+=1
    
    for j in cnt1.keys():
        if cnt1[j]!=cnt2[j]:
            return j
    
    