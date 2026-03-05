from collections import defaultdict


reactions = dict()
amounts_produced = dict()
with open('input/input14.txt', 'r') as f:
    for line in f:
        line = line.strip()
        inputs = line.split(', ')
        last = inputs[-1].split(' => ')
        inputs[-1] = last[0]

        output = last[1].split(' ')
        output[0] = int(output[0])

        for i in range(len(inputs)):
            temp = inputs[i].split(' ')
            inputs[i] = [int(temp[0]), temp[1]]

        reactions[output[1]] = inputs
        amounts_produced[output[1]] = output[0]




