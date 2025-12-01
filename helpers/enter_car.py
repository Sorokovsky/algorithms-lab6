def enter_car() -> (float, float):
    try:
        power = float(input("Введіть потужність автомобіля в кінських силах: "))
        price = float(input("Введіть ціну автомобіля в грн: "))
        return power, price
    except ValueError:
        print("Ви ввели не коректні данні. Спробуйте ще.")
        return enter_car()
