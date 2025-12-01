from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.enter_car import enter_car


class AddManyCarsCommand(Command):
    def get_title(self: "AddManyCarsCommand") -> str:
        return "Додати кілька автомобілів"

    def process(self: "AddManyCarsCommand", context: CommandContext) -> None:
        database = context.get_database()
        try:
            count = int(input("Введіть кількість нових машин: "))
            if count < 1:
                raise ValueError
            for i in range(count):
                print(f"{i + 1}-й автомобіль")
                database.add_item(*enter_car())

        except ValueError:
            print("Не можлива кількість нових машин. Спробуйте ще")
            self.process(context)
