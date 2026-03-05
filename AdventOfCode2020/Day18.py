def evaluate(ex, eval_method):
    """
    Evaluate mathematical expressions.

    Replace top level parenthesis recursively while also splitting the
    expression into numbers and operators in a list. Since there are
    no more parenthesis, replace numbers in the list using the requested
    method.
    """

    ex_list = []
    ind = 0
    while ind < len(ex):
        if ex[ind] == '(':
            count = 1
            last_ind = ind+1
            while count > 0:
                if ex[last_ind] == '(':
                    count += 1
                elif ex[last_ind] == ')':
                    count -= 1
                last_ind += 1
            last_ind -= 1

            ex_list.append(evaluate(ex[ind+1: last_ind], eval_method))
        else:
            # single digit number
            ex_list.append(int(ex[ind]))
            last_ind = ind

        if last_ind < len(ex)-1:
            # get operator
            op = ex[last_ind+2]
            ex_list.append(op)
        ind = last_ind+4

    return eval_method(ex_list)


def equal_presidence(ex_list):
    while len(ex_list) > 1:
        a = ex_list[0]
        b = ex_list[2]
        op = ex_list[1]
        if op == '+':
            n = a+b
        elif op == '*':
            n = a*b
        ex_list = [n]+ex_list[3:]
    return ex_list[0]


def addition_first(ex_list):
    while '+' in ex_list:
        ind = ex_list.index('+')
        a = ex_list[ind-1]
        b = ex_list[ind+1]
        ex_list = ex_list[:ind-1]+[a+b]+ex_list[ind+2:]

    # pass multiplication to other code
    return equal_presidence(ex_list)


tot1 = 0
tot2 = 0
with open('input/input18.txt') as f:
    for line in f:
        line = line.strip()
        tot1 += evaluate(line, equal_presidence)
        tot2 += evaluate(line, addition_first)

print(tot1)
print(tot2)
