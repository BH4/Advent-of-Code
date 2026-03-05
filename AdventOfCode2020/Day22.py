decks = [[], []]
with open('input/input22.txt') as f:
    player = 0
    for line in f:
        line = line.strip()
        if len(line) > 0:
            if line[0] != 'P':
                decks[player].append(int(line))
        else:
            player += 1


def combat(deck1, deck2):

    while len(deck1) != 0 and len(deck2) != 0:
        a = deck1.pop(0)
        b = deck2.pop(0)

        if a > b:
            deck1.append(a)
            deck1.append(b)
        elif b > a:
            deck2.append(b)
            deck2.append(a)
        else:
            # No rules for ties
            print('oops')

    return deck1, deck2


def score(deck):
    deck = deck[::-1]
    s = sum([(i+1)*deck[i] for i in range(len(deck))])
    deck = deck[::-1]
    return s


result = combat(decks[0][:], decks[1][:])
winner = result[0] if len(result[0]) > 0 else result[1]
print(score(winner))


def recursive_combat(deck1, deck2):
    # returns boolian and final two decks
    # True if deck1 wins, False if deck2 wins.
    states = set()
    while len(deck1) != 0 and len(deck2) != 0:
        state = str(deck1)+str(deck2)
        if state in states:
            return True, deck1, deck2
        states.add(state)
        a = deck1.pop(0)
        b = deck2.pop(0)
        if len(deck1) < a or len(deck2) < b:
            if a > b:
                deck1.append(a)
                deck1.append(b)
            elif b > a:
                deck2.append(b)
                deck2.append(a)
            else:
                print('oops')
        else:
            # slicing always copies lists.
            w, d1, d2 = recursive_combat(deck1[:a], deck2[:b])

            if w:
                deck1.append(a)
                deck1.append(b)
            else:
                deck2.append(b)
                deck2.append(a)

    won = True
    if len(deck1) == 0:
        won = False
    return won, deck1, deck2


won, deck1, deck2 = recursive_combat(decks[0][:], decks[1][:])
if won:
    print(score(deck1))
else:
    print(score(deck2))
