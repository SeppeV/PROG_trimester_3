import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def recursive_draw(x, y, width, height):
    """Recursive rectangle function."""
    pygame.draw.rect(screen, BLACK, [x, y, width, height], 1)
    if y >= 500:  # Screen bottom reached.
        return
    # Is the rectangle wide enough to draw again?
    elif x < 750-width:  # Right screen edge not reached.
        x += width
        # Recursively draw again.
        recursive_draw(x, y, width, height)
    else:
        # Increment y and reset x to 0 and start drawing the next row.
        x = 0
        y += height
        recursive_draw(x, y, width, height)


pygame.init()
size = [750, 500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill(WHITE)
recursive_draw(0, 0, 150, 50)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(60)


pygame.quit()