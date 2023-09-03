import pandas as pd
import math
import os

os.system("clear")

data = pd.read_csv("Squirrel_Data.csv")
# print(data)

fur_color_list = (data["Primary Fur Color"].to_list()
                  )  # don't forget parenthesis
# print(type(fur_color_list))
# print(set(fur_color_list))
check_list = ["Cinnamon", "Gray", "Black"]
check_list_total = []
for i in check_list:
    total = len([item for item in fur_color_list if item == i])
    check_list_total.append(total)
print(check_list)
print(check_list_total)

data_dict = {
    "Fur Color": check_list,
    "Count": check_list_total
}

df = pd.DataFrame(data_dict)
print(df)

df.to_csv("squirrel_count_self.csv")
