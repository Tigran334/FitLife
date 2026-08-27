import sys

sys.stdout.reconfigure(encoding="utf-8")

WATER_PER_KG = 30
MIN_AGE = 1
MAX_AGE = 119
MIN_WEIGHT = 30
MAX_WEIGHT = 300
MIN_HEIGHT = 1.0
MAX_HEIGHT = 2.5
ML_PER_LITER = 1000
ROUND_DIGITS = 1

print("Здравствуйте")

user_name = input("Как вас зовут? ")

while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        if not (MIN_AGE <= user_age <= MAX_AGE):
            print("Укажите возраст от 1 до 119 лет.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите возраст целым числом.")

while True:
    try:
        user_weight = float(input("Введите вес в кг: "))
        if not (MIN_WEIGHT <= user_weight <= MAX_WEIGHT):
            print("Укажите вес от 30 до 300 кг.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите вес числом.")

while True:
    try:
        user_height = float(input("Введите рост в метрах: "))
        if not (MIN_HEIGHT <= user_height <= MAX_HEIGHT):
            print("Укажите рост от 1.0 до 2.5 метров.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите рост числом.")

bmi = round(user_weight / (user_height ** 2), ROUND_DIGITS)

water_ml = user_weight * WATER_PER_KG
water_liters = round(water_ml / ML_PER_LITER, ROUND_DIGITS)

print(f"\nОтчёт: {user_name}, {user_age} лет.")
print(f"Индекс массы тела: {bmi} кг/м².")
print(f"Норма воды: {water_liters:.1f} л. в день.")
print("Расчёт окончен. Будьте здоровы!")
