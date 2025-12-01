from commands_system.command import Command
from database import Database


class CommandContext:
    _database: Database
    _commands: list[Command]
    _title: str
    _is_running: bool

    def __init__(self: "CommandContext", title: str = "Меню") -> None:
        self._database = Database()
        self._commands = []
        self._title = title
        self._is_running = False

    def add_command(self: "CommandContext", command: Command) -> None:
        self._commands.append(command)

    def start(self: "CommandContext") -> None:
        self._is_running = True
        print(self._title)
        self._loop()

    def _loop(self: "CommandContext") -> None:
        while self._is_running:
            self._show_commands()
            self._choose_operation().process(self)

    def _show_commands(self: "CommandContext") -> None:
        for command in self._commands:
            print(f"{command.get_id()}-{command.get_title()}.")

    def exit(self: "CommandContext") -> None:
        self._is_running = False

    def _choose_operation(self: "CommandContext") -> "Command":
        try:
            command_id = int(input(">>> "))
            for command in self._commands:
                if command_id == command.get_id():
                    return command
            raise ValueError
        except ValueError:
            print("Ви не вибрали жодну команду. Спробуйте ще.")
            return self._choose_operation()
