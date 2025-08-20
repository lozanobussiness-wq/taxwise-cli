
# Provides calculation functions for different tax and fiscal operations.
# Will include methods for VAT, income tax, and other related computations.

class TaxCalculator:
    def __init__(self):
        self.iva_rate = 21
# Calculates IVA (Value Added Tax) based on base amount and rate.
    def calculate_iva(self, base_amount):
        iva_amount = base_amount * 0.21
        return iva_amount
# Calculates IRPF (personal income tax) based on gross income and rate.
    def calculate_irpf(self, gross_income, irpf_rate):
        irpf_amount = gross_income * (irpf_rate / 100)
        return irpf_amount 
    
    #  Calculates standard employee deductions based on gross income.
    # Includes:
    #   - Social Security (SS): 4.7%
    #   - Unemployment insurance: 1.55%
    #   - Job training: 0.1%
    #   - Intergenerational Equity Mechanism (MEI): 0.7%   
    def calculate_additional_deductions(self, gross_income):

        social_security = gross_income * 0.047
        unemployment = gross_income * 0.0155
        training = gross_income * 0.001
        mei = gross_income * 0.007

        total_deductions = social_security + unemployment + training + mei
        return total_deductions
    # Calculates net income for freelancers
    def calculate_net_income_freelancer(self, gross_income, irpf_rate):
        irpf = self.calculate_irpf(gross_income, irpf_rate)
        return gross_income - irpf
    
    # Calculates net income for employees
    def calculate_net_income_employee(self, gross_income, irpf_rate):
        irpf = self.calculate_irpf(gross_income, irpf_rate)
        other_deductions = self.calculate_additional_deductions(gross_income)
        return gross_income - irpf - other_deductions