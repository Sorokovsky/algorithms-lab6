from commands_system.command import Command
from commands_system.command_context import CommandContext
from helpers.enter_employee import enter_employee


class AddManyEmployeeCommand(Command):
    def get_title(self: "AddManyEmployeeCommand") -> str:
        return "Додати кількох співробітників"

    def process(self: "AddManyEmployeeCommand", context: CommandContext) -> None:
        database = context.get_database()
        try:
            count = int(input("Введіть кількість нових співробітників: "))
            if count < 1:
                raise ValueError
            for i in range(count):
                print(f"{i + 1}-співробітник")
                surname, salary, gender = enter_employee()
                database.add_item(surname, (salary, gender))
        except ValueError:
            print("Не коректна кількість.")
            self.process(context)
