from pymongo import MongoClient

# Connect to MongoDB (local or Atlas URL)
client = MongoClient("mongodb://localhost:27017/")      #connect to the local server
db = client["expense_tracker"]      #create a db
expenses_collection = db["expenses"]        #create a collection named "expenses"



def add_expense(date, category, amount, description):
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses_collection.insert_one(expense)
    print("Expense added successfully!")


def get_expenses():
    ###
    ###
    pass
    print("Here are the expenses!")


def update_expense(expense_id, new_data):
    ###
    ###
    pass
    print("Expense updated successfully!")


def delete_expense(expense_id):
    ###
    ###
    pass
    print("Expense deleted successfully!")


def get_total_by_category():
    pass

def get_expenses_by_date_range(start_date, end_date):
    pass


while True:
    print("The Expense Tracker")
    print("-------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(date, category, amount, description)

    elif choice == "2":
        pass

    ###

    elif choice == '5':
        print("Exiting the program...")
        break
    
    else:
        print("Invalid choice. Please select a number between 1 and 5.")