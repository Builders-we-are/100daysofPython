First_name = input("What is your first name? \n")
Last_name = input("What is your last name? \n")

def format_name(First_name,Last_name):
    formated_f_name = First_name.title()
    formated_l_name = Last_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name(First_name,Last_name)
print(formated_string)