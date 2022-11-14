
import math
import random 
import os


my_hand_1 = []
my_hand_total = sum(my_hand_1)
end_game = True
os.system("clear")

print("\n \n \n \n \n \n \n \n \nWelcome to BlackJack \n \n \n")

card_options = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def pick_a_card():
    

    end_game = True
    if end_game == True :   
        choice = random.choice(card_options)
        my_hand_1.append(choice) 
        # print(my_hand_1)
        # return my_hand_1
        my_hand_total = sum(my_hand_1)

        if my_hand_total < 21:
            print(f" You just picked a {choice}")
            print(f" Your current hand total is {my_hand_total} \n")
            end_deal = input("\n Do you wish to continue?").lower()
            if end_deal == "y" :
                pick_a_card()
            else :
                end_game = False
                return 
        else:
            print(" BUST")

    else:
        return 


pick_a_card()

my_hand_total = sum(my_hand_1)
print(f" Your hand total is {my_hand_total} \n \n ")


dealer_hand_1 = random.choice(card_options)

my_hand_2 = random.choice(card_options)

dealer_hand_2 = random.choice(card_options)


dealer_hand_total = dealer_hand_1 + dealer_hand_2


# print(my_hand_1)
# print(my_hand_2)
# print(my_hand_total)