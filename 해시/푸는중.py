from collections import Counter

def solution(participant, completion):
    #해시 이용
    #Collections 모듈의 Counter 사용(해시 개념임)
    
    answer = ''
    #리스트 2개를 합친다
    all = participant + completion
    #counter를 이용해 각 원소가 몇번 나오는지 정리
    counter_hash = Counter(all)
    #1번 나오는 원소의 키값 리턴
    answer = find_index(counter_hash, 1)
    https://bluemumin.github.io/python/2021/01/24/Python-Counter%EC%97%90%EC%84%9C-index-%EA%B3%A8%EB%9D%BC%EB%82%B4%EB%8A%94-%EB%B0%A9%EB%B2%95/
    return answer
