"""
To solve these problems I make two dictionaries. One dictionary represents the
steps which have the key as a prerequisite and the other represents the steps
which are a prerequisite for the key.

For both parts I use a loop which completes one step at a time, updating the
variable of interest (order and time respectively) as well as other variables
needed to determine future steps in the correct order.

The solution to the second problem is similar to the first but with the
addition of keeping track of the time until each step is completed.
"""


from collections import defaultdict

# Indexing instructions at a letter will give the steps which can be
# completed after.
all_steps = set()
requirements = defaultdict(list)
instructions = defaultdict(list)
with open('input/input7.txt') as f:
    for line in f:
        line = line.split()
        prereq = line[1]
        step = line[7]
        requirements[step].append(prereq)
        instructions[prereq].append(step)

        all_steps.add(step)
        all_steps.add(prereq)

# part 1

allowed_steps = sorted(all_steps - requirements.keys())
completed = set()
order = ''

while len(allowed_steps) > 0:
    curr = allowed_steps.pop(0)
    order += curr
    completed.add(curr)

    # Determine which steps are now allowed since curr has been completed.
    new_allowed = []
    for x in instructions[curr]:
        if x not in completed and x not in allowed_steps:
            allowed = True
            for test in requirements[x]:
                if test not in completed:
                    allowed = False
                    break
            if allowed:
                new_allowed.append(x)

    allowed_steps = sorted(allowed_steps + new_allowed)

print("Order for steps to be completed: {}".format(order))


# part 2

num_workers = 5
allowed_steps = sorted(all_steps - requirements.keys())
completed = set()
time = 0

# Take at most num_workers tasks to be done concurrently. Put the time till
# completion in the first index of the pair.
current_work = sorted([[60+ord(s)-ord("A")+1, s] for s in allowed_steps[:num_workers]])
allowed_steps = allowed_steps[num_workers+1:]


while len(allowed_steps) > 0 or len(current_work) > 0:
    elapsed_time, curr = current_work.pop(0)

    time += elapsed_time
    # reduce the time until completion for each step by the elapsed time.
    for i in range(len(current_work)):
        current_work[i][0] -= elapsed_time

    completed.add(curr)

    # Determine which steps are now allowed since curr has been completed.
    new_allowed = []
    for x in instructions[curr]:
        if x not in completed and x not in allowed_steps:
            allowed = True
            for test in requirements[x]:
                if test not in completed:
                    allowed = False
                    break
            if allowed:
                new_allowed.append(x)

    allowed_steps = sorted(allowed_steps + new_allowed)

    resting_workers = num_workers-len(current_work)
    new_work = [[60+ord(s)-ord("A")+1, s] for s in allowed_steps[:resting_workers]]
    allowed_steps = allowed_steps[resting_workers+1:]

    current_work = sorted(current_work + new_work)

print("Minimum time for all steps with {} workers: {}".format(num_workers, time))
