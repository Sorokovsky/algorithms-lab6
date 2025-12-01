from commands_system.command_context import CommandContext
from commands_system.exit_command import ExitCommand


def main() -> None:
    context = CommandContext()
    context.add_command(ExitCommand())
    context.start()

if __name__ == "__main__":
    main()