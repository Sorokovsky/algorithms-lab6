from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.enter_employee import enter_employee


class AddEmployeeCommand(Command):
    def get_title(self: "CommandContext") -> str:
        return "Додати співробітника"

    def process(self: "AddEmployeeCommand", context: CommandContext) -> None:
        surname, salary, gender = enter_employee()
        context.get_database().add_item(surname, (salary, gender))
