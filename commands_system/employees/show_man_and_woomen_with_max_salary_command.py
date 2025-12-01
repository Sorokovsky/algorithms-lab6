from commands_system.command import Command
from commands_system.command_context import CommandContext


class ShowManAndWomenWithMaxSalaryCommand(Command):
    _man_surname: str
    _women_surname: str
    _man_salary: float
    _women_salary: float

    def get_title(self: "ShowManAndWomenWithMaxSalaryCommand") -> str:
        return "Вивести прізвище чоловіка та жінки з найменшою зарплатою"

    def process(self: "ShowManAndWomenWithMaxSalaryCommand", context: CommandContext) -> None:
        self._man_salary = 0
        self._women_salary = 0
        self._man_surname = ""
        self._women_surname = ""
        context.get_database().loop(self.find)
        if self._man_surname != "":
            print(f"Найменша зарплата = {self._man_salary} у чоловіка: {self._man_surname}")
        if self._women_surname != "":
            print(f"Найменша зарплата = {self._women_salary} у жінки: {self._women_surname}")

    def find(self: "ShowManAndWomenWithMaxSalaryCommand", surname: str, value: (float, str), index: int) -> None:
        salary: float = value[0]
        gender: str = value[1]
        if gender == "чоловік" and (salary < self._man_salary or self._man_salary == 0):
            self._man_surname = surname
            self._man_salary = salary
        if gender == "жінка" and (salary < self._women_salary or self._women_salary == 0):
            self._women_surname = surname
            self._women_salary = salary
