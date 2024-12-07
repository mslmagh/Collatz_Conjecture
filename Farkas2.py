import matplotlib.pyplot as plt

def farkas_steps(num):
    steps = []
    while num != 1:
        steps.append(num)
        if num % 3 == 1:
            num = (num - 1) // 3
        elif num % 6 == 0 or num % 6 == 2:
            num //= 2
        elif num % 6 == 3 or num % 6 == 5:
            num = (3 * num + 1) // 2
        else:
            break
    steps.append(1)
    return steps

def plot_farkas_sequence(num):
    steps = farkas_steps(num)

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(steps)), steps, marker=".", linestyle="-", color="r")
    plt.title(f"Farkas Variant Sequence for {num}")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.yscale("log")
    plt.grid(True)
    plt.show()

plot_farkas_sequence(851967)