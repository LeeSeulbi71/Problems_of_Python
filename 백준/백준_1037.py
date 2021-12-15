#약수

#전체 sorted
#처음, 맨마지막 곱하기

N_measure = int(input())
measures = list(map(int, input().split()))
sorted_measures = sorted(measures, reverse=False)
print(sorted_measures[0]*sorted_measures[-1])