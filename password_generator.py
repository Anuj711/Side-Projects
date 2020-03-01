import random, sys, os, string


def main():
    ask_user()


def ask_user():
    print(
        "How strong do you want the password to be?\n For a weak password, press 1.\n For a medium password press "
        "2.\n For a "
        "strong password press 3")
    choice1 = int(input())
    if choice1 == 1:
        weak(choice1)
    elif choice1 == 2:
        medium(choice1)
    elif choice1 == 3:
        strong(choice1)
    else:
        ask_user()


def weak(strength_choice):
    weak_list = [random.choice(string.ascii_lowercase) for x in range(0, 6)]
    password = ""
    print_password(password.join(weak_list), strength_choice)


def medium(strength_choice):
    print("How many characters would you like to make the password?")
    num_characters = int(input())
    medium_list = [random.choice(string.ascii_letters) for x in range(0, num_characters)]
    password = ""
    print_password(password.join(medium_list),strength_choice)


def strong(strength_choice):
    print("Would you like to make this password based on total number of characters, or the different numbers of "
          "letters "
          ", numbers, and symbols?\n For the first option, press 1.\n For the second option press 2.\n")
    option = int(input())
    if option == 1:
        print("How many total characters would you like to make the password?")
        total_num_characters = int(input())
        num_characters = int(total_num_characters/3)
        strong_numbers_list = [str(random.randint(0, 9)) for x in range(0, num_characters)]
        strong_strings_list = [random.choice(string.ascii_letters) for x in
                               range(0, num_characters)]
        symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '<', '>', '~']
        random.shuffle(symbols_list)
        strong_symbols_list = [random.choice(symbols_list) for x in range(0, num_characters)]
        strong_list = strong_symbols_list + strong_strings_list + strong_numbers_list
        remainder = 0
        if total_num_characters % 3 != 0:
            remainder = total_num_characters % 3
        x = 0;
        if (len(strong_list)) != total_num_characters:
            while x < remainder:
                strong_list.append(random.choice(string.ascii_letters))
                x += 1
    elif option == 2:
        print("How many letters would you like in your password?")
        num_letters = int(input())
        print("How many numbers would you like in your password?")
        num_numbers = int(input())
        print("How many symbols would you like in your password?")
        num_symbols = int(input())
        strong_numbers_list = [str(random.randint(0, 9)) for x in range(0, num_numbers)]
        strong_strings_list = [random.choice(string.ascii_letters) for x in
                               range(0, num_letters)]
        symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '<', '>', '~']
        random.shuffle(symbols_list)
        strong_symbols_list = [random.choice(symbols_list) for x in range(0, num_symbols)]
        strong_list = strong_symbols_list + strong_strings_list + strong_numbers_list

    random.shuffle(strong_list)
    password = ""
    print_password(password.join(strong_list),strength_choice)


def print_password(password,strength_choice):
    print("Your password is:", password)
    with open("passwords.txt","a+") as password_file:
        password_file.write(password + "\n")
    password_file.close()
    post_password(strength_choice, password_file)
    

def post_password(strength_choice, password_file):
    print("\nIf you would like a different password of the same strength press 1.\nIf you would like a password of "
          "different strength press 2.\nPress 3 to see all the previous passwords that have been generated for you.\n"
          "Otherwise, press 4 to exit the program")
    choice = int(input())
    if choice == 1:
        if strength_choice == 1:
            weak(strength_choice)
        elif strength_choice == 2:
            medium(strength_choice)
        elif strength_choice == 3:
            strong(strength_choice)
    elif choice == 2:
        ask_user()
    elif choice == 3:
        password_file = open("passwords.txt","r+")
        if password_file.mode == "r+":
            contents = password_file.read()
            print(contents)
        post_password(strength_choice,password_file)
    elif choice == 4:
        exit()
    else:
        print("Sorry try a valid input.")
        post_password()


main()

