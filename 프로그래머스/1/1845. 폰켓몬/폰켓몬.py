def solution(nums):
    n= len(nums)
    k=set(nums)
    answer = min(len(k), n//2)
    return answer