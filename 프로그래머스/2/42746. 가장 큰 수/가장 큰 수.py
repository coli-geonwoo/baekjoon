from functools import cmp_to_key

'''
def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x: x*4, reverse=True)
    return str(int(''.join(numbers)))
'''

def compare(x,y):
    if(str(x)+str(y)<=str(y)+str(x)):
        return 1
    else:
        return -1

def solution(numbers):
    numbers=[str(i) for i in numbers]
    numbers.sort(key=cmp_to_key(compare))
    return str(int(''.join(numbers)))
    