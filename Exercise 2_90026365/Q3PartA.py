# This function takes a direction and a position and returns the new position
def move_direction(direction, x, y):
    if x < 0 or y < 0 or x > 7 or y > 7:
        raise ValueError('Invalid position')
    if direction == 'N':
        y -= 1
    elif direction == 'S':
        y += 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    elif direction == 'NE':
        x += 1
        y -= 1
    elif direction == 'NW':
        x -= 1
        y -= 1
    elif direction == 'SE':
        x += 1
        y += 1
    elif direction == 'SW':
        x -= 1
        y += 1
    else:
        raise ValueError('Invalid direction')
    return x, y