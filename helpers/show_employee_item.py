def show_employee_item(surname: str, value: (float, str), index: int) -> None:
    print(f"#{index + 1} Прізвище: {surname}, Зарплата: {value[0]} грн, Стать: {value[1]}")
