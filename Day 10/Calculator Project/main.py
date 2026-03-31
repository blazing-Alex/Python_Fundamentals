import art

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(art.logo)

    should_continue = True
    num1 = float(input("What is the first number: "))
    while should_continue:
        for op in operations:
            print(op)
        input_operation = input("What is the operation: ")
        num2 = float(input("What is the second number: "))
        answer = operations[input_operation](num1, num2)
        print(f"{num1} {input_operation} {num2} = {answer}")

        choice = input(f"Type y to continue with {answer}, or type n to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()