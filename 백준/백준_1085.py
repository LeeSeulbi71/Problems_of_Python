#직사각형에서 탈출

import math

x, y, w, h = map(int, input().split())

if w-x > x:
    go_w = x
else:
    go_w = w-x

if h-y > y:
    go_h = y
else:
    go_h = h-y

print(min(go_h, go_w))
