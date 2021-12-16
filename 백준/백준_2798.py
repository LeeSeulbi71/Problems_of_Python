#블랙잭

cards, M = map(int, input().split())

all_cards = []
Ns = []
all_cards = list(map(int, input().split()))

for first in range(cards):
    for second in range(first+1, cards):
        for third in range(second+1, cards):
            N = all_cards[first] + all_cards[second] + all_cards[third]
            if N <= M:
                Ns.append(N)

print(max(Ns))
                