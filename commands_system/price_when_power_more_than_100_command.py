from commands_system.command import Command
from commands_system.command_context import CommandContext


class PriceWhenPowerMoreThan100Command(Command):
    _total_price: float

    def get_title(self: "PriceWhenPowerMoreThan100Command") -> str:
        return "Сумарна ціна автомобілів, у яких потужність перевищує 100 к.с"

    def process(self: "PriceWhenPowerMoreThan100Command", context: CommandContext) -> None:
        self._total_price = 0
        context.get_database().loop(self._collect_price)
        print(f"Ціна: {self._total_price}")

    def _collect_price(self: "PriceWhenPowerMoreThan100Command", power: float, price: float, index: int) -> None:
        if power > 100:
            self._total_price += price
