from commands_system.command import Command
from commands_system.command_context import CommandContext


class RemoveEmployeeCommand(Command):
    def get_title(self: "RemoveEmployeeCommand") -> str:
        return "Видалити співробітника"

    def process(self: "RemoveEmployeeCommand", context: CommandContext) -> None:
        context.get_database().remove_item(input("Введіть прізвище: "))
