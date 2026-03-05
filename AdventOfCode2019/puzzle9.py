from intcode_computer import run


with open('input/input9.txt', 'r') as f:
    line = f.readline()

code = [int(x) for x in line.split(',')]

#code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

point, new_code, out = run(code, [1])
print(out)

point, new_code, out = run(code, [2])
print(out)
