def solution(friends, gifts):
    answer = 0
    #준 횟수 2차원 배열
    give_cnt = {}
    for i in friends:
        temp = {}
        for j in friends:
            temp[j]=0
        give_cnt[i]= temp
            
    gift_score = {}
    for j in friends:
        gift_score[j]=0
    #점수 조정
    for k in gifts:
        a,b= k.split(" ")
        if a not in gift_score.keys():
            gift_score[a]=1
        else:
            gift_score[a]+=1
        if b not in gift_score.keys():
            gift_score[b]=-1
        else:
            gift_score[b]-=1
        give_cnt[a][b]+=1
    
    result = {}
    for j in friends:
        result[j]=0
    
    for i in range(len(friends)-1):
        a=friends[i]
        for j in range(i, len(friends)):
            b= friends[j]
            if give_cnt[a][b] > give_cnt[b][a]:
                result[a]+=1
            elif  give_cnt[a][b] < give_cnt[b][a]:
                result[b]+=1
            elif gift_score[a]> gift_score[b]:
                result[a]+=1
            elif gift_score[b]> gift_score[a]:
                result[b]+=1

    answer=max(result.values())
            
                       
    
        
            
    
    return answer