def solution(array, commands):
    answer = []
    for i in commands: #commands의 for문을 돌고 있으므로
        for j in i: #해당 내용은 없어도 됨
            aws = array[i[0]-1:i[1]] # i는 commands[0]과 같다 commands[0][0]을 해당
            aws.sort()
        answer.append(aws[i[2]-1])
    return answer

#실수했던 내용
def solution(array, commands):
    answer = []
    for i in commands:
        for j in i:
            aws = array[commands[i][0]-1:commands[i][1]] #commands의 for문을 돌고 있는데 예시로 연습하고 commands를 떼지 못함 
            aws.sort()
            answer.append(aws[commands[i][2]-1])
    return answer
