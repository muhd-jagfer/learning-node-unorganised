from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format, please enter the date in dd-mm-yy ")
        return get_date(prompt, allow_default)
    
def get_amount():
    try:
        amount = float(input(" enter a amount : "))
        if amount <= 0:
            raise ValueError(" amount must be a positive digit ")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_catergory():
    category = input("enter the category (I for income or E for expense) : ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid Category, plase enter I fot income and E for expense ")

def get_description():
    return input("Enter a description (optional): ")