# # 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
position = int(position)
y_axis = int(position % 10)
# print(f"y_axis is {y_axis}")

x_axis = int((position - y_axis ) / 10)
# print(f"x_axis is {x_axis}")
# print(f"y_axis is {y_axis}")

map[y_axis-1][x_axis-1]="X"
print(f"{row1}\n{row2}\n{row3}")

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


# notes for self
# odd_numbers = [1,3,5]
# even_numbers = [2,4,6]

# numbers = [odd_numbers , even_numbers]
# print(numbers[0][2])
# # print(sorted(numbers))
# # print(numbers.reverse)

# # print(numbers.pop(2))
