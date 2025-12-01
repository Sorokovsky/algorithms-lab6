from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.show_car_item import show_car_item


class ShowSortedCarsCommand(Command):
    def get_title(self: "ShowSortedCarsCommand") -> str:
        return "Вивести відсортовану інформацію про всіх автомобілей"

    def process(self: "ShowSortedCarsCommand", context: CommandContext) -> None:
        print("Відсортовані за потужністю автомобілі")
        context.get_database().loop(show_car_item, True)
