
# Main entry point for the TaxWise CLI project.
# This file will handle the main program loop and user interaction

from calculators import TaxCalculator as TC
from bot import TaxBot as TB   

class TaxWiseCLI:
    def __init__(self):
        self.calculator = TC()
        self.bot = TB()

    def show_welcome(self):
        print("=" * 40)
        print("Welcome to TaxWise CLI!")
        print("Your personal tax assistant.")
        print("=" * 40)
    
    def show_menu(self):
        print("========== OPTION MENU ==========")
        print("Choose an option:")
        print("1. Calculate VAT (IVA) only")
        print("2. Calculate IRPF only")
        print("3. Calculate Net Income(Freelancer)")
        print("4. Calculate Net Income (Employee)")
        print("5. Tax FAQ Assistant")
        print("6. Exit")
        print("-" * 30)
# Checks if the input is a number
    def is_number(self, text):
        text = text.replace(".", "", 1)
        return text.isdigit()
    
    def option_calculate_iva(self):
        print("\n🔹 VAT Calculator (IVA - 21%)")
        amount = input("Base amount: ")
        if self.is_number(amount):
            amount = float(amount)
            iva = self.calculator.calculate_iva(amount)
            print(f"   Base Amount: {amount:.2f}€")
            print(f"   IVA Amount: {iva:.2f}€")
            print(f"   Total Amount (with IVA): {amount + iva:.2f}€")
        else:
            print("Invalid input. Please enter a valid number.")
        input("Press Enter to continue...")

    def option_calculate_irpf(self):
        print("\n🔹 IRPF Calculator")
        income = input("Gross income: ")
        rate = input("IRPF rate (default 17%): ")
        if self.is_number(income) and self.is_number(rate):
            income = float(income)
            rate = float(rate)
            irpf = self.calculator.calculate_irpf(income, rate)
            print(f"   Gross Income: {income:.2f}€")
            print(f"   IRPF Amount: {irpf:.2f}€")
        else:
            print("Invalid input. Please enter valid numbers.")
        input("Press Enter to continue...")

    def option_calculate_net_income_freelancer(self):
        print("\n🔹 Net Income Calculator (Freelancer)")
        income = input("Gross income: ")
        rate = input("IRPF rate: ")
        if self.is_number(income) and self.is_number(rate):
            income = float(income)
            rate = float(rate)
            net_income = self.calculator.calculate_net_income_freelancer(income, rate)
            print(f"   Gross Income: {income:.2f}€")
            print(f"   Net Income (after IRPF): {net_income:.2f}€")
        else:
            print("Invalid input. Please enter valid numbers.")
        input("Press Enter to continue...")

    def option_calculate_net_income_employee(self):
        print("\n🔹 Net Income Calculator (Employee)")
        income = input("Gross income: ")
        rate = input("IRPF rate: ")
        if self.is_number(income) and self.is_number(rate):
            income = float(income)
            rate = float(rate)
            net_income = self.calculator.calculate_net_income_employee(income, rate)
            irpf = self.calculator.calculate_irpf(income, rate)
            other_deductions = self.calculator.calculate_additional_deductions(income)
            print(f"   Gross Income: {income:.2f}€")
            print(f"   IRPF Deduction ({rate}%): {irpf:.2f}€")
            print(f"   Other Deductions (SS, unemployment, training, MEI): {other_deductions:.2f}€")
            print(f"   Net Income (after all deductions): {net_income:.2f}€")
            input("Press Enter to see breakdown details...")
            print("   Note:")
            print("      - Social Security (SS): 4.7%")
            print("      - Unemployment Insurance: 1.55%")
            print("      - Job Training: 0.1%")
            print("      - Intergenerational Equity Mechanism (MEI): 0.7%")
        else:
            print("Invalid input. Please enter valid numbers.")
        input("Press Enter to continue...")       


    def option_use_faq_assistant(self):
        print("\n--- FAQ Assistant ---")
        print("Type a topic or keyword to get information.")
        print("Type 'help' to see available topics again or 'exit' to return to the main menu.")
        self.bot.show_topics()
        while True:
            topic = input("Enter a topic or keyword ('help' for topics, 'exit' to return): ").strip()
            if topic.lower() == "exit":
                break
            elif topic.lower() == "help":
                self.bot.show_topics()
                continue
            self.bot.get_faq(topic)
            print("\n")
        

    def run_taxwise(self):
       self.show_welcome()

       while True:
        print()  
        self.show_menu()
        option = input("Select an option (1-6): ")

        if option == "1":
            self.option_calculate_iva()
            print("\n")
        elif option == "2":
            self.option_calculate_irpf()
            print("\n")
        elif option == "3":
            self.option_calculate_net_income_freelancer()
            print("\n")
        elif option == "4":
            self.option_calculate_net_income_employee() 
            print("\n")
        elif option == "5":
            self.option_use_faq_assistant()
            print("\n")
        elif option == "6":
            print("Exiting TaxWise CLI. Goodbye!")
            break
        else:
            print("Please select a valid option (1-6).")
            input("\nPress Enter to continue...")
            print()              

        

app = TaxWiseCLI()
app.run_taxwise()    