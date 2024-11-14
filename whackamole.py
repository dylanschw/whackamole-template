import pygame 
import random


def main():
    try:
        pygame.init()

        # Set up the game window and other configurations
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()

        # Load the mole image
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft=(0, 0))  # Start at the top-left corner

        # Game variables
        grid_size = 32  # Size of each square in the grid
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):  # Check if mole is clicked
                        # Move mole to a random square
                        new_x = random.randrange(0, 640, grid_size)
                        new_y = random.randrange(0, 512, grid_size)
                        mole_rect.topleft = (new_x, new_y)

            # Fill the screen with a background color
            screen.fill("light green")

            # Draw the grid
            for x in range(0, 640, grid_size):
                pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, 512))  # Vertical lines
            for y in range(0, 512, grid_size):
                pygame.draw.line(screen, (200, 200, 200), (0, y), (640, y))  # Horizontal lines

            # Draw the mole
            screen.blit(mole_image, mole_rect)

            # Update the display
            pygame.display.flip()

            # Limit the frame rate
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
