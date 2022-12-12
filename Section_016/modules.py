

# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
table.field_names = ["Type", "Name"]
table.add_row(["Electric", "Pikachu"])
table.add_row(["Water", "Squirtle"])
table.add_row(["Fire", "Charmander"])
table.sortby = "Name"
table.reversesort = True

table.align = "c"
table.align["Type"] = "l"
print(table)

# table.del_row(0)
# table.del_column("Type")
# table.clear_rows()
# table.clear()


print(table.get_string(fields=["Type"]))
print(table.get_string(fields=["Name"]))
table.reversesort = False
print(table.get_string(sortby="Type"))
