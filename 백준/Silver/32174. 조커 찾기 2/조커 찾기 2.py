import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip('\n')

#덱에서 조커의 위치
n,m= map(int, input().split())
turn = defaultdict(int)
turn[0] = 1

def func(op, k, i):
    if(op==1):
        return (k+i)%n
    if(op==2):
        if(k-i<=0):
            return n-(abs(k-i)%n)
        return (k-i)
    if(op==3):
        return turn[i]

for i in range(1, m+1):
    op, j= map(int, input().split())
    turn[i] = func(op, turn[i-1], j)
    #print(turn[i])

print(turn[m])