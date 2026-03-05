import os
from intcode_computer import run

with open('input/input13.txt', 'r') as f:
    line = f.readline()

code = [int(x) for x in line.split(',')]

copy = [x for x in code]
state, out = run(copy, [])


tot_blocks = 0
for i in range(len(out)//3):
    if out[3*i+2] == 2:
        tot_blocks += 1

print(tot_blocks)


# Part 2

def update_board(out, board, ball_pos, paddle_pos):
    score = 0
    tiles = dict()
    for i in range(len(out)//3):
        x = out[3*i]
        y = out[3*i+1]
        tileid = out[3*i+2]

        if x == -1 and y == 0:
            score = tileid
        else:
            tiles[(x, y)] = tileid

    for x, y in tiles.keys():
        tid = tiles[(x, y)]

        if tid == 4:
            board[y] = board[y][:x]+'o'+board[y][x+1:]
            ball_pos = (x, y)
        elif tid == 1:
            board[y] = board[y][:x]+'W'+board[y][x+1:]
        elif tid == 2:
            board[y] = board[y][:x]+'-'+board[y][x+1:]
        elif tid == 3:
            board[y] = board[y][:x]+'_'+board[y][x+1:]
            paddle_pos = (x, y)
        else:
            board[y] = board[y][:x]+' '+board[y][x+1:]

    return board, score, ball_pos, paddle_pos


copy = [x for x in code]
copy[0] = 2

stdin = []
curr = 0
relative_base = 0

board = [' '*43 for x in range(22)]
tot_score = 0
ball_pos = ()
paddle_pos = ()

input_list = []

human = False
show = False


while curr != -1:
    state, out = run(copy, stdin, curr=curr, relative_base=relative_base)

    curr, relative_base, copy = state

    board, score, ball_pos, paddle_pos = update_board(out, board, ball_pos, paddle_pos)
    tot_score += score

    if show:
        os.system('cls')
        for line in board:
            print(line)
        print('W'*43)
        print(tot_score)

    if human:
        joy = int(input())
    else:
        if paddle_pos[0] > ball_pos[0]:
            joy = -1
        elif paddle_pos[0] < ball_pos[0]:
            joy = 1
        else:
            joy = 0
    stdin = [joy]
    input_list.append(joy)

print(score)
