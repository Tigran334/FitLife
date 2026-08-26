import sys

sys.stdout.reconfigure(encoding="utf-8")

WATER_PER_KG = 30

print("Здравствуйте")

user_name = input("Как вас зовут? ")

while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        if not (0 < user_age < 120):
            print(
                "Пожалуйста, укажите реальный возраст "
                "от 1 до 119 лет."
            )
            continue
        break
    except ValueError:
        print(
            "Ошибка! Нужно ввести целое число "
            "(например, 25)."
        )

while True:
    try:
        user_weight = float(
            input("Введите ваш вес в кг (например, 70.5): ")
        )
        if not (30 <= user_weight <= 300):
            print(
                "Кажется, вес указан неверно. "
                "Проверьте данные и попробуйте снова."
            )
            continue
        break
    except ValueError:
        print(
            "Ошибка! Нужно ввести число, "
            "можно с точкой (например, 80.3)."
        )

while True:
    try:
        user_height = float(
            input("Введите ваш рост в метрах (например, 1.75): ")
        )
        if not (1.0 <= user_height <= 2.5):
            print(
                "Рост должен быть в диапазоне "
                "от 1.0 до 2.5 метров. Проверьте ввод."
            )
            continue
        break
    except ValueError:
        print(
            "Ошибка! Нужно ввести число "
            "(например, 1.80)."
        )

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

water_ml = user_weight * WATER_PER_KG
water_liters = round(water_ml / 1000, 1)

print(
    f"\nОтчёт для пользователя: "
    f"{user_name}, {user_age} лет."
)
print(f"Твой индекс массы тела: {bmi_rounded} кг/м².")
print(
    f"Рекомендуемая норма воды: "
    f"{water_liters:.1f} л. в день."
)
print("Расчёт окончен. Будьте здоровы!")
