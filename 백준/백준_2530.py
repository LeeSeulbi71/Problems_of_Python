#인공지능 시계

H, M, S = map(int, input().split())
taken_time = int(input())

H += taken_time // 3600
M += taken_time % 3600 // 60
S += taken_time % 3600 % 60

if S >= 60:
    S -= 60
    M += 1
if M >= 60:
    M -= 60
    H += 1
if H >= 24:
    H -= 24

print(H, M, S)
