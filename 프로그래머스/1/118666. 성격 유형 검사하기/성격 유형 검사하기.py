from collections import defaultdict

def solution(survey, choices):
    answer = ["RT", "CF", "JM", "AN"]
    score=defaultdict(int)
    
    for i in range(len(survey)):
        negative= survey[i][0]
        positive= survey[i][1]
        
        if choices[i]>4:
            score[positive]+= abs(4-choices[i])
        else:
            score[negative]+=abs(4-choices[i])
    
    result=''
    for i in range(4):
        if score[answer[i][0]] == score[answer[i][1]]:
            result+=answer[i][0]
        elif score[answer[i][0]] > score[answer[i][1]]:
            result+=answer[i][0]
        else:
            result+=answer[i][1]
        
    return result