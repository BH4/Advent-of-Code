card_dict = dict()
card_dict['T'] = 10
card_dict['J'] = 11
card_dict['Q'] = 12
card_dict['K'] = 13
card_dict['A'] = 14
for i in range(2, 10):
    card_dict[str(i)] = i




class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.type = self.read(hand)

    def read(self, hand):
        cards = set([x for x in hand])
        num = len(set([x for x in hand]))
        if num == 1:
            return 6

        count = sorted([hand.count(c) for c in cards])

        if num == 2 and count == [1, 4]:
            return 5

        if num == 2 and count == [2, 3]:
            return 4

        if 3 in count:
            return 3

        if 2 in count and count.count(2) == 2:
            return 2

        if 2 in count:
            return 1

        return 0

    def __eq__(self, other):
        return self.hand == other.hand

    def __gt__(self, other):
        if self.type > other.type:
            return True

        if self.type < other.type:
            return False

        for i in range(5):
            a = card_dict[self.hand[i]]
            b = card_dict[other.hand[i]]

            if a > b:
                return True

            if a < b:
                return False

        return False




with open('input/input7.txt') as f:
    hands = []
    for line in f:
        line = line.strip()
        hand, bid = line.split()
        hands.append((Hand(hand), int(bid)))


hands = sorted(hands)

tot = 0
rank = 1
for h, bid in hands:
    tot += bid*rank

    rank += 1

print(tot)




# Just redo everything for second part
card_dict = dict()
card_dict['T'] = 10
card_dict['J'] = 1
card_dict['Q'] = 12
card_dict['K'] = 13
card_dict['A'] = 14
for i in range(2, 10):
    card_dict[str(i)] = i




class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.type = self.read(hand)

    def read(self, hand):
        cards = set([x for x in hand])
        if 'J' in cards:
            nj = hand.count('J')
            if nj == 5:
                return 6

            most = None
            num = 0
            for c in cards:
                n = hand.count(c)
                if n > num and c != 'J':
                    num = n
                    most = c
            hand = hand.replace('J', most)
            cards = set([x for x in hand])

        num = len(set([x for x in hand]))

        if num == 1:
            return 6

        count = sorted([hand.count(c) for c in cards])

        if num == 2 and count == [1, 4]:
            return 5

        if num == 2 and count == [2, 3]:
            return 4

        if 3 in count:
            return 3

        if 2 in count and count.count(2) == 2:
            return 2

        if 2 in count:
            return 1

        return 0

    def __eq__(self, other):
        return self.hand == other.hand

    def __gt__(self, other):
        if self.type > other.type:
            return True

        if self.type < other.type:
            return False

        for i in range(5):
            a = card_dict[self.hand[i]]
            b = card_dict[other.hand[i]]

            if a > b:
                return True

            if a < b:
                return False

        return False




with open('input/input7.txt') as f:
    hands = []
    for line in f:
        line = line.strip()
        hand, bid = line.split()
        hands.append((Hand(hand), int(bid)))


hands = sorted(hands)

tot = 0
rank = 1
for h, bid in hands:
    tot += bid*rank

    rank += 1

print(tot)





