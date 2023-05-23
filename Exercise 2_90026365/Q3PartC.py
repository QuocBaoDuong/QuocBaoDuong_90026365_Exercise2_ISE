# This program calculates the number of pies each person gets and the number of leftover pies
def pie_divider():
    # Get the number of people
    num_people = int(input())

    # Get the number of pies
    num_pies = int(input())

    while num_pies < 0 or num_people < 1:
        print("Invalid")
        num_people = int(input())
        num_pies = int(input())

    # Calculate the number of pies each person gets
    pies_per_person = num_pies // num_people

    # Calculate the number of leftover pies
    leftover_pies = num_pies % num_people

    # Print the number of pies each person gets
    print(pies_per_person)

    # Print the number of leftover pies
    print(leftover_pies)

    if leftover_pies == 0:
        print("Perfect")