#팰린드롬인지 확인하기

word = list(input())
word_reversed = reversed(word)  

word_ = "".join(word)
word_reversed_ = "".join(word_reversed)


if word_ == word_reversed_:
    print(1)
else:
    print(0)