print('''
*******************************************************************************
      .    _.----~~~~~~~7
             /              ~-..-~~--..--.
       .'.'.'                             `.
         .~                                 \
       .'                                    `.
   .   (                                       \
 '.    )                                        `.
   '  (                                           ~-.
       \                                             ~-~~7
        `.       __.._                                  .'
          ~-.--~~     ~--.                             /
                         ;                          .-~
                         (                        .~
                          `.                    .'
                            ;                   ;
                            `.                  `       _
                             )                   )     / )
                            (                 _.-'  .-' .'
                            `.               (      )   /
                              7             _;      < _/
                               \           /         ~
                                \         /
                                 `. __..-'
                                   ~
*******************************************************************************
''')
print("Welcome to Streets of Lagos.")
print("Your mission is to navigate the streets to you destination without dying.")

choice1 = input("You enter street. Where do you want to go? Type 'left' or 'right' \n").lower()
if choice1 == "left":
  choice2 = input("You jam 4 SARS officers. dem ask you for your laptop. Type 'Okay' to give dem. Type 'No' to argue. \n").lower()
  # .lower() allows your input to be Okay, okay, oKAY, adn so on. 
  if choice2 == "no":
    choice3 = input("dem slap you put you for black mariah. \n Inside Black mariah Sergeant A says find boys something \n how much do you give dem: '20', '50', '200'  \n").lower()
    if choice3 == "20":
      print("dem flog you and lock you for cell. Game Over.")
    elif choice3 == "50":
      print("dem konk you and lock you for cell. Game Over")
    elif choice3 == "200":
      print("dem Hail you and let you go free")
  else:
    print("As dem want collect your phone DPO walked by and dem let you go.")
else:
  print("Moule Jam you. Game Over.")

  # You can find more ascii arts at
  # ascii.co.uk/art