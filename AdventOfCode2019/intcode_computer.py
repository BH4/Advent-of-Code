from collections import defaultdict

"""
Existing opcodes:
01, a, b, c - a+b -> c
02, a, b, c - a*b -> c
03, a - input -> a
04, a - a -> output
05, a, b - if a != 0: curr = b
06, a, b - if a == 0: curr = b
07, a, b, c - if a<b: c = 1 else c=0
08, a, b, c - if a==b: c = 1 else c=0
09, a - relative_base += a
99 end

ABCDE
DE - two-digit opcode
 C - mode of 1st parameter
 B - mode of 2nd parameter
 A - mode of 3rd parameter
 and so on

Parameter modes:
0 position mode - The parameter is interpreted as a position in the code to get the input from
1 immediate mode - The parameter is itself the input
2 relative mode - 
"""


def get_in(code, pm, ind, relative_base):
    if pm == 0:
        return code[code[ind]]
    if pm == 1:
        return code[ind]
    if pm == 2:
        return code[code[ind]+relative_base]
    print('Error: Invalid parameter mode')


def get_out_ind(code, pm, ind, relative_base):
    if pm == 1:
        print('Error: output parameter mode cannot be immediate')

    if pm == 0:
        return code[ind]

    if pm == 2:
        return code[ind]+relative_base

    print('Error: Invalid parameter mode')


def run(code, stdin, curr=0, relative_base=0):
    """
    Both code and stdin are lists of integers
    """
    output_to_return = []

    # Turn code into defaultdict in order to give it extra memory beyond its coded values
    cdd = defaultdict(int)
    for i, x in enumerate(code):
        cdd[i] = x
    code = cdd

    # curr = 0
    instruction = code[curr]
    opcode = instruction % 100
    parameter_modes = instruction//100

    while opcode != 99:
        if opcode in [1, 2, 7, 8]:  # 2 inputs and 1 output index
            pm1 = parameter_modes % 10
            pm2 = (parameter_modes//10) % 10
            pm3 = (parameter_modes//100) % 10

            in1 = get_in(code, pm1, curr+1, relative_base)
            in2 = get_in(code, pm2, curr+2, relative_base)
            out_ind = get_out_ind(code, pm3, curr+3, relative_base)

            if opcode == 1:
                code[out_ind] = in1+in2
            elif opcode == 2:
                code[out_ind] = in1*in2
            elif opcode == 7:
                code[out_ind] = int(in1 < in2)
            elif opcode == 8:
                code[out_ind] = int(in1 == in2)

            # Move to next instruction
            curr += 4
        elif opcode in [3]:  # one output index
            pm1 = parameter_modes % 10

            out_ind = get_out_ind(code, pm1, curr+1, relative_base)

            if len(stdin) == 0:
                list_code = []
                for i in range(0, max(code.keys())+1):
                    list_code.append(code[i])
                state = (curr, relative_base, list_code)
                return state, output_to_return

            code[out_ind] = stdin.pop(0)

            # Move to next instruction
            curr += 2
        elif opcode in [4]:  # one input index
            pm1 = parameter_modes % 10

            in1 = get_in(code, pm1, curr+1, relative_base)

            output_to_return.append(in1)

            # Move to next instruction
            curr += 2

            # INSTRUCTION POINTER MODIFICATION CODES BELOW THIS POINT
        elif opcode in [5, 6]:  # two inputs
            pm1 = parameter_modes % 10
            pm2 = (parameter_modes//10) % 10

            in1 = get_in(code, pm1, curr+1, relative_base)
            in2 = get_in(code, pm2, curr+2, relative_base)

            if opcode == 5:
                if in1 != 0:
                    curr = in2
                else:
                    curr += 3
            elif opcode == 6:
                if in1 == 0:
                    curr = in2
                else:
                    curr += 3
        elif opcode in [9]:
            pm1 = parameter_modes % 10

            in1 = get_in(code, pm1, curr+1, relative_base)
            relative_base += in1

            curr += 2
        else:
            print(instruction, opcode, parameter_modes)
            print('Error: invalid opcode')
            quit()

        #print(relative_base)
        # Get next instruction
        instruction = code[curr]
        opcode = instruction % 100
        parameter_modes = instruction//100

    list_code = []
    for i in range(0, max(code.keys())+1):
        list_code.append(code[i])

    state = (-1, relative_base, list_code)
    return state, output_to_return
