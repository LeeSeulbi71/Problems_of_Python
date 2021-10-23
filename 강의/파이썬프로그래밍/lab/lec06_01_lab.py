# Yesterday 라는 노래에는 Yesterday라는 말이 몇 번 나올까?

f = open("lec06-3-yesterday.txt", 'r')
yesterday_lyric = ""
while 1:
    line = f.readline() 

    #readlines()는 전체를 불러와서 리스트 형태로 저장
    #\n까지 포함해서!
    
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
    if not line:
        break
f.close()
n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
print("Number of a Word 'yesterday' = ", n_of_yesterday)
