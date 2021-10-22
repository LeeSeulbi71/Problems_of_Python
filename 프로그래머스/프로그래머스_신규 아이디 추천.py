def solution (new_id):
    #1단계
    new_id = new_id.lower()

    #2단계
    character = "~!@#$%^&*()=+[{]}:?,<>/"
    for j in range(len(character)):
        new_id = new_id.replace(character[j],"")

    #3단계
    new_id = list(new_id)
    # list를 만드는 방법은 두 가지만 형태가 다름
    # list()는 하나씩 끊어서 만듦
    # []는 한 덩어리
    recommanded_id = []
    for i in range(len(new_id)):
        if new_id[i] == '.':
            if new_id[i-1] !='.':
                recommanded_id += new_id[i]
        else:
            recommanded_id += new_id[i]

    #4단계
    if recommanded_id != []:
        if (recommanded_id[0]) == '.':
            recommanded_id.remove('.')
        elif (recommanded_id[-1]) == '.':
            recommanded_id.remove('.')

    #5단계
    if recommanded_id == []:
        recommanded_id.append('a')

    #6단계
    if len(recommanded_id) >= 16:
        recommanded_id = recommanded_id[:15]
    if (recommanded_id[-1]) == '.':
            recommanded_id.remove('.')

    #7단계
    if len(recommanded_id) <= 2:
        while len(recommanded_id) <= 2:
            recommanded_id.append(recommanded_id[-1])

    #8단계
    recommanded_id = "".join(recommanded_id)

    return recommanded_id

print(solution("z-+.^."))