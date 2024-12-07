import matplotlib.pyplot as plt

def collatz_steps(num):
    steps = []
    while num != 1:
        steps.append(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    steps.append(1)
    return steps

def plot_collatz(num):
    steps = collatz_steps(num)

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(steps)), steps, marker=".", linestyle="-", color="r")
    plt.title(f"Collatz Sequence for {num}")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.yscale("log")
    plt.grid(True)
    plt.show()


plot_collatz(837799)
