def solution(number, k):
    
    #순서 -> 숫자
    #기회가 되는 대로 작은 숫자가 오면 지움
    stack =[]
    
    for num in number:
        num = int(num)
        
        #stack에 아무것도 없거나 더이상 지울 기회가 없을 때
        if len(stack)==0 or k==0:
            stack.append(num)
        else:
            while(k!=0 and len(stack)!=0 and stack[-1]<num):
                stack.pop()
                k-=1
            stack.append(num)

    
    if k==0:
        return ''.join(map(str,stack))
    else:
        return ''.join(map(str,stack[:-k]))
