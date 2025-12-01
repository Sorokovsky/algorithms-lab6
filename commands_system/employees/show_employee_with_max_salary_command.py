from commands_system.command import Command
from commands_system.command_context import CommandContext


class ShowEmployeeWithMaxSalaryCommand(Command):
    _surname: str
    _max_salary: float

    def get_title(self: "ShowEmployeeWithMaxSalaryCommand") -> str:
        return "Вивести прізвище працівника з найбільшою зарплатою"

    def process(self: "ShowEmployeeWithMaxSalaryCommand", context: CommandContext) -> None:
        self._max_salary = 0
        self._surname = ""
        context.get_database().loop(self._find_surname)
        print(f"Максимальна зарплата = {self._max_salary} у {self._surname}")

    def _find_surname(self: "ShowEmployeeWithMaxSalaryCommand", surname: str, value: (float, str), index: int) -> None:
        if value[0] > self._max_salary:
            self._surname = surname
            self._max_salary = value[0]
