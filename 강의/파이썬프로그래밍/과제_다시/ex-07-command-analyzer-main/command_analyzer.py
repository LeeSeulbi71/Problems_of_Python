
def count_unique(data):
    """CSV 파일에서 읽어들인 list 형태의 데이터를 받아
    고유한 id의 수, 고유한 command의 수를 반환하는 함수입니다.

    Input:
        data: read_csv 함수로 읽어들인 list 형태의 데이터

    Output:
        n_unique_id: 고유한 id의 수
        n_unique_command: 고유한 command의 수
    """
    #===== write your code below =======
    unique_id = set([data[i][1] for i in range(len(data))])
    unique_command = set([data[i][0] for i in range(len(data))])
    n_unique_id = len(unique_id)
    n_unique_command = len(unique_command)
    #===================================

    return n_unique_id, n_unique_command

def make_dict(data):
    """CSV 파일에서 읽어들인 list 형태의 데이터를
    dictionary 형태로 변환하여 반환하는 함수입니다.

    주의사항: 명령어들 좌우에 불필요한 공백 등을 제거해야 함 -> strip()

    Input:
        data: read_csv 함수로 읽어들인 list 형태의 데이터

    Output:
        data_dict: id를 key,
                   해당 id가 실행한 command들의 list가 value인 dict
    """
    #===== write your code below =======
    ids = list(set([data[i][1] for i in range(len(data))]))
    all_command = []
    for id in ids:
        command = []
        for i in range(len(data)): 
            if data[i][1] == id:
                command.append(data[i][0].strip())
        all_command.append(command)
    
    data_dict = {}

    for n in range(len(ids)):
        data_dict[ids[n]] = all_command[n]
    #===================================

    return data_dict

def find_ranked(data_dict, rank=1):
    """dict 형태의 데이터와 rank를 입력받아 명령어 수를 기준으로
    상위 rank 번째에 해당되는 id와 그 id가 실행한 총 명령어 수, 고유한 명령어 수를 반환합니다.

    예를 들어, rank=3 이면 세 번째로 많은 명령어를 실행시킨 id와 그 명령어의 수를 반환합니다.

    Input:
        data_dict: make_dict 함수를 통해 얻은 dict 형태의 데이터

    Output:
        target_id: 상위 rank 번째에 해당되는 id
        n_commands: target_id가 실행시킨 명령어의 수
        n_unique_commands: target_id가 실행한 고유한 명령어의 수
    """

    sorted_dict = sort_by_n_command(data_dict)

    #===== write your code below =======
    dic_to_list = list(sorted_dict.items())
    target_id = dic_to_list[rank-1][0]
    
    n_commands = len(dic_to_list[rank-1][1])

    n_unique_commands = len(set(dic_to_list[rank-1][1]))
    #===================================

    return (target_id, n_commands, n_unique_commands)

# Helper function: 이 함수는 수정하지 말 것
def sort_by_n_command(data_dict):
    """dict 형태의 데이터를 받아 각 id의 명령어 수를 기준으로
    내림차순 정렬한 OrderedDict를 반환합니다.
    """

    from collections import OrderedDict

    sorted_dict = OrderedDict(sorted(data_dict.items(),
                                     key=lambda x:len(x[1]),
                                     reverse=True))

    return sorted_dict

# Helper function: 이 함수는 수정하지 말 것
def read_csv(filename):
    """파일 이름을 입력받아 list 형태로 데이터를 반환합니다.
    """

    import csv

    command_data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            command_data.append(row)

    # 첫 줄 (header) 을 제거하고 반환
    return command_data[1:]

if __name__ == "__main__":
    # 구현한 함수들을 아래에서 확인해보세요.

    filename = 'command-data.csv'
    data = read_csv(filename)

    # Correct answer: n_unique_id = 115, n_unique_command = 4245
    n_unique_id, n_unique_command = count_unique(data)
    print(n_unique_id, n_unique_command)
    data_dict = make_dict(data)

    # Correct answer: ('elsa', 7500, 78)
    res = find_ranked(data_dict, rank=2)
    print(res)