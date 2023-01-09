from art import logo

print (logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(original_text,shift_amount,crypt_direction):

    
    encrypt_word = ""

    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            if crypt_direction == "encode":
                new_index = index + shift_amount
                if new_index > 25:
                    new_index = new_index - 26
            elif crypt_direction == "decode":
                new_index = index - shift_amount
                if new_index < 0 :
                    new_index = new_index + 26                
            encrypted_char = alphabet[new_index]
            encrypt_word +=encrypted_char
        else:
            encrypt_word +=(char)
                            
    print(encrypt_word)

# def decrypt(original_text,shift_amount):
    
#     decrypt_word = ""

#     for letter in original_text:
#         if letter in alphabet:
#             index = alphabet.index(letter)
#             new_index = index - shift_amount
#             if new_index < 0 :
#                 new_index = new_index + 26
#             dencrypt_letter = alphabet[new_index]
#             decrypt_word +=dencrypt_letter
#         else:
#             decrypt_word +=(letter)
                            
#     print(decrypt_word)

                
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift     amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction == "encode":
#     encrypt(text,shift)
# elif direction == "decode":
#     decrypt(text,shift)
# else:
#     print("please call a correct function")

restart = True

while restart:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >26:
       shift=shift % 26
    
    caesar(text,shift,direction)
    restart_prompt = input("Do you want to go again(Yes/No)? ").lower()
    if restart_prompt == "no":
        restart = False
        print("Good Bye!")

