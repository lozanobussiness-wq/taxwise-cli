
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
        self.show_welcome()
        print("Choose an option:")
        print("1. Calculate IVA only")
        print("2. Calculate IRPF only")
        print("3. Calculate Net Income")
        print("4. Browse FAQ topics")
        print("5. Search FAQ by keyword")
        print("6. Exit")
        print("-" * 30)

    
    def run_taxwise(self):
       self.show_welcome()  
    

app = TaxWiseCLI()
app.run_taxwise()    