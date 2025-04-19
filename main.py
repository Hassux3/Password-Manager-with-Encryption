# Email/Password Saver in Accounts.txt

import time
import string
import os

alphabets = string.ascii_lowercase
def encryption(plain_text, shift_key):
    cypher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_key) % 26
            cypher_text += alphabets[new_position]
        else:
            cypher_text += char
    return cypher_text

def decryption(cypher_text, shift_key):
    decrypted_text = ""
    for char in cypher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position-shift_key) % 26
            decrypted_text += alphabets[new_position]
        else:
            decrypted_text += char
    return decrypted_text

def add():
    email = input("\nEnter your email address: ")
    password = input("Enter your password: ")
    en_email = encryption(email, 7)
    en_pass = encryption(password, 7)
    info = (en_email + "        |        " + en_pass +"\n")
    asking = input("Are you sure about it? (Yes/No) --> ")
    if asking == "Yes" or asking == "yes":
        with open('Accounts.txt', 'a') as f:
            f.write(info)
        print("Your given details has been saved...!\n")
        os.system('cls')
    else:
        print("Please make sure first...!\n")
        os.system('cls')
    
security_passcode = 7666
def accounts_data():
    security = int(input("\nEnter the secret passcode to acces the details:--> "))
    os.system('cls')
    if security == security_passcode:
        print("Here is your details...\n\n\n")
        with open('Accounts.txt', 'r') as f:
            info = f.read()
        decrypted = decryption(info, 7)
        print(decrypted)
        time.sleep(3)
        input("\nPress enter to close this window...! ")

    elif security != security_passcode:
        print("Incorrect passcode!\n")
    else:
        print("Invalid Command!\n")
        return

#Master Password
password = 6777

isnt_logged_in = True
is_on = False

print("\tPassword Manager\n")
#Security checkup...
while isnt_logged_in:
    master_password = int(input("\nEnter master password: "))
    if master_password == password:
        print("Opening...")
        time.sleep(3)
        isnt_logged_in = False
        is_on = True
        os.system('cls')
        print("            Welcome to Python Password Manager            \n\n")
    else:
        print("Incorrect Password...!\n")
        isnt_logged_in = True
        time.sleep(5)
        print("Try again...")
        time.sleep(2)
        os.system('cls')


#After security checkup --> Program will open to use the functions...
while is_on:
    option = input('\n\nWould you like to add a password\nOr to view existing passwords\nOr you want to quit? (add/view/quit)\nEnter your choice: --> ')
    if option == 'add':
        add()
        time.sleep(2)
        os.system('cls')
    elif option == 'view':
        accounts_data()
        time.sleep(2)
        os.system('cls')
    elif option == 'quit':
        asking = input("Are you sure? (Yes/No) --> ")
        if asking == "Yes" or asking == "yes":
            print("Thanks for using our service...!\n")
            break
            isnt_logged_in = False
            is_on = False
        else:
            print("Okay...\n")
            time.sleep(2)
            os.system('cls')
    else:
        print("Invalid Command...!\n")
        time.sleep(2)
        os.system('cls')