def times_or_divide(num_one, num_two, operation):
    if operation == "*":
        return num_one * num_two
    elif operation == "/":
        return num_one / num_two
    else:
        raise ValueError("Invalid operation")

def add_or_subtract(num_one, num_two, operation):
    if operation == "+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    else:
        raise ValueError("Invalid operation")

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

    if operation == "*" or operation == "/":
        result = times_or_divide(num_one, num_two, operation)
    elif operation == "+" or operation == "-":
        result = add_or_subtract(num_one, num_two, operation)
    else:
        print("Invalid input")
        return

    print(result)

def main():
    while True:
        calculate()
        print("Do you want to calculate again? (y/n)")
        if input() != "y":
            break
    print("Goodbye")

if __name__ == "__main__":
    main()