import tkinter as tk
from tkinter import messagebox, simpledialog, font
from datetime import datetime
import json
from PIL import Image, ImageTk
import random


class BudgetApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Budgeting App")
        self.root.geometry('1750x1000')
        self.transactions = {}  # Dictionary to store transactions for each name

        # Load and display background image
        self.set_background_image("Blog-Banner.jpg")

        # Create login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.place(x=400,y=200,height=300)

        opening_label = tk.Label(self.login_frame, text="MONEY MASTER", font=("Times New Roman", 56, "bold"),
                                 bg="burlywood2")
        custom_font = font.Font(opening_label, opening_label.cget("font"))
        custom_font.configure(underline=True)
        opening_label.configure(font=custom_font)
        opening_label.pack()

        n = tk.Label(self.login_frame, text="(YOUR PERSONAL FINANCE MANAGER)", font=("Georgia", 15, "italic"),
                     bg="burlywood3")
        n.pack()

        self.username_label = tk.Label(self.login_frame, text="Username:", font=("Times", 15, "bold italic"),
                                       bg="burlywood3")
        self.username_label.place(x=85,y=160)
        self.username_entry = tk.Entry(self.login_frame, font=("Times", 15, "bold italic"), width=40)
        self.username_entry.place(x=210,y=160)

        self.password_label = tk.Label(self.login_frame, text="Password:", font=("Times", 15, "bold italic"),
                                       bg="burlywood3")
        self.password_label.place(x=85,y=200)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Times", 15, "bold italic"), width=40)
        self.password_entry.place(x=210,y=200)

        self.login_button = tk.Button(self.login_frame, text="LOGIN", command=self.authenticate_user,
                                      font=("Times", 12, "bold italic"), bg="honeydew4")
        self.login_button.place(x=350,y=250)

    def set_background_image(self, image_path):
        # Load background image and resize it to fit the screen
        background_image = Image.open(image_path)
        background_image = background_image.resize((1750, 1000))
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image and place it in the root window
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy authentication (replace with your authentication logic)
        if username == "Allies" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Allies!")
            self.show_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def show_main_app(self):
        # Destroy login frame
        self.login_frame.destroy()
 


        # Create a frame for the main application window
        self.main_app_frame = tk.Frame(self.root)
        self.main_app_frame.place(x=260,y=0,height=800,width=1000)
        o = tk.Label(self.main_app_frame, text="NOTE :  For Tips, \n right click anywhere on the screen. ",
                     bg="darkgray")
        o.place(x=2,y=720)

        opening_label = tk.Label(self.main_app_frame, text="MONEY MASTER", font=("Times New Roman", 56, "bold"),
                                 bg="burlywood2")
        custom_font = font.Font(opening_label, opening_label.cget("font"))
        custom_font.configure(underline=True)
        opening_label.configure(font=custom_font)
        opening_label.pack()

        n = tk.Label(self.main_app_frame, text="(YOUR PERSONAL FINANCE MANAGER)", font=("Georgia", 15, "italic"),
                     bg="burlywood3")
        n.pack()

 
        self.name_label = tk.Label(self.main_app_frame, text="Name:", font=("Times", 15, "bold italic"),
                                   bg="burlywood3")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.name_entry.pack()

        self.income_label = tk.Label(self.main_app_frame, text="Income:", font=("Times", 15, "bold italic"),
                                     bg="burlywood3")
        self.income_label.pack()
        self.income_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.income_entry.pack()

        self.expense_label = tk.Label(self.main_app_frame, text="Expense:", font=("Times", 15, "bold italic"),
                                      bg="burlywood3")
        self.expense_label.pack()
        self.expense_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.expense_entry.pack()

        self.category_label = tk.Label(self.main_app_frame, text="Category:", font=("Times", 15, "bold italic"),
                                       bg="burlywood3")
        self.category_label.pack()
        self.category_var = tk.StringVar(self.main_app_frame)
        self.category_var.set("Select Category")
        self.category_menu = tk.OptionMenu(self.main_app_frame, self.category_var, "Food", "Transportation", "Housing",
                                           "Utilities", "Entertainment", "Education", "Grocery", "Other")
        self.category_menu.config(width=95)
        self.category_menu.pack()

        self.source_label = tk.Label(self.main_app_frame, text="Source of Income:", font=("Times", 15, "bold italic"),
                                     bg="burlywood3")
        self.source_label.pack()
        self.source_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.source_entry.pack()

        self.savings_goal_button = tk.Button(self.main_app_frame, text="SET SAVING GOAL", command=self.set_savings_goal,
                                             font=("Helvetica", 12, "bold italic"), bg="tan2")
        self.savings_goal_button.place(x=430,y=500)

        self.add_button = tk.Button(self.main_app_frame, text="ADD", command=self.add_transaction,
                                    font=("Times", 12, "bold italic"), bg="honeydew4")
        self.add_button.place(x=480,y=415)

        self.delete_button = tk.Button(self.main_app_frame, text="DELETE", command=self.delete_transaction,
                                       font=("Times", 12, "bold italic"), bg="honeydew4")
        self.delete_button.place(x=430,y=455)

        self.clear_button = tk.Button(self.main_app_frame, text="CLEAR", command=self.clear_transactions,
                                      font=("Times", 12, "bold italic"), bg="honeydew4")
        self.clear_button.place(x=520,y=455)

        self.show_button = tk.Button(self.main_app_frame, text="SHOW DETAILS", command=self.show_details,
                                     font=("Times", 12, "bold italic"), bg="honeydew4")
        self.show_button.place(x=290,y=500)

        self.forecast_button = tk.Button(self.main_app_frame, text="FORECAST", command=self.forecast,
                                         font=("Times", 12, "bold italic"), bg="honeydew4")
        self.forecast_button.place(x=600,y=500)

        self.transactions_label = tk.Label(self.main_app_frame, text="TRANSACTIONS:",
                                           font=("Times", 15, "bold italic"), bg="tan2")
        self.transactions_label.place(x=430,y=545)
        y = tk.Label(self.main_app_frame, text="WANT TO \n ENHANCE \n FINANCIAL VOCAB?", font=("Times", 13, "bold"),
                     bg="thistle3")
        y.place(x=810,y=600)
        play = tk.Button(self.main_app_frame, text="PLAY", font=("Times", 12, "bold italic"), bg="sienna4",
                         command=self.play_word_scramble)
        play.place(x=870,y=690)

        # Add a scrollbar to the transactions text widget
        self.transactions_text_frame = tk.Frame(self.main_app_frame)
        self.transactions_text_frame.place(x=200,y=585)
        self.transactions_text_scrollbar = tk.Scrollbar(self.transactions_text_frame, orient=tk.VERTICAL)
        self.transactions_text = tk.Text(self.transactions_text_frame, height=9, width=65,
                                         font=("Times", 13, "italic"), bg="burlywood2",
                                         yscrollcommand=self.transactions_text_scrollbar.set)
        self.transactions_text_scrollbar.config(command=self.transactions_text.yview)
        self.transactions_text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.transactions_text.pack(side=tk.LEFT, fill=tk.BOTH)

        # Load transactions from file
        self.load_transactions()

        # Budget tips and advice dropdown menu
        self.tips_menu = tk.Menu(root, tearoff=0)
        self.tips_menu.add_command(label="Tip 1: Create a budget plan", command=self.show_tip_1)
        self.tips_menu.add_command(label="Tip 2: Track your expenses", command=self.show_tip_2)
        self.tips_menu.add_command(label="Tip 3: Limit impulse purchases", command=self.show_tip_3)
        self.tips_menu.add_command(label="Tip 4: Use cashback and rewards", command=self.show_tip_4)
        self.tips_menu.add_command(label="Tip 5: Review and adjust your budget regularly", command=self.show_tip_5)

        self.root.bind("<Button-3>", self.show_tips_menu)

        # Add a menu option for setting the savings goal
        self.menu_bar = tk.Menu(root)
        self.menu_bar.add_command(label="Set Savings Goal", command=self.set_savings_goal)
        root.config(menu=self.menu_bar)

    def show_tips_menu(self, event):
        self.tips_menu.post(event.x_root, event.y_root)

    def show_tip_1(self):
        messagebox.showinfo("Tip 1", "Create a budget plan: For your income level, it's important to create a detailed budget plan to manage your expenses effectively.")

    def show_tip_2(self):
        messagebox.showinfo("Tip 2", "Track your expenses: Keep track of all your expenses to understand where your money is going.")

    def show_tip_3(self):
        messagebox.showinfo("Tip 3", "Limit impulse purchases: Avoid making impulse purchases by sticking to your budget plan.")

    def show_tip_4(self):
        messagebox.showinfo("Tip 4", "Use cashback and rewards: Take advantage of cashback offers and rewards programs to save money.")

    def show_tip_5(self):
        messagebox.showinfo("Tip 5", "Review and adjust your budget regularly: Review your budget regularly and make adjustments as needed.")

    def set_savings_goal(self):
        # Prompt the user to input their savings goal amount
        savings_goal = simpledialog.askfloat("Set Savings Goal", "Enter your savings goal amount:")
        if savings_goal is not None:
            self.savings_goal = savings_goal
            messagebox.showinfo("Savings Goal", f"Your savings goal is set to: {savings_goal}")

    def add_transaction(self):
        name = self.name_entry.get()
        income = self.income_entry.get()
        expense = self.expense_entry.get()
        category = self.category_var.get()
        source_of_income = self.source_entry.get()  # Retrieve the source of income

        try:
            income = float(income)
            expense = float(expense)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return

        difference = income - expense

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Calculate net income after deducting tax
        if income > 500000:  # If income exceeds 5 lakhs, deduct 5% tax from the amount exceeding 5 lakhs
            tax_amount = (income - 500000) * 0.05
            net_income = income - tax_amount
        else:
            net_income = income

        # Initialize balance for name if it doesn't exist
        if name not in self.transactions:
            self.transactions[name] = {"balance": 0, "transactions": []}

        self.transactions[name]["balance"] += net_income - expense

        # Check if savings goal is set
        if hasattr(self, 'savings_goal') and self.transactions[name]["balance"] >= self.savings_goal:
            self.transactions[name]["savings_goal"] = "Savings goal met!"
            messagebox.showinfo("Congratulations", f"Congratulations, {name}! You have achieved your savings goal.")
        elif hasattr(self, 'savings_goal') and self.transactions[name]["balance"] < self.savings_goal:
            self.transactions[name]["savings_goal"] = "Savings goal not met!"
            messagebox.showinfo("Savings Goal Update", f"Sorry, {name}. You have not met your savings goal yet.")

        transaction_info = {"timestamp": timestamp, "income": net_income, "expense": expense, "category": category,
                            "source_of_income": source_of_income}  # Include source_of_income in transaction details
        self.transactions[name]["transactions"].append(transaction_info)

        self.update_transaction_display(name, timestamp, net_income, expense, category, source_of_income)  # Pass source_of_income to update_transaction_display

        self.name_entry.delete(0, tk.END)
        self.income_entry.delete(0, tk.END)
        self.expense_entry.delete(0, tk.END)
        self.source_entry.delete(0, tk.END)
        self.category_var.set("Select Category")

        # Save transactions to file
        self.save_transactions()

    def delete_transaction(self):
        name = self.name_entry.get()
        category = self.category_var.get()
        transactions = self.transactions.get(name, {}).get("transactions", [])
        if not transactions:
            messagebox.showerror("Error", "No transactions found for this name")
            return

        for idx, transaction in enumerate(transactions):
            if transaction['category'] == category:
                del self.transactions[name]["transactions"][idx]
                break

        self.update_transaction_display(name)  # Update displayed transactions
        self.save_transactions()  # Save transactions to file

    def clear_transactions(self):
        name = self.name_entry.get()
        if name in self.transactions:
            del self.transactions[name]
            self.update_transaction_display(name)  # Update displayed transactions
            self.save_transactions()  # Save transactions to file

    def highlight_categories(self, event):
        self.category_menu.selection_clear()

    def update_transaction_display(self, name, timestamp=None, income=None, expense=None, category=None,
                                    source_of_income=None):
        if name not in self.transactions:
            return

        self.transactions_text.config(state=tk.NORMAL)  # Enable editing to insert new transactions
        self.transactions_text.delete(1.0, tk.END)  # Clear existing content

        for transaction in self.transactions[name]["transactions"]:
            self.transactions_text.insert(tk.END, f"Name: {name}\n")
            self.transactions_text.insert(tk.END, f"Date & Time: {transaction['timestamp']}\n")
            self.transactions_text.insert(tk.END, f"Income: {transaction['income']}\n")
            self.transactions_text.insert(tk.END, f"Expense: {transaction['expense']}\n")
            self.transactions_text.insert(tk.END, f"Category: {transaction['category']}\n")
            self.transactions_text.insert(tk.END,
                                          f"Source of Income: {transaction['source_of_income']}\n")  # Display source of income
            self.transactions_text.insert(tk.END, "\n" + "-" * 50 + "\n")

        # Scroll to the end of the text widget
        self.transactions_text.see(tk.END)

        self.transactions_text.config(state=tk.DISABLED)  # Disable editing after updating

    def save_transactions(self):
        with open("transactions.json", "w") as file:
            json.dump(self.transactions, file)

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            pass

    def show_details(self):
        name = self.name_entry.get()
        if name in self.transactions:
            messagebox.showinfo("Transaction Details", json.dumps(self.transactions[name], indent=4))
        else:
            messagebox.showerror("Error", "No transactions found for this name")

    def forecast(self):
        # Get user inputs and historical data
        name = self.name_entry.get()
        if name not in self.transactions:
            messagebox.showerror("Error", "No transactions found for this name")
            return

        transactions = self.transactions[name]["transactions"]
        last_balance = self.transactions[name]["balance"]

        # Calculate average income and expense over the last few transactions
        num_transactions = len(transactions)
        total_income = sum(transaction["income"] for transaction in transactions)
        total_expense = sum(transaction["expense"] for transaction in transactions)

        if num_transactions == 0:
            messagebox.showerror("Error", "No transactions found for forecasting")
            return

        avg_income = total_income / num_transactions
        avg_expense = total_expense / num_transactions

        # Calculate average monthly change in income and expense
        monthly_changes_income = [(transactions[i]["income"] - transactions[i - 1]["income"]) for i in
                                  range(1, len(transactions))]
        monthly_changes_expense = [(transactions[i]["expense"] - transactions[i - 1]["expense"]) for i in
                                   range(1, len(transactions))]

        avg_monthly_change_income = sum(monthly_changes_income) / len(
            monthly_changes_income) if monthly_changes_income else 0
        avg_monthly_change_expense = sum(monthly_changes_expense) / len(
            monthly_changes_expense) if monthly_changes_expense else 0

        # Forecast future income, expense, and savings
        num_months = 6  # Number of months for forecasting
        forecast_data = []
        projected_balance = last_balance
        for month in range(1, num_months + 1):
            # Add variability to projected income and expense based on historical trends
            projected_income = max(avg_income + random.uniform(-0.1 * avg_income, 0.1 * avg_income), 0)
            projected_expense = max(avg_expense + random.uniform(-0.1 * avg_expense, 0.1 * avg_expense), 0)

            projected_balance += (projected_income - projected_expense)

            forecast_data.append({
                "Month": month,
                "Projected Income": projected_income,
                "Projected Expense": projected_expense,
                "Projected Balance": projected_balance
            })

        # Display forecast data in a table
        forecast_str = "\n".join([json.dumps(entry, indent=4) for entry in forecast_data])
        messagebox.showinfo("Forecast", forecast_str)

    def play_word_scramble(self):
        word_list = ["income", "expense", "budget", "savings", "balance", "financial", "transaction", "category",
                     "forecast", "expense", "tips", "goal", "details", "forecast"]
        word = random.choice(word_list)
        scrambled_word = ''.join(random.sample(word, len(word)))
        guess = simpledialog.askstring("Word Scramble", f"Unscramble the word: {scrambled_word}")
        if guess == word:
            messagebox.showinfo("Congratulations", "You unscrambled the word correctly!")
        else:
            messagebox.showerror("Incorrect", "Incorrect guess. Better luck next time!")


if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()