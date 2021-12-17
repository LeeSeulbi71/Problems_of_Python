f = open('count_log', 'w', encoding='utf8')
for i in range(10):
    data = '%d번째 줄입니다. \n' % (i+1)
    f.write(data)
f.close()