import random

s = random.randint(1, 100)
attemps = 0

while True:
    try:
        u = int(input("Ваше число: "))
        attemps += 1
        if u < s:
            print("больше")
        elif u > s:
            print("меньше")
        elif u == s:
            print(f"Верно, это {s}!\nВы угадали за {attemps} попыток!")
            break
    except ValueError:
        print("Неверный ввод")
