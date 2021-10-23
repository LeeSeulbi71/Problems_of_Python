# 대소문자를 구분하여 Yesterday와 yesterday의 개수를 나눠서 세는 프로그램

f = open("lec06-3-yesterday.txt", 'r')
yesterday_lyric = ""
while 1:
    line = f.readline()
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
    if not line:
        break
f.close()

n_of_yesterday_including_upper = yesterday_lyric.count("Yesterday")
n_of_yesterday_including_lower = yesterday_lyric.count("yesterday")
print("The Number of a Word 'Yesterday' = ", n_of_yesterday_including_upper)
print("The Number of a Word 'yesterday' = ", n_of_yesterday_including_lower)
