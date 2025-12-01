from commands_system.command import Command
from commands_system.command_context import CommandContext


class ExitCommand(Command):
    def get_id(self: "Command") -> int:
        return 0

    def get_title(self: "Command") -> str:
        return "Вихід"

    def process(self: "Command", context: CommandContext) -> None:
        context.exit()
