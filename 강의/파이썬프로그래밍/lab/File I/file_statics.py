from io import SEEK_CUR


with open('lec12-i-have-a-dream (1).txt', 'r') as my_file:
    contents = my_file.read()
    sentences = contents.split('\n')
    word = contents.split(' ')

    print(len(contents), len(sentences), len(word))