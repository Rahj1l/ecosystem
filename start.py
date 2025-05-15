import numpy as np
import pandas as pd
import pygame

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Window")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color (RGB)
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()