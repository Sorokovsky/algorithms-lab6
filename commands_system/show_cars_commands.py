from commands_system.command import Command
from commands_system.command_context import CommandContext


class ShowCarsCommand(Command):
    def get_title(self: "ShowCarsCommand") -> str:
        return "Вивести інформацію про всіх автомобілів "

    def process(self: "ShowCarsCommand", context: CommandContext) -> None:
        print("Автомобілі")
        context.get_database().loop(self._show_car)

    @staticmethod
    def _show_car(power: float, price: float, index: int) -> None:
        print(f"#{index + 1} Потужність: {power} к.с., Ціна: {price} грн.")
