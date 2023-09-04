import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(value)
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(value)
    # print(row)
    # print(row["score"])
    # print(row.score)
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("./nato.csv")
df = pandas.DataFrame(nato)
# print(df)
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ").upper
result = [nato_dict[i.upper()] for i in name]
print(result)
