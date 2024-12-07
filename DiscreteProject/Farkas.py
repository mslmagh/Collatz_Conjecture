import matplotlib.pyplot as plt

def farkas_steps(num):
    steps = 0
    while num != 1:
        if num % 3 == 1:
            num = (num - 1) // 3
        elif num % 6 == 0 or num % 6 == 2:
            num //= 2
        elif num % 6 == 3 or num % 6 == 5:
            num = (3 * num + 1) // 2
        else:
            break  # Eğer hiçbir kural uygulanamıyorsa döngüden çık
        steps += 1
    return steps

def plot_farkas_variant(start, end):
    numbers = list(range(start, end + 1))
    steps = [farkas_steps(num) for num in numbers]

    plt.figure(figsize=(10, 6))
    plt.plot(numbers, steps, marker=".", linestyle="-", color="#FF000099")  # Kırmızı renk, opaklık
    plt.title("Farkas Variant Steps vs Number")
    plt.xlabel("Number")
    plt.ylabel("Steps")
    plt.grid(True)
    plt.yscale("log")  # Logaritmik ölçek
    plt.show()

# 1'den 1 milyona kadar aralık belirleyip grafiği çizelim
plot_farkas_variant(1, 1000000)