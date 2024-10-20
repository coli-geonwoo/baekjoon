import sys
input = lambda: sys.stdin.readline().strip('\n')
n= int(input())
answer = [0]*(n+2)
answer[1]=1

result = []

for i in range(n):
    op, start, end =  map(int, input().split())

    if op==1:
        if answer[end] -answer[start-1] == end-(start-1):
            answer[i+2]=answer[i+1]+1
            result.append("Yes")
        else:
            answer[i+2]=answer[i+1]
            result.append("No")
    else:
        if answer[end] -answer[start-1] == 0:
            answer[i + 2] = answer[i + 1] + 1
            result.append("Yes")
        else:
            answer[i+2]=answer[i+1]
            result.append("No")


print(*result, sep="\n")



