
# Provides calculation functions for different tax and fiscal operations.
# Will include methods for VAT, income tax, and other related computations.

class TaxCalculator:
    def __init__(self):
        self.iva_rate = 21

    def calculate_iva(self, base_amount, iva_rate):
        iva_amount = base_amount * iva_rate
        return iva_amount

    def calculate_irpf(self, gross_income, irpf_rate):
        irpf_amount = gross_income * (irpf_rate / 100)
        return irpf_amount 