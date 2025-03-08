import numpy as np

class Spacecraft:
    def __init__(self, name, position, velocity, mass):
        """
        Initialize the spacecraft object with the following parameters:
        
        name: Name of the spacecraft (string).
        position: The initial position of the spacecraft (list of [x, y, z] coordinates).
        velocity: The initial velocity of the spacecraft (list of [vx, vy, vz]).
        mass: The mass of the spacecraft (in kilograms).
        """
        self.name = name
        self.position = np.array(position, dtype=np.float64)  # Position of the spacecraft (x, y, z)
        self.velocity = np.array(velocity, dtype=np.float64)  # Velocity (vx, vy, vz)
        self.mass = mass                    # Mass of the spacecraft

    def __str__(self):
        """
        Return a string representation of the spacecraft.
        """
        return f"{self.name} (Position: {self.position}, Velocity: {self.velocity})"

    def update_position(self, delta_t):
        """
        Update the position of the spacecraft based on its velocity and the time step delta_t.
        
        delta_t: The time step (in seconds).
        """
        self.position += self.velocity * delta_t

    def apply_gravity(self, planet):
        """
        Apply the gravitational force of the given planet to the spacecraft.
        Update the spacecraft's velocity based on the gravitational acceleration.
        
        planet: The planet that exerts gravitational force on the spacecraft.
        """
        G = 6.67430e-11  # Gravitational constant (N·m²/kg²)
        r = np.linalg.norm(self.position)  # Distance between the spacecraft and the planet (simplified)
        force_magnitude = G * self.mass * planet.mass / r**2
        force_direction = -self.position / r  # Gravity pulls towards the planet
        force = force_magnitude * force_direction
        acceleration = force / self.mass  # Acceleration = Force / Mass
        self.velocity += acceleration * 1  # Update the velocity (time step = 1 second)