cel = float (input("введите температуру: "))
if cel <= 20:
    print("кондиционер включен")
else:
    print("кондиционер выключен")


month = int (input ("введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    x = "зима"
elif 3 <= month <= 5:
    x = "весна"
elif 6 <= month <= 8:
    x = "лето"
elif 9 <= month <= 11:
    x = "осень"
else:
    print("неверный номер месяца")
if 1 <= month <= 12:
    print (x)
else :
    print("неверный номер месяца")


def age1(dog_age):
    if dog_age <= 2:
        human_age = dog_age * 10.5
    else:
        human_age = 21 + (dog_age - 2) * 4
    return human_age
x = input("Введите возраст собаки (в годах): ")
try:
    age = float(x)
    if age < 1:
        print("Ошибка: возраст должен быть не меньше 1")
    elif age > 22:
        print("Ошибка: возраст должен быть не больше 22")
    else:
        human = age1(age)
        print(f"Возраст собаки в человеческих годах: {human}")
except ValueError:
    print("Ошибка: введено не число")


