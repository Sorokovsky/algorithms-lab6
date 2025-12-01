from commands_system.cars.add_car_command import AddCarCommand
from commands_system.cars.add_many_cars_command import AddManyCarsCommand
from commands_system.cars.price_when_power_more_than_100_command import PriceWhenPowerMoreThan100Command
from commands_system.cars.remove_car_command import RemoveCarCommand
from commands_system.cars.show_cars_commands import ShowCarsCommand
from commands_system.cars.show_sorted_cars_command import ShowSortedCarsCommand
from commands_system.command_context import CommandContext
from commands_system.exit_command import ExitCommand


def main() -> None:
    context = CommandContext("Легкові автомобілі")
    context.add_command(ExitCommand())
    context.add_command(AddCarCommand())
    context.add_command(AddManyCarsCommand())
    context.add_command(ShowCarsCommand())
    context.add_command(ShowSortedCarsCommand())
    context.add_command(PriceWhenPowerMoreThan100Command())
    context.add_command(RemoveCarCommand())
    context.start()

if __name__ == "__main__":
    main()