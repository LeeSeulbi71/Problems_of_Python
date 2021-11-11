# 그릇

bowl = list(input())
height = 10

for shape in range(1,len(bowl)):
    if bowl[shape-1] == '(':
        if bowl[shape] == '(':
            height += 5
        else: 
            height += 10
    else:
        if bowl[shape] == '(':
            height += 10
        else: 
            height += 5

print(height)