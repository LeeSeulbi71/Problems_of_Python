with open('lec12-i-have-a-dream (1).txt', 'r') as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break
        if line == '\n':
            continue
        else:
            print(str(i) + ' === ' +  line.replace('\n', '').strip())
        i += 1