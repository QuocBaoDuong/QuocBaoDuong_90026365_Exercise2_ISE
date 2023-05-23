def fastest_racer(name_one, name_two, top_speed_one, top_speed_two, acceleration_one, acceleration_two): 
    # This function takes in the top speed and acceleration of two racers and returns the name of the racer that hits their top speed fastest
    # If both racers reach their top speed at the same time, the function returns "Tie"
    # If the inputs are invalid, the function returns "Invalid Input"

    # Check if the inputs are valid
    if top_speed_one <= 0 or top_speed_two <= 0 or acceleration_one <= 0 or acceleration_two <= 0:
        return "Invalid Input"
    
    # Calculate the time taken for each racer to reach their top speed
    time_one = top_speed_one / acceleration_one
    time_two = top_speed_two / acceleration_two

    # Check which racer is faster
    if time_one < time_two:
        return name_one
    elif time_two < time_one:
        return name_two
    else:
        return "Tie"
    
    