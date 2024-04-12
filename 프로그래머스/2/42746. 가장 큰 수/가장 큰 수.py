
def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x: x*4, reverse=True)
    return str(int(''.join(numbers)))

    