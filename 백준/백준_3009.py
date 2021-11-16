# 네 번째 점

x_ractangle = []
y_ractangle = []

for i in range(3):
    coordinate_x, coordinate_y = map(int, input().split())
    x_ractangle.append(coordinate_x)
    y_ractangle.append(coordinate_y)

for i in range(3):
    if x_ractangle.count(x_ractangle[i]) == 1:
        x = x_ractangle[i]
    if y_ractangle.count(y_ractangle[i]) == 1:
        y = y_ractangle[i]


print(x, y)