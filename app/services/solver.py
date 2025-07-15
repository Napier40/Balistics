import math

def calculate_trajectory(initial_velocity, angle):
    """
    Calculates the trajectory of a projectile.

    Args:
        initial_velocity: The initial velocity of the projectile in m/s.
        angle: The angle of the projectile in degrees.

    Returns:
        A list of tuples, where each tuple contains the x and y coordinates of the projectile at a given time.
    """
    g = 9.81
    angle_rad = math.radians(angle)
    t_flight = (2 * initial_velocity * math.sin(angle_rad)) / g
    trajectory = []
    for t in range(0, int(t_flight) + 1):
        x = initial_velocity * math.cos(angle_rad) * t
        y = initial_velocity * math.sin(angle_rad) * t - 0.5 * g * t**2
        if y >= 0:
            trajectory.append((x, y))
    return trajectory