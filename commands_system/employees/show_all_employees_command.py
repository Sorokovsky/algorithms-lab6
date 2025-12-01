from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.show_employee_item import show_employee_item


class ShowAllEmployeesCommand(Command):
    def get_title(self: "ShowAllEmployeesCommand") -> str:
        return "Вивести список співробітників"

    def process(self: "ShowAllEmployeesCommand", context: CommandContext) -> None:
        print("Співробітники")
        context.get_database().loop(show_employee_item)
