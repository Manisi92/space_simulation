import numpy as np

class Planet:
    def __init__(self, name, radius, mass, distance_from_sun):
        """
        Initialize the Planet object with the following parameters:
        
        name: The name of the planet (string).
        radius: The radius of the planet (in kilometers).
        mass: The mass of the planet (in kilograms).
        distance_from_sun: The distance of the planet from the Sun (in kilometers).
        """
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance_from_sun = distance_from_sun

    def __str__(self):
        """
        Return a string representation of the planet.
        """
        return f"{self.name} (Radius: {self.radius} km, Mass: {self.mass} kg, Distance from Sun: {self.distance_from_sun} km)"
    
    def gravity(self):
        """
        Calculate the gravitational force at the planet's surface.
        The formula used is:
        F = G * M * m / r^2
        where:
            F is the gravitational force
            G is the gravitational constant
            M is the mass of the planet
            m is the mass of the object (not used here, but would be used for spacecraft)
            r is the radius of the planet
        """
        G = 6.67430e-11  # Gravitational constant (N·m²/kg²)
        return G * self.mass / (self.radius ** 2)

    def orbital_velocity(self):
        """
        Calculate the orbital velocity of the planet using the formula:
        v = sqrt(G * M / r)
        where:
            v is the orbital velocity (m/s)
            G is the gravitational constant
            M is the mass of the Sun
            r is the distance of the planet from the Sun
        """
        G = 6.67430e-11  # Gravitational constant (N·m²/kg²)
        M_sun = 1.989e30  # Mass of the Sun (kg)
        velocity = np.sqrt(G * M_sun / self.distance_from_sun)  # Orbital velocity (m/s)
        return velocity

    def orbital_period(self):
        """
        Calculate the orbital period (the time taken for the planet to complete one orbit).
        The formula used is:
        T = 2 * pi * sqrt(r³ / G * M_sun)
        where:
            T is the orbital period (in years)
            r is the distance from the Sun (in meters)
            G is the gravitational constant
            M_sun is the mass of the Sun
        """
        G = 6.67430e-11  # Gravitational constant
        M_sun = 1.989e30  # Mass of the Sun (kg)
        period = 2 * np.pi * np.sqrt(self.distance_from_sun ** 3 / (G * M_sun))
        return period / (60 * 60 * 24 * 365)  # Convert seconds to years