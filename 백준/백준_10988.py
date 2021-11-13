#팰린드롬인지 확인하기

word = list(input())
word_reversed = reversed(word)  

word_ = "".join(word)
word_reversed_ = "".join(word_reversed)


if word_ == word_reversed_:
    print(1)
else:
    print(0)

#어짜피 reversed는 list로 만들어지기 때문에
#reversed만 join 해줘도 됨!