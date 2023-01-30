# Determines whether or not a cannonball hits a target.


def get_float(prompt):
    """
    Read a floating point number from user input.

    :param prompt: A string to print before getting a float
    :return: The next float typed by the user
    """
    return float(input(prompt))


def time_of_flight(height):
    """
    Determine how long a cannonball will be in the air.

    :param height: An initial height of a cannonball
    :return: The time the cannonball will be in the air
    """
    return (2 * height / 9.81) ** 0.5


def range_of_shot(time, velocity):
    """
    Determine how far a cannonball will travel.

    :param time: A cannonball's time in the air
    :param velocity: A cannonball's horizontal velocity
    :return: The distance the cannonball will travel
    """
    return time * velocity


def is_hit(shot, distance, width):
    """
    Determine whether or not a cannonball hits a target.

    :param shot: A cannonball's distance traveled
    :param distance: A target's distance from a cannon
    :param width: A target's width
    :return: Whether or not the cannonball hits the target
    """
    return distance <= shot


def main():
    height = get_float("Enter the height of the cannon: ")
    velocity = get_float("Enter the initial velocity of the ball: ")
    distance = get_float("Enter the distance to the target: ")
    width = get_float("Enter the width of the target: ")

    time = time_of_flight(height)
    shot = range_of_shot(time, velocity)
    hit = is_hit(shot, distance, width)

    if hit:
        print("Hit!")
    else:
        print("Miss!")


if __name__ == "__main__":
    main()
