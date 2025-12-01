from commands_system.command import Command
from commands_system.command_context import CommandContext


class AddCarCommand(Command):
    def get_title(self: "AddCarCommand") -> str:
        return "Додати автомобіль"

    def process(self: "AddCarCommand", context: "CommandContext") -> None:
        power, price = self._enter_car()
        context.get_database().add_item(power, price)

    def _enter_car(self: "AddCarCommand") -> (float, float):
        try:
            power = float(input("Введіть потужність автомобіля в кінських силах: "))
            price = float(input("Введіть ціну автомобіля в грн: "))
            return power, price
        except ValueError:
            print("Ви ввели не коректні данні. Спробуйте ще.")
            return self._enter_car()
