import pygame
from screeninfo import get_monitors

# Asigno variable resolucion.
res = ""
# obtengo informacion de la pantalla
for m in get_monitors():
    res = m
# Paso la variable a texto
res = str(res)
# recorto los valores del texto y los hago enteros
width = int(res[24:28])
height = int(res[37:41]) - 70

background_colour = (0, 0, 0)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((width, height))

raton = pygame.image.load(r"assets\raton.png")


def ratonsillo(x, y):
    screen.blit(raton, (x, y))


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

    ratonsillo(0, 0)
    screen.blit(raton, (0, 0))

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
