with open('count_log', 'a', encoding='utf8') as my_file:
    for i in range(11, 21):
        data = '%d번째 줄입니다. \n' % i
        my_file.write(data)