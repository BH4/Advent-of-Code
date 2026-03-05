class tile:
    def __init__(self, label, s):
        self.image = s
        self.label = label

        self.edges = []
        self.get_edges()

    def get_edges(self):
        top = self.image[0]
        bottom = self.image[-1]
        left = ''.join([x[0] for x in self.image])
        right = ''.join([x[-1] for x in self.image])

        # Must keep this order!!
        self.edges = [top, right, bottom, left]

    def rotate_right(self):
        new_image = []
        for i in range(len(self.image[0])):
            row = ''.join([x[i] for x in self.image])
            new_image.append(row[::-1])
        self.image = new_image
        self.get_edges()

    def flip_over_verticle(self):
        new_image = [x[::-1] for x in self.image]
        self.image = new_image
        self.get_edges()

    def flip_over_horizontal(self):
        new_image = self.image[::-1]
        self.image = new_image
        self.get_edges()

    def get_edge_matches(self, other):
        e1 = self.edges
        e2 = other.edges
        matches = []
        for i in range(1, len(e1)+1):
            s = e1[i-1]
            if s in e2:
                matches.append((i, e2.index(s)+1))
            if s[::-1] in e2:
                matches.append((-i, e2.index(s[::-1])+1))
        return matches

    def rotate_flip_other_to_match(self, other):
        # self and other share one side. Flip other such that it could be
        # directly combined onto self.

        match = self.get_edge_matches(other)[0]
        sides = (abs(match[0]), match[1])
        while (sides[0]+2) % 4 != sides[1] % 4:
            other.rotate_right()
            match = self.get_edge_matches(other)[0]
            sides = (abs(match[0]), match[1])
        if match[0] < 0:
            if match[0] % 2 == 1:
                other.flip_over_verticle()
            else:
                other.flip_over_horizontal()

        # return other's direction relative to self
        return abs(match[0])

    def view(self):
        for i in self.image:
            print(i)
        print('')

    def view_together(self, other):
        for i in range(len(self.image)):
            print(self.image[i]+' '+other.image[i])
        print('')


all_tiles = dict()
with open('input/input20.txt') as f:
    curr_tile = []
    for line in f:
        line = line.strip()
        if 'Tile' in line:
            label = line[5:-1]
        elif len(line) > 0:
            curr_tile.append(line)
        else:
            all_tiles[label] = tile(label, curr_tile)
            curr_tile = []


# Rotating this allows it to start as a top left corner.
all_tiles['1709'].rotate_right()

prod = 1
match_dict = dict()
for i, ti in all_tiles.items():
    matches = []
    for j, tj in all_tiles.items():
        if i != j:
            edges = ti.get_edge_matches(tj)
            if len(edges) > 0:
                matches.append(j)
                assert len(edges) == 1

    if len(matches) == 2:
        # print(i, matches)
        prod *= int(i)
    match_dict[i] = matches

print(prod)


image_ids = [[0]*12 for i in range(12)]
image_ids[0][0] = '1709'
queue = [(0, 0, '1709')]
fixed = set(['1709'])
while len(queue) > 0:
    i, j, curr = queue.pop(0)
    for m in match_dict[curr]:
        if m not in fixed:
            d = all_tiles[curr].rotate_flip_other_to_match(all_tiles[m])
            fixed.add(m)

            if d == 2:
                p = (i, j+1, m)
                image_ids[i][j+1] = m
            elif d == 3:
                p = (i+1, j, m)
                image_ids[i+1][j] = m

            queue.append(p)


final_image = []
for tile_row in image_ids:
    for i in range(len(all_tiles[tile_row[0]].image)-2):
        row = ''.join([all_tiles[label].image[i+1][1:-1] for label in tile_row])
        final_image.append(row)


# Correct image orientation
final_tile = tile('final', final_image)
final_tile.flip_over_verticle()
final_image = final_tile.image

sea_monster = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']
sea_monster_signal = []
for i in range(len(sea_monster)):
    for j in range(len(sea_monster[0])):
        if sea_monster[i][j] == '#':
            sea_monster_signal.append((i, j))


def check_for_signal(array):
    for pos in sea_monster_signal:
        if array[pos[0]][pos[1]] != '#':
            return False
    return True


count = 0
for i in range(len(final_image)-2):
    for j in range(len(final_image[0])-19):
        curr = final_image[i:i+3]
        curr = [x[j:j+20] for x in curr]

        if check_for_signal(curr):
            count += 1
            for pos in sea_monster_signal:
                s = final_image[i+pos[0]]
                # I checked there were no overlapping monsters so lets remove them.
                final_image[i+pos[0]] = s[:j+pos[1]]+'%'+s[j+pos[1]+1:]

#print(count)

# Final answer is the number of # left
print(sum([x.count('#') for x in final_image]))
