def solution(num_list):
    #마지막 원소 > 그전 원소 = 마지막 - 그전
    #마지막 원소 <= 그전 원소 = 마지막 * 2
    
    answer = []
    
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    answer = num_list.copy()
    return answer