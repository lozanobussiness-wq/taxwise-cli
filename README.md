# 💼 TaxWise CLI

**TaxWise CLI** is a command-line assistant for self-employed individuals and employees in Spain. It helps you calculate VAT, IRPF, and Net Income, and includes a simple FAQ bot for common tax-related questions.

> ⚠️ This is a personal learning project built in Python. It simulates real tax logic and language but should not be used for legal or financial advice.

---

## ✨ Features

### 📊 Tax Calculators

- Calculate VAT (21% fixed rate).
- Calculate IRPF (user-defined rate).
- Net income for freelancers (with IRPF and fixed SS quota).
- Net income for employees (IRPF + standard payroll deductions).

### 🤖 Tax FAQ Assistant

- Enter a keyword like `iva`, `employee`, or `freelancer`.
- The assistant returns a brief explanation.
- If no exact match is found, it offers suggestions.
- Supports aliases (e.g. `value added tax` → `iva`, `salary` → `employee`).

---

## 🧪 Example Flow


~~~~~~~~~~~~~~
  TAXWISE CLI
~~~~~~~~~~~~~~

========== OPTION MENU ==========
Choose an option:
1. Calculate VAT (IVA) only
2. Calculate IRPF only
3. Calculate Net Income (Freelancer)
4. Calculate Net Income (Employee)
5. Tax FAQ Assistant
6. Exit

Option (1–6): 2

Enter your gross income: 2000  
Enter your IRPF rate (%): 15

Your gross income is: 2000.0 €  
Your IRPF retention is: 300.0 €  
---------------------------------
Net income after IRPF: 1700.0 €

Press Enter to return to the menu...

Option (1–6): 5

--- TAX FAQ ASSISTANT ---
Available topics:
- IVA
- IRPF
- Freelancer
- Employee
- Invoice
- Deductions

Type a topic or keyword to get information, or 'exit' to return to the main menu.

> What is salary?

Topic not found. Did you mean:  
 - employee  
 - freelancer  

Tip: Type 'help' to view all available topics again.
```

---

## 🔧 Tech Stack

- **Python 3.x**
- Pure CLI (no external dependencies)
- Modular structure:
  - `main.py`: main loop and user interface
  - `calculators.py`: tax logic
  - `bot.py`: FAQ assistant

---

## 🚧 Future Improvements

This project is part of a learning roadmap. Planned improvements include:

### ✅ Short-term
- Input validation and error handling  
- Improve formatting and decimal precision  
- Save/load data from `.txt` or `.json`  
- Persistent user preferences

### 🌐 Mid-term
- Export to CSV or PDF  
- Use JSON for FAQ and aliases  
- Logging user interactions  
- CLI arguments support

### 🚀 Long-term
- Web version (Flask or FastAPI)  
- AI-based assistant via API (OpenAI or local LLM)  
- Real tax API integration  
- Multilingual support (ES/EN)

> *Future implementations are ideas for learning and improvement.*
> *This project is for educational purposes only.*

---

## 📁 Project Structure

```bash
TaxWise/
│
├── main.py             # Entry point and menu interface
├── calculators.py      # Functions for VAT, IRPF, and net income calculations
├── bot.py              # Tax FAQ assistant logic and data
└── README.md           # Project documentation
```

---

## 🧠 Learning Goals

This project helped me practice and understand:

- How to structure CLI projects using Python modules.
- Basic input handling, loops, and menus.
- Using dictionaries, lists, and mappings for logic.
- Writing clean output and improving CLI UX.
- Designing small assistants using keywords and alias mapping.

---

## 👨‍💻 Author

Created by Miguel Lozano as a final project for the Codedex Python Beginner Course.

## 📜 License

This project is licensed under the MIT License.  
You are free to use, copy, modify, and distribute this project with attribution.  

Copyright © 2025 [Miguel Lozano]