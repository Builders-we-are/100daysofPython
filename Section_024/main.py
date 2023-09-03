'''
TODO: Create a letter using starting_letter.txt 
for each name in invited_names.txt
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".
    
Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

a is for append
r is for read
w is for write
'''
import os
os.system("clear")

'''with open("Input/Names/invited_names.txt", "r") as names:
    new = names.readlines()

new2=[]
for each in new:
    new3 = each.strip("\n")
    new2.append(new3)

for i in new2:
    with open("Input/Letters/starting_letter.txt",mode="r") as file1:
        change=file1.readlines()
        letter=change[0].replace("[Name]",i)

    with open(f"Output/ReadyToSend/letter_for_{i}.txt",mode="w") as file2:
        file2.write(letter)
        for j in range(1,7):
            file2.write(change[j])'''

with open("Input/Names/invited_names.txt", "r") as names:
    new = names.readlines()

with open("Input/Letters/starting_letter.txt",mode="r") as file1:
    generated_letter = file1.read()
    for names in new:
        stripped_name = names.strip()
        new_letter = generated_letter.replace("[Name]",stripped_name)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as file2:
            file2.write(new_letter)