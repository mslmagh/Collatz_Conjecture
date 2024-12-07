import matplotlib.pyplot as plt

def collatz_steps(num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        steps += 1
    return steps

def plot_collatz(start, end):
    numbers = list(range(start, end + 1))
    steps = [collatz_steps(num) for num in numbers]

    plt.figure(figsize=(10, 6))
    plt.plot(numbers, steps, marker=".", linestyle="-", color="#FF000099")
    plt.title("Collatz Sequence Steps vs Number")
    plt.xlabel("Number")
    plt.ylabel("Steps")
    plt.grid(True)
    plt.yscale("log")
    plt.show()

# Aralık belirleyip grafiği çizelim
plot_collatz(1, 10000000)
