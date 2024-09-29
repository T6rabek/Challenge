import os


expenses = []
categories = []
names = []
full_list = []
total = 0

def save_data():
    data = ''

    for i in range(len(expenses)):
        data += f"{expenses[i]} | {names[i]} | {categories[i]}\n"

    with open("list.txt", "w") as file:
        file.write(data)



def load_data():
    if os.path.exists("list.txt"):
        with open("list.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                category, name, expense = line.strip().split(" | ")
                categories.append(category)
                names.append(name)
                expenses.append(float(expense))






def add_expense():
    try:
        price = float(input("Enter the price of the product: "))
        expenses.append(price)
    except Exception:
        print("Something went wrong")

def name_spending():
    spending = input("Enter the name of the spending: ")
    names.append(spending)
def filter_category():
    cate = input("Enter the category you want to put your spending into: ")
    categories.append(cate)
def show_list():
    print(f"{expenses} | {names} | {categories}")
def view_expenses():
    for expense in expenses:
        print(expense)
def total_money():
    global total
    total = 0
    for i in expenses:
        total = total + i
        print(total)
def filtering():
    for category in categories:
        print(category, end=" | ")
def delete_expense():
    choice = input("Enter the name of category you want to delete: ")
    categories.remove(choice)
def main():
    while True:
        try:
            options = int(input("Choose an option: \n1. Add expense\n2. View all expenses\n3. Filter by category\n4. View total spendings\n5. Delete expense\n6. Save and quit | "))
        except ValueError:
            print("There was an issue with the type. Please enter only numbers!")
            continue

        if options == 1:

            add_expense()
            filter_category()
            name_spending()
            show_list()

        elif options == 2:
            view_expenses()

        elif options == 3:
            filtering()

        elif options == 4:
            total_money()

        elif options == 5:
            delete_expense()

        elif options == 6:
            save_data()
            load_data()
            break

        else:
            print("Please, enter a valid option!")







if __name__ == "__main__":
    main()


