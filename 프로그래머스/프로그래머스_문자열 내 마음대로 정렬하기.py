# ["sun", "bed", "car"]	1	["car", "bed", "sun"]
# strings[i][n]

def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
        print(strings[i])
    strings.sort()
    
    # sort 함수는 앞 인덱스부터 하나씩 크기 비교 (같으면 뒤에 걸로 비교)
    # 비교해줘야 하는 인덱스를 앞으로 가져오고
    # 그 뒤에 원래 string을 붙여주면 됨
    for j in range(len(strings)):
        answer.append(strings[j][1:])

    return answer

print(solution(['abce', 'abcd', 'cdx'], 1))

# 다른 사람 풀이

def strange_sort(strings, n):
    return sorted(strings, key = lambda x: x[n])

# sort에 기준을 부여하는 방법은
# lambda! key = lambda 로 기준 만들어주기 !~