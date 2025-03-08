import numpy as np
import matplotlib.pyplot as plt
from planet import Planet
from spacecraft import Spacecraft

# Create Earth and Mars as planets
earth = Planet(name="Earth", radius=6371, mass=5.972e24, distance_from_sun=1.496e8 * 1000)  # 1 AU in meters
mars = Planet(name="Mars", radius=3389, mass=0.64171e24, distance_from_sun=2.279e8 * 1000)

# Create spacecraft
spacecraft = Spacecraft(name="Apollo", position=[0, 1.496e8 * 1000, 0], velocity=[3000, 0, 0], mass=5000)

# Time step for the simulation
delta_t = 100  # 100 seconds
time_steps = 360  # Total number of steps to simulate

# Create lists to store spacecraft position and velocity data
positions = []
velocities = []

# Run the simulation for the specified number of time steps
for _ in range(time_steps):
    spacecraft.update_position(delta_t)
    spacecraft.apply_gravity(earth)  # Apply Earth's gravity
    
    positions.append(spacecraft.position.copy())
    velocities.append(np.linalg.norm(spacecraft.velocity))  # Store velocity magnitude

# Convert position data to numpy array for easier manipulation
positions = np.array(positions)

# Plot spacecraft trajectory
plt.figure(figsize=(10, 6))
plt.plot(positions[:, 0], positions[:, 1], label="Spacecraft Trajectory", color='white')
plt.scatter(earth.distance_from_sun, 0, color='blue', label='Earth')
plt.scatter(mars.distance_from_sun, 0, color='red', label='Mars')
plt.title("Spacecraft Trajectory in Space")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)
plt.show()

# Plot spacecraft velocity over time
plt.figure(figsize=(10, 6))
plt.plot(np.arange(time_steps), velocities, label="Spacecraft Velocity", color='orange')
plt.title("Spacecraft Velocity Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.grid(True)
plt.show()