from commands_system.command import Command
from commands_system.command_context import CommandContext


class RemoveCarCommand(Command):
    def get_title(self: "Command") -> str:
        return "Видалити машину"

    def process(self: "Command", context: CommandContext) -> None:
        try:
            power: float = float(input("Введіть потужність автомобіля: "))
            context.get_database().remove_item(power)
        except ValueError:
            print("Не коректні данні, спробуйте ще.")
            self.process(context)
