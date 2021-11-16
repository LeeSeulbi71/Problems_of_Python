# 네 번째 점

x_ractangle = []
y_ractangle = []

for i in range(3):
    coordinate_x, coordinate_y = map(int, input().split())
    x_ractangle.append(coordinate_x)
    y_ractangle.append(coordinate_y)

answer_x = list(set(x_ractangle))
answer_y = list(set(y_ractangle))

print(answer_x[0], answer_y[0])