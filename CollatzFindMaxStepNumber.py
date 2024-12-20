def collatz_steps(num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        steps += 1
    return steps


def find_max_collatz(limit):
    max_steps = 0
    number_with_max_steps = 0

    for num in range(1, limit + 1):
        steps = collatz_steps(num)
        if steps > max_steps:
            max_steps = steps
            number_with_max_steps = num

    return number_with_max_steps, max_steps



limit = 1_000_000
number, steps = find_max_collatz(limit)

print(f"The number of max step number: {number}")
print(f"Number of step: {steps}")
