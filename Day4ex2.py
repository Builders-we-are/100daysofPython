# Exercise3 Treasure Map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# to get the input position of 23 which is supposed to be a str bcos of input functn, u can split d str
# horizontal = position[0] #2 i.e, the 0 item out of this str 23
# vertical = position[1] #3 i.e, 23 positions are 0 & 1, 0-vertical,1-vertical
# print(map[vertical]) # this will give a TypeError so, convert to int

horizontal = int(position[0]) #2
vertical = int(position[1]) #3
# print(map[vertical]) #this will still give Error bcos of the range in the list which is 0,1,2. the 3 is out of range
# this because the input was 23 and 3 is out of range

#  print(map[vertical -1])

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
# what if we do not separate these into 2 lines
# instead of separating these2 rows we can have a single row by tagging the map
map[vertical - 1][horizontal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")