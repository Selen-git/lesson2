month = int(input("Введите номер месяца: "))
if (month < 1 or month > 12):
    print("Ошибка! Некорректный ввод.")
else:
    if month in [12, 1, 2]:
        season = "зима"
    elif month in [3, 4, 5]:
        season = "весна"
    elif month in [6, 7, 8]:
        season = "лето"
    else:
        season = "осень"

    print(f"{month} - {season}")
