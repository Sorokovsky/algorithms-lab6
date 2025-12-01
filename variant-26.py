from commands_system.command_context import CommandContext
from commands_system.employees.add_employee_command import AddEmployeeCommand
from commands_system.employees.add_many_emploees_command import AddManyEmployeeCommand
from commands_system.employees.remove_employee_command import RemoveEmployeeCommand
from commands_system.employees.show_all_employees_command import ShowAllEmployeesCommand
from commands_system.employees.show_sorted_employees_command import ShowSortedEmployeesCommand
from commands_system.exit_command import ExitCommand


def main() -> None:
    context = CommandContext()
    context.add_command(ExitCommand())
    context.add_command(AddEmployeeCommand())
    context.add_command(AddManyEmployeeCommand())
    context.add_command(ShowAllEmployeesCommand())
    context.add_command(ShowSortedEmployeesCommand())
    context.add_command(RemoveEmployeeCommand())
    context.start()


if __name__ == '__main__':
    main()
