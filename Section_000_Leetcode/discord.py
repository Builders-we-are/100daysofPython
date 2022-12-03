

words = input("please enter words separated by spaces: ")
print(f"You entered the words below \n{words} \n")

wordlist = sorted(words.split())
print(f"words are split and sorted as shown below \n {wordlist} \n")

for i in wordlist:
    print(i)

# Find out how to edit files using python.

with open('testfile.txt', 'a') as f:
    f.write(f"\nentry is: {words}\n")
    f.write(f"sorted entry is: {wordlist}\n")
