def multiply(num_one, num_two):
    return num_one * num_two

def divide(num_one, num_two):
    return num_one / num_two

def add(num_one, num_two):
    return num_one + num_two

def subtract(num_one, num_two):
    return num_one - num_two

def get_number():
    while True:
        try:
            number = float(input())
            return number
        except ValueError:
            print("Invalid input")

def calculate():
    num_one = get_number()
    operation = input()
    num_two = get_number()

    if operation == "*":
        result = multiply(num_one, num_two)
    elif operation == "/":
        result = divide(num_one, num_two)
    elif operation == "+":
        result = add(num_one, num_two)
    elif operation == "-":
        result = subtract(num_one, num_two)
    else:
        print("Invalid input")
        return

    print(result)

def main():
    while True:
        calculate()
        print("Do you want to calculate again? (y/n)")
        choice = input()
        if choice.lower() != "y":
            break

    print("Goodbye")

if __name__ == "__main__":
    main()
