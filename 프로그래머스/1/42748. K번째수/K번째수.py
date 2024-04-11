def solution(array, commands):
    answer = []
    for command in commands:
        k=sorted(array[command[0]-1: command[1]])
        answer.append(k[command[2]-1])
    return answer