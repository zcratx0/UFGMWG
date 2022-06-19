import pygame
from screeninfo import get_monitors
res = ""
for m in get_monitors():
    res = m

res = str(res)

width = int(res[24:28])
height = int(res[37:41]) - 70

background_colour = (234, 212, 252)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((width, height))

# Set the caption of the screen
pygame.display.set_caption('UFGMWG')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
