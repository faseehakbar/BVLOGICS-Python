from datetime import datetime


class FinanceTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.budgets = {}
        self.investments = []
        self.categories = []

    def set_expense_categories(self, categories):
        self.categories = categories

    def add_income(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid income amount. Please enter a number.")
        self.income += amount

    def add_expense(self, category, amount, description):
        if self.income == 0:
            print(
                "You have not added any income yet. Please add income before adding expenses.")
            return
        if category not in self.categories:
            raise ValueError(
                f"Invalid expense category: {category}. Please choose from: {', '.join(self.categories)}")
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Expense amount must be a positive number.")
        except ValueError:
            raise ValueError(
                "Invalid expense amount. Please enter a valid number.")
        self.expenses.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'category': category,
            'amount': amount,
            'description': description
        })
        print("Expense added successfully!")

    def set_budget(self, category, limit):
        if self.income == 0:
            print(
                "You have not added any income yet. Please add income before setting budget.")
            return
        if category not in self.categories:
            raise ValueError(
                f"Invalid budget category: {category}. Please choose from: {', '.join(self.categories)}")
        try:
            limit = float(limit)
            if limit <= 0:
                raise ValueError("Budget limit must be a positive number.")
        except ValueError:
            raise ValueError(
                "Invalid budget limit. Please enter a valid number.")
        self.budgets[category] = limit
        print(f"Budget limit set successfully for {category}: {limit}")
        print("budget set successfully:")

    def add_investment(self, asset, amount, type):
        if self.income == 0:
            print(
                "You have not added any income yet. Please add income before adding investment.")
            return
        self.investments.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'asset': asset,
            'amount': amount,
            'type': type
        })

    def save_data(self, filename='finance_data.txt'):
        if self.income == 0:
            print(
                "You have not added any income yet. Please add income before saving data.")
            return
        with open(filename, 'a') as file:
            file.write(f"Income: {self.income}\n")
            file.write("Expenses:\n")
            for expense in self.expenses:
                file.write(
                    f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}\n")
            file.write("Budgets:\n")
            for category, limit in self.budgets.items():
                file.write(f"{category}, {limit}\n")
            file.write("Investments:\n")
            for investment in self.investments:
                file.write(
                    f"{investment['date']}, {investment['asset']}, {investment['amount']}, {investment['type']}\n")

    def load_data(self, filename='finance_data.txt'):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.income = float(lines[0].split(": ")[1])

            self.expenses = []
            expense_start = lines.index("Expenses:\n") + 1
            expense_end = lines.index("Budgets:\n")
            for line in lines[expense_start:expense_end]:
                parts = line.strip().split(", ")
                self.expenses.append(
                    (parts[0], parts[1], float(parts[2]), parts[3]))

            self.budgets = {}
            budget_start = lines.index("Budgets:\n") + 1
            budget_end = lines.index("Investments:\n")
            for line in lines[budget_start:budget_end]:
                parts = line.strip().split(", ")
                self.budgets[parts[0]] = float(parts[1])

            self.investments = []
            investment_start = lines.index("Investments:\n") + 1
            for line in lines[investment_start:]:
                parts = line.strip().split(", ")
                self.investments.append(
                    (parts[0], parts[1], float(parts[2]), parts[3]))

    def check_budget_alert(self):
        for category, limit in self.budgets.items():
            total_expense = sum(
                expense['amount'] for expense in self.expenses if expense['category'] == category)
            if total_expense >= limit:
                print(
                    f"Alert: Budget limit exceeded for {category}. Total expense: {total_expense}, Budget limit: {limit}")
            elif total_expense >= 0.8 * limit:
                print(
                    f"Warning: Approaching budget limit for {category}. Total expense: {total_expense}, Budget limit: {limit}")

    def get_income_report(self):
        print("Income Report:")
        print(f"Total Income: {self.income}")

    def get_expense_report(self, category=None):
        print("Expense Report:")
        if category:
            if category not in self.categories:
                raise ValueError(
                    f"Invalid expense category: {category}. Please choose from: {', '.join(self.categories)}")
            filtered_expenses = [
                expense for expense in self.expenses if expense['category'] == category]
            total_expense = sum(expense['amount']
                                for expense in filtered_expenses)
            print(f"Category: {category}")
            print(f"Total Expense: {total_expense}")
            # You can add further details about expenses in this category here
        else:
            print("By Category:")
            for category in self.categories:
                filtered_expenses = [
                    expense for expense in self.expenses if expense['category'] == category]
                total_expense = sum(expense['amount']
                                    for expense in filtered_expenses)
                print(f"- {category}: {total_expense}")

    def get_budget_report(self):
        print("Budget Report:")
        for category, limit in self.budgets.items():
            total_expense = sum(
                expense['amount'] for expense in self.expenses if expense['category'] == category)
            remaining = limit - total_expense
            print(f"- {category}:")
            print(f"  * Budget Limit: {limit}")
            print(f"  * Total Expense: {total_expense}")
            print(f"  * Remaining: {remaining}")

    def get_investment_report(self):
        print("Investment Report:")
        # Implement report logic for investments
        # ...

# Function to display menu and get user input


def display_menu():
    print("===== Finance Tracker Menu =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Set Budget")
    print("4. Add Investment")
    print("5. Save Data")
    print("6. View Summary")
    print("     6.1 Income Report")
    print("     6.2 Expense Report (by category)")
    print("     6.3 Expense Report (all categories)")
    print("7. Exit")
    choice = input("Enter your choice: ")
    return choice


# Usage example with user input and error handling
tracker = FinanceTracker()
tracker.set_expense_categories(['food', 'housing', 'utilities'])
while True:
    choice = display_menu()
    if choice == '1':
        try:
            amount = float(input("Enter income amount: "))
            tracker.add_income(amount)
            print("Income added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '2':
        category = input("Enter expense category(food,housing,utilities): ")
        try:
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(category, amount, description)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '3':
        category = input("Enter budget category: ")
        try:
            limit = float(input("Enter budget limit: "))
            tracker.set_budget(category, limit)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '4':
        asset = input("Enter asset name: ")
        try:
            amount = float(input("Enter investment amount: "))
            investment_type = input("Enter investment type: ")
            tracker.add_investment(asset, amount, investment_type)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '5':
        tracker.save_data()
        print("Data saved successfully!")
        tracker.check_budget_alert()
    elif choice == '6':
        print("===== Financial Summary =====")
        print(f"Income: {tracker.income}")
        print("Expenses:")
        for expense in tracker.expenses:
            print(
                f"- {expense['category']}: {expense['amount']} ({expense['descriptiton']})")
        print("Budgets:")
        for category, limit in tracker.budgets.items():
            print(f"- {category}: {limit}")
        print("Investments:")
        for investment in tracker.investments:
            print(
                f"- {investment['asset']}: {investment['amount']} ({investment['type']})")
    elif choice == '6.1':
        tracker.get_income_report()  # Call to display income report
    elif choice == '6.2':
        category = input("Enter expense category:")
        tracker.get_expense_report(category)  # Call with optional category
    elif choice == '6.3':
        tracker.get_expense_report()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
