def input_car() -> (float, float):
    try:
        power = float(input("Введіть потужність двигуна в кінських силах: "))
        price = float(input("Введіть вартість автомобіля в грн: "))
        return power, price
    except ValueError:
        print("Ви ввели некоректні данні, спробуйте ще.")
        return input_car()

def enter_cars(count: int) -> dict[float, float] | None:
    if count < 1:
        print("Кількість машин не може бути від'ємна чи 0.")
        return None
    print(f"Введіть данні про {count} автомобілей.")
    cars: dict[float, float] = {}
    print()
    for i in range(count):
        print(f"{i + 1}-й автомобіль")
        power, price = input_car()
        cars[power] = price
    return cars


def print_cars(cars: dict[float, float]) -> None:
    print(f"{len(cars)} автомобілей")
    i = 0
    for power, price in cars.items():
        i += 1
        print(f"{i}-й автомобіль: ")
        print(f"Потужність: {power} к.с.")
        print(f"Ціна: {price} грн.")


def get_price_of_car_when_power_mor(cars: dict[float, float], min_power: int) -> float:
    total_price: float = 0.0
    for power, price in cars.items():
        if power > min_power:
            total_price += price
    return total_price

def main() -> None:
    cars = enter_cars(10)
    print_cars(cars)
    print(
        f"Загальна вартість автомобілів, у яких потужність двигуна перевищує 100 к.с: {get_price_of_car_when_power_mor(cars, 100)}")

if __name__ == "__main__":
    main()