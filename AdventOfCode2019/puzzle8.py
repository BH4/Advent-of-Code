import numpy as np


def num_zeros(M):
    tot = 0
    for row in M:
        for e in row:
            if e == 0:
                tot += 1
    return tot


with open('input/input8.txt', 'r') as f:
    line = f.readline()

    line = line.strip()

    curr = 0
    image = []
    while curr < len(line):
        layer = []
        for j in range(6):
            row = []
            for i in range(25):
                row.append(int(line[curr]))
                curr += 1

            layer.append(row)
        image.append(layer)


zeros_per_layer = [num_zeros(layer) for layer in image]

z = list(zip(*sorted(zip(zeros_per_layer, image))))

layer_fewest_0s = z[1][0]

num_ones = num_zeros(np.array(layer_fewest_0s)-1)
num_twos = num_zeros(np.array(layer_fewest_0s)-2)
print(num_ones*num_twos)


final_image = []
image = np.array(image)
for j in range(6):
    row = []
    for i in range(25):
        pxl = image[:, j, i]
        for z in pxl:
            if not z == 2:
                row.append(z)
                break
    final_image.append(row)

print(np.array(final_image))

