from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.enter_car import enter_car


class AddCarCommand(Command):
    def get_title(self: "AddCarCommand") -> str:
        return "Додати автомобіль"

    def process(self: "AddCarCommand", context: "CommandContext") -> None:
        context.get_database().add_item(*enter_car())
