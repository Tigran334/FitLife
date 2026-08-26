import sys

sys.stdout.reconfigure(encoding="utf-8")

WATER_PER_KG = 30

print("Здравствуйте")

user_name = input("Как вас зовут? ")

while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        if not (0 < user_age < 120):
            print("Укажите возраст от 1 до 119 лет.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите возраст целым числом.")

while True:
    try:
        user_weight = float(input("Введите вес в кг: "))
        if not (30 <= user_weight <= 300):
            print("Укажите вес от 30 до 300 кг.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите вес числом.")

while True:
    try:
        user_height = float(input("Введите рост в метрах: "))
        if not (1.0 <= user_height <= 2.5):
            print("Укажите рост от 1.0 до 2.5 метров.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите рост числом.")

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

water_ml = user_weight * WATER_PER_KG
water_liters = round(water_ml / 1000, 1)

print(f"\nОтчёт: {user_name}, {user_age} лет.")
print(f"Индекс массы тела: {bmi_rounded} кг/м².")
print(f"Норма воды: {water_liters:.1f} л. в день.")
print("Расчёт окончен. Будьте здоровы!")
