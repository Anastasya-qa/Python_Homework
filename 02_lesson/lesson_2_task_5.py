m = int(input("Введите номер месяца: "))


def month_to_season(m):
    if 1 <= m <= 2 or m == 12:
        print("Зима")
    if (3 <= m <= 5):
        print("Весна")
    if (6 <= m <= 8):
        print("Лето")
    if (9 <= m <= 11):
        print("Осень")
    else:
        print("Введено неверное число.")


season = month_to_season(m)
