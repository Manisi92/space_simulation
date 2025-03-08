import pygame
import numpy as np
from planet import Planet
from spacecraft import Spacecraft

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create planets
earth = Planet(name="Earth", radius=6371, mass=5.972e24, distance_from_sun=1.496e8 * 1000)
mars = Planet(name="Mars", radius=3389, mass=0.64171e24, distance_from_sun=2.279e8 * 1000)

# Create spacecraft
spacecraft = Spacecraft(name="Apollo", position=[400, 300], velocity=[3000, 0], mass=5000)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update spacecraft position
    spacecraft.update_position(0.1)
    spacecraft.apply_gravity(earth)  # Gravity applied from Earth

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw Earth and Mars
    pygame.draw.circle(screen, BLUE, (400, 300), 10)  # Earth
    pygame.draw.circle(screen, RED, (600, 300), 8)    # Mars

    # Draw spacecraft
    pygame.draw.circle(screen, WHITE, (int(spacecraft.position[0] / 1000), int(spacecraft.position[1] / 1000)), 5)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()