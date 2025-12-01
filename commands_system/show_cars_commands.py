from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.show_car_item import show_car_item


class ShowCarsCommand(Command):
    def get_title(self: "ShowCarsCommand") -> str:
        return "Вивести інформацію про всіх автомобілів"

    def process(self: "ShowCarsCommand", context: CommandContext) -> None:
        print("Автомобілі")
        context.get_database().loop(show_car_item)
