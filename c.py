class Calculator:
    def options(self):
        print(
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "5. Modulus\n"
            "6. Exponentiation\n"
            "7. Floor Division"
        )

    def choice(self, ch, a, b):
        operations = {
            1: a + b,
            2: a - b,
            3: a * b,
            4: a / b if b != 0 else 'Error: Division by zero',
            5: a % b,
            6: a ** b,
            7: a // b if b != 0 else 'Error: Division by zero'
        }
        return operations.get(ch, 'Invalid choice')

c = Calculator()
c.options()
try:
    ch = int(input("Enter your choice (1,2,3,4,5,6,7): "))
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = c.choice(ch, a, b)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")
