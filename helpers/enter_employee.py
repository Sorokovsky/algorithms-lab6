def enter_gender() -> str:
    genders = ["чоловік", "жінка"]
    gender = input("Введіть стать(чоловік чи жінка): ")
    if gender.lower() in genders:
        return gender.lower()
    print("Такої статі не існує.")
    return enter_gender()


def enter_employee() -> (str, float, str):
    try:
        return input("Введіть прізвище: "), int(input("Введіть зарплату в грн: ")), enter_gender()
    except ValueError:
        print("Не вірні данні. Спробуйте ще.")
        return enter_employee()
