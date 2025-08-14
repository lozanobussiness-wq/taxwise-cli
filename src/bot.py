
# Contains the core logic for the TaxWise CLI assistant.
# This will process user inputs and return responses based on tax-related queries.

class TaxBot:

    def __init__(self):
        self.faqs = {
            "iva": "IVA is 21% tax on goods and services. Basic necessities have 10% or 4% rates.",
            "irpf": "IRPF is personal income tax. Self-employed typically pay 7%, 15% or 19% withholding.",
            "autonomo": "Self-employed must pay monthly fee (294€) and quarterly taxes.",
            "deadlines": "Quarterly taxes due: Jan 20, Apr 20, Jul 20, Oct 20. Annual IRPF: May-June.",
            "deductions": "Business expenses can reduce your taxable income. Keep all receipts!",
            "rates": "Current tax rates: IVA 21%, IRPF 7-19% for self-employed"
        }

        

   