import random
import string
from string import ascii_letters
import os



def user_input():
    while True:
        try:
            length = int(input("Enter the length of your password: "))
            if length >= 6:
                break
            else:
                print("Password must have at least 6 symbols!")
        except ValueError:
            print("Please only input numbers!")

    while True:
        try:
            options = input("Enter one of the options:"
                            "\n1. Easy"
                            "\n2. Medium"
                            "\n3. Hard"
                            "\nChoose: ")
            if options == '1':

                combined_options = ascii_letters
                print("Here is your easy password")
            elif options == '2':
                print("Here is your medium password")

                combined_options = ascii_letters + string.digits
            elif options == '3':
                print("Here is your hard password")

                combined_options = ascii_letters + string.punctuation + string.digits

            else:
                print("Please choose one of the options!")
                continue
            break
        except Exception:
            print("Something went wrong")


    return length, combined_options

def generate_password(length, combined_options):
    password = "".join(random.choices(combined_options, k=length))
    return password


def save_password(password):
    with open('password.txt', 'a') as file:
        file.write(password + '\n')



def main():
    choices = int(input("Enter the number:"
                        "\n1. Create password"
                        "\n2. See my passwords"
                        "\nYour choice: "))
    if choices == 1:

        while True:

            length, combined_options = user_input()
            password = generate_password(length, combined_options)
            print(f"-----> {password} <-----")


            choice = input("Do you want to create another password: "
                           "\n1. Yes"
                           "\n2. No"
                           "\nChoice: ")
            try:
                if choice == '1':
                    continue
                elif choice == "2":
                    choice2 = input("Do you want to save your passwords?"
                                    "\n1. Yes"
                                    "\n2. No"
                                    "\nChoice: ")
                    try:
                        if choice2 == '1':
                            save_password(password)
                            print("Your password was saved successfully")
                            break

                        elif choice2 == '2':
                            print("Your password was not saved")
                            break
                        else:
                            print("Please choose one of the options!")
                    except Exception:
                        print("Something went wrong")


                else:
                    print("Please choose one of the options!")
            except Exception:
                print("Something went wrong")




        print("Thank you for choosing us!")


    elif choices == 2:

        if os.path.exists('password.txt'):

            with open('password.txt', 'r') as file:

                passwords = file.read()

                print("Here are your saved passwords:\n" + passwords)

        else:

            print("No passwords saved yet.")


if __name__ == "__main__":
    main()





