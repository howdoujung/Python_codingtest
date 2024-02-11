def solution(nums):
    #해시 이용
    #dictionary: 키값이 중복될 수 없다(key-value)
    
    #key값으로 만들어주는 작업
    num_len = len(nums)
    change_key = dict.fromkeys(nums)
    #해시 상태를 리스트로 변환하는 작업 후 길이 반환
    answer = len(list(change_key))
    
    #조건1: n/2만큼 선택할 수 있음
    if (num_len/2) < answer:
        return (num_len/2)
    
    return answer
