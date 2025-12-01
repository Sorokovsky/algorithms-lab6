from commands_system.add_car_command import AddCarCommand
from commands_system.command_context import CommandContext
from commands_system.exit_command import ExitCommand
from commands_system.remove_car_command import RemoveCarCommand
from commands_system.show_cars_commands import ShowCarsCommand
from commands_system.show_sorted_cars_command import ShowSortedCarsCommand


def main() -> None:
    context = CommandContext()
    context.add_command(ExitCommand())
    context.add_command(AddCarCommand())
    context.add_command(ShowCarsCommand())
    context.add_command(ShowSortedCarsCommand())
    context.add_command(RemoveCarCommand())
    context.start()

if __name__ == "__main__":
    main()