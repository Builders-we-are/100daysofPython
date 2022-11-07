



def format_name():
    f_name = input("What's your first name? ").title()
    l_name = input("What's your last name? ").title()

    if f_name == "" or l_name == "":
        return "You didn't provide a valid input. "
    return f"{f_name} {l_name}"


print(format_name())