def is_year_leap(a):
    return True if a % 4 == 0 else False


year = int(input("Введите год: "))
result = is_year_leap(year)

print(f"год {year}: {result}")
