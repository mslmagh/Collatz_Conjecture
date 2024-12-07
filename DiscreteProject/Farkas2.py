import matplotlib.pyplot as plt

def farkas_steps(num):
    steps = []  # Adımları saklamak için liste kullanıyoruz
    while num != 1:
        steps.append(num)
        if num % 3 == 1:
            num = (num - 1) // 3
        elif num % 6 == 0 or num % 6 == 2:
            num //= 2
        elif num % 6 == 3 or num % 6 == 5:
            num = (3 * num + 1) // 2
        else:
            break  # Eğer hiçbir kural uygulanamıyorsa döngüden çık
    steps.append(1)  # Son olarak 1'i ekliyoruz
    return steps

def plot_farkas_sequence(num):
    steps = farkas_steps(num)

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(steps)), steps, marker=".", linestyle="-", color="r")
    plt.title(f"Farkas Variant Sequence for {num}")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.yscale("log")  # Logaritmik ölçek
    plt.grid(True)
    plt.show()

# Belirli bir sayı için Farkas varyantını çizelim
plot_farkas_sequence(851967)