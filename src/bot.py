
# Contains the core logic for the TaxWise CLI assistant.
# This will process user inputs and return responses based on tax-related queries.

class TaxBot:

    def __init__(self):
        self.faqs = {
            "iva": "IVA is a 21% tax on goods and services. Basic necessities may have reduced rates of 10% or 4%.",
            "irpf": "IRPF is the personal income tax. Employees have withholding on salary, and self-employed usually pay 7%-19% in advance.",
            "autonomo": "Self-employed must pay a fixed monthly social security fee (≈294€ minimum in 2025) plus quarterly taxes.",
            "employee": "Employees have automatic withholdings on salary: IRPF + social security + unemployment + training.",
            "deadlines": "Quarterly taxes are due on Jan 20, Apr 20, Jul 20, and Oct 20. Annual IRPF is filed May-June.",
            "deductions": "Business expenses (equipment, office, transport) can reduce taxable income. Keep all receipts!",
            "invoices": "Invoices must include date, invoice number, tax ID, description, base amount, IVA, and total.",
            "rates": "Current tax rates: IVA 21%. IRPF ranges approx. 7%-19% for self-employed, progressive for employees.",
            "expenses": "Common deductible expenses: office supplies, coworking space, professional services, transport, phone/internet.",
            "neto": "Net income is calculated as gross income minus IRPF and mandatory deductions (social security, etc.)."
    }


        self.aliases = {
            "vat": "iva",
            "value added tax": "iva",
            "income tax": "irpf",
            "withholding": "irpf",
            "freelancer": "autonomo",
            "self-employed": "autonomo",
            "worker": "employee",
            "salary": "employee",
            "dates": "deadlines",
            "due dates": "deadlines",
            "write-off": "deductions",
            "deductible": "deductions",
            "bills": "invoices",
            "receipts": "invoices",
            "costs": "expenses",
            "spending": "expenses",
            "net income": "neto",
            "take-home": "neto"
        }

        self.more_info = {
            "iva": "Official guide: Agencia Tributaria - IVA",
            "irpf": "Official guide: Agencia Tributaria - IRPF",
            "autonomo": "Social Security - Self-employed (Régimen Especial de Trabajadores Autónomos)",
            "deadlines": "Agencia Tributaria - Tax calendar",
            "deductions": "Agencia Tributaria - Deductions overview",
            "invoices": "Agencia Tributaria - Facturación (invoices)",
            "expenses": "Agencia Tributaria - Gastos deducibles",
            "rates": "Agencia Tributaria - Types and rates",
            "employee": "Social Security - Contributions for employees",
            "neto": "Overview: Net vs. gross income (IRPF + payroll deductions)"
        }


    def get_topics(self):
        return list(self.faqs.keys())

    def show_topics(self):
        topics = self.get_topics()
        print("\nAvailable topics:\n")
        print(" | ".join(topics))
        print("\nExample: 'What is IRPF?' or 'Explain freelancer'\n")

    def get_faq(self, topic):
        topic = topic.lower().strip()

        # Search for alias first
        if topic in self.aliases:
            topic = self.aliases[topic]

        # Check if exact topic exists
        if topic in self.faqs:
            print(f"\n🔹 {topic.upper()}:\n{self.faqs[topic]}")
            if topic in self.more_info:
                print(f"📌 For more info:")
                print(f"{self.more_info[topic]}")
            return
        
        # If no exact match, check for partial matches
        for key in self.faqs.keys():
            if key in topic:
                print(f"\n🔹 {key.upper()}:\n{self.faqs[key]}")
                if key in self.more_info:
                    print(f"📌 For more info:")
                    print(f"{self.more_info[key]}")
                return 
                   
        # If no matches found, suggest similar topics
        print(self.suggest(topic))

    def suggest(self, invalid_topic):
        topic = invalid_topic.lower()
        suggestions = []

        # Check for partial matches in topics
        for t in self.get_topics():
            if topic in t:
                suggestions.append(t)

        # Check for aliases that match the topic
        for alias in self.aliases.keys():
            if topic in alias and self.aliases[alias] not in suggestions:
                suggestions.append(self.aliases[alias])

        # If suggestions found, return them
        if suggestions:
            return f"Did you mean: {', '.join(suggestions)}?"
        else:
            return f"❌ Topic not found. Try one of these: {', '.join(sorted(self.get_topics())[:3])}..."

     