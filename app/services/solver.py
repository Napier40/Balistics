import math
from .weather import get_weather_data

def calculate_coriolis_force(latitude, velocity):
    """
    Calculates the Coriolis force.

    Args:
        latitude: The latitude in degrees.
        velocity: The velocity of the projectile in m/s.

    Returns:
        The Coriolis force in m/s^2.
    """
    omega = 7.2921159e-5  # Earth's angular velocity
    return 2 * velocity * omega * math.sin(math.radians(latitude))

def calculate_magnus_force(velocity, spin_rate):
    """
    Calculates the Magnus force.

    Args:
        velocity: The velocity of the projectile in m/s.
        spin_rate: The spin rate of the projectile in rad/s.

    Returns:
        The Magnus force in m/s^2.
    """
    # This is a simplified model of the Magnus force.
    # In a real-world application, you would use a more accurate model.
    return 0.5 * 1.225 * 0.04**2 * math.pi * spin_rate * velocity

def calculate_trajectory(initial_velocity, angle, weather_data=None, latitude=None, spin_rate=None):
    """
    Calculates the trajectory of a projectile.

    Args:
        initial_velocity: The initial velocity of the projectile in m/s.
        angle: The angle of the projectile in degrees.
        weather_data: A dictionary containing the weather data.
        latitude: The latitude in degrees.
        spin_rate: The spin rate of the projectile in rad/s.

    Returns:
        A list of tuples, where each tuple contains the x and y coordinates of the projectile at a given time.
    """
    g = 9.81
    
    if weather_data:
        # Adjust for wind
        wind_speed = weather_data['wind']['speed']
        wind_deg = weather_data['wind']['deg']
        wind_rad = math.radians(wind_deg)
        wind_x = wind_speed * math.cos(wind_rad)
        wind_y = wind_speed * math.sin(wind_rad)
    else:
        wind_x = 0
        wind_y = 0

    if latitude:
        coriolis_force = calculate_coriolis_force(latitude, initial_velocity)
    else:
        coriolis_force = 0

    if spin_rate:
        magnus_force = calculate_magnus_force(initial_velocity, spin_rate)
    else:
        magnus_force = 0

    angle_rad = math.radians(angle)
    t_flight = (2 * initial_velocity * math.sin(angle_rad)) / g
    trajectory = []
    for t in range(0, int(t_flight) + 1):
        x = initial_velocity * math.cos(angle_rad) * t + wind_x * t
        y = initial_velocity * math.sin(angle_rad) * t - 0.5 * g * t**2 + wind_y * t + coriolis_force * t + magnus_force * t
        if y >= 0:
            trajectory.append((x, y))
    return trajectory