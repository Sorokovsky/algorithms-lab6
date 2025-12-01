def input_car() -> (float, float):
    try:
        power = float(input("Введіть потужність двигуна в кінських силах: "))
        price = float(input("Введіть вартість автомобіля в грн: "))
        return power, price
    except ValueError:
        print("Ви ввели некоректні данні, спробуйте ще.")
        return input_car()

def enter_cars(count: int) -> dict[float, float] | None:
    if count < 0:
        print("Кількість машин не може бути від'ємна")
        return None

    cars: dict[float, float] = {}
    print()
    for i in range(count):
        power, price = input_car()

def main() -> None:
    power, price = input_car()
    print(f"{power} к.с")
    print(f"{price} грн")

if __name__ == "__main__":
    main()