from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.show_employee_item import show_employee_item


class ShowSortedEmployeesCommand(Command):
    def get_title(self: "ShowSortedEmployeesCommand") -> str:
        return "Вивести відсортований список співробітників"

    def process(self: "ShowSortedEmployeesCommand", context: CommandContext) -> None:
        print("Відсортований список співробітників за прізвищем")
        context.get_database().loop(show_employee_item, True)
