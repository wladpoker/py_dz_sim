
print("   █████████     ███████       ███████     █████████  ██████████    ███████████   █████  █████████  \n  ███░░░░░███  ███░░░░░███   ███░░░░░███  ███░░░░░███░░███░░░░░█   ░░███░░██████ ░░███  ███░░░░░███ \n ███     ░░░  ███     ░░███ ███     ░░███░███    ░░░  ░███  █ ░     ░███ ░███░███ ░███ ███     ░░░  \n░███         ░███      ░███░███      ░███░░█████████  ░██████       ░███ ░███░░███░███░███          \n░███    █████░███      ░███░███      ░███ ░░░░░░░░███ ░███░░█       ░███ ░███ ░░██████░███          \n░░███  ░░███ ░░███     ███ ░░███     ███  ███    ░███ ░███ ░   █    ░███ ░███  ░░█████░░███     ███ \n ░░█████████  ░░░███████░   ░░░███████░  ░░█████████  ██████████    ██████████  ░░█████░░███████████")
zd = int(input("Введите номер задания(по порядку): "))
import random
if zd == 1:
    # На столе лежат n монеток. Некоторые из них лежат вверх
    # решкой, а некоторые – гербом. Определите минимальное число
    # монеток, которые нужно перевернуть, чтобы все монетки были
    # повернуты вверх одной и той же стороной. Выведите минимальное
    # количество монет, которые нужно перевернуть.
    number = int(input("Введите кол-во монет: "))
    i=1
    one = 0
    zero = 0
    for i in range(number):
        inp = random.randint(0, 1)
        print(inp)
        if inp == 1:
            one+=1
        else:
            zero+=1
    if one < zero:
        print(f"Перевернуть {one} раз/а")
    else:
        print(f"Перевернуть {zero} раз/а")
if zd == 2:
    # Петя и Катя – брат и сестра. Петя – студент, а Катя –
    # школьница. Петя помогает Кате по математике. Он задумывает два
    # натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
    # этого Петя делает две подсказки. Он называет сумму этих чисел S и их
    # произведение P. Помогите Кате отгадать задуманные Петей числа.

    # получем P
    # получаем S

    S = int(input("Введите сумму чисел: "))
    P = int(input("Введите произведение чисел: "))

    # P = X*Y
    # S = X+Y
    # P = (S - Y) * Y

    # P = S * Y - 2 * Y
    # P = Y * (S - Y)
    # P = S * Y - Y^2
    # Y^2 - S * Y + P = 0



    D = S * S - 4 * P

    if D < 0:
        print("Подсказки даны неверно!")
    elif D == 0:
        X = Y = S/2
        print(f"{S} {P} -> {Y} {X}")
    else:
        X = int((S + math.sqrt(D))/2)
        Y = int((S - math.sqrt(D))/2)
        print(f"{S} {P} -> {Y} {X}")


if zd == 3:
    # Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
    N = int(input("Введите нужное число: "))

    max_step = 1
    while N >= max_step:
        print(max_step)
        max_step *= 2
