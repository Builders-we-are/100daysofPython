
import math
import random 
import os


my_hand_1 = []
my_hand_total = sum(my_hand_1)

end_game = True

dealer_hand = []
dealer_hand_total = sum(dealer_hand)
os.system("clear")

print("\n \n \n \n \n \n \n \n \nWelcome to BlackJack \n \n \n")

card_options = [11,2,3,4,5,6,7,8,9,10,10,10,10]


# Select a card at random for the dealer
def pick_a_card_dealer():
    #insert cpu 2nd card here and pick till ends
    # if dealer_hand_total == 21:
    choice_cpu = random.choice(card_options)
    dealer_hand.append(choice_cpu) 
    return choice_cpu


# Select a card at random for the user
def pick_a_card_me():
    end_game = True
    if end_game == True :   
        choice_me = random.choice(card_options)
        my_hand_1.append(choice_me) 
        my_hand_total = sum(my_hand_1)

        if my_hand_total == 21:
            print(f" User has a blackjack")
            my_hand_total = 21
            return my_hand_total

        elif my_hand_total < 22:
            print(f" You just picked a {choice_me}")
            print(f" Your current hand total is {my_hand_total} \n The cards in your hand are {my_hand_1}")
            end_deal = input("\n Do you wish to continue?").lower()
            if end_deal == "y" :
                pick_a_card_me()
            else :
                end_game = False
                return 
        else:
            print(" BUST")
            return my_hand_total

    else:
        return 

pick_a_card_dealer()
print(f"The computer's first card is {dealer_hand}")

pick_a_card_me()


# Continue to pick a card if the total is under 17
while dealer_hand_total < 17:
    pick_a_card_dealer()
    dealer_hand_total = sum(dealer_hand)
    print(f"{dealer_hand} and the total is {dealer_hand_total} ")

#Conditions for ending the game
if dealer_hand_total == 21:
    print(" Dealer wins BlackJack ")
elif my_hand_total == 21:
    print(" You win BlackJack")
elif my_hand_total > 21:
    print("You BUST, you LOSE!")
elif my_hand_total < 21 and dealer_hand_total > my_hand_total and dealer_hand_total < 21:
    print(" Dealer wins, you lose!")
elif my_hand_total < 21 and dealer_hand_total < my_hand_total and dealer_hand_total < 21:
    print(" You win, Dealer lose!")
elif my_hand_total < 21 and dealer_hand_total >21:
    print(" You won!")
else: 
    print("Game Over")


print("\n \n \n ")

#Show final hand at end of game
print(f"My hand is {my_hand_1} and the total is {sum(my_hand_1)}")
print(f"Computer hand is {dealer_hand} and the total is {dealer_hand_total}")

print("\n \n \n ")