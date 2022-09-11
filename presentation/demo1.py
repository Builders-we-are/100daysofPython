#  program to welcome new students and inform them of the best contact for the group

#  inputs : first name , last name  
# outputs: welcome to the devops group
#  reach out to Edoboye, Eloho and Osay for more infor
#  length of your name for fun

print("Congratulations, you are on your way to become a programer!!!")
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

f_name_len = len(f_name)

l_name_len = len(l_name)

len_of_fullname = f_name_len + l_name_len

contact_1 = "Edoboye"
contact_2 = "Osayamen"
contact_3 = "Elohor"

email1 = contact_1 + "@devopsgroup.com"
email2 = contact_2 + "@devopsgroup.com"
email3 = contact_3 + "@devopsgroup.com"

print(f"Welcome {f_name.capitalize()} {l_name.capitalize()} to the DEVOPS group, we are glad you are interested in Programming")
print(f"for more information, you can contact \n{contact_1} at {email1} \n{contact_2} at {email2} \n{contact_3} at {email3}")
print(f"Just for fun, your full name has {len_of_fullname} characters.")