import logging

# Basic config
logging.basicConfig(
    filename="app.log",        # Log file
    filemode="a",              # Append mode
    level=logging.DEBUG,       # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    num = int("abc")
except ValueError:
    logging.error("Tried to convert a non-numeric string to int", exc_info=True)

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = input("Enter the operation to perform- +,-,*,/")


while True:
    def calculator():
        match c:
            case "+":
                print(a + b)
            case "-":
                print(a - b)
            case "*":
                print(a * b)
            case "/":
                if b != 0:
                    print(a / b)
                else:
                    logging.error("Error! Division by zero is not allowed")
            case _:
                logging.warning("Invalid operation")
    calculator()
        

                
logging.info("Program completed")