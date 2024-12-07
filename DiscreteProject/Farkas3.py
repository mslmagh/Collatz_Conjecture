import matplotlib.pyplot as plt

def farkas_steps(num):
    steps = 0  # Adım sayısını saklamak için değişken kullanıyoruz
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

def find_max_farkas(limit):
    max_steps = 0
    number_with_max_steps = 0

    for num in range(1, limit + 1):
        steps = farkas_steps(num)
        if steps > max_steps:
            max_steps = steps
            number_with_max_steps = num

    return number_with_max_steps, max_steps

# 1'den 1 milyona kadar olan sayılardan en çok adıma sahip olanı bulalım
limit = 1_000_000
number, steps = find_max_farkas(limit)

print(f"En çok adıma sahip olan sayı: {number}")
print(f"Adım sayısı: {steps}")
