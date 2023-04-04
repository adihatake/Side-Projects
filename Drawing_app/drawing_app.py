import pygame
from pygame import *

pygame.init()

window_size = 700

palette_colour = (139, 69, 19)
palette_coordinates = (600, 0, 100, window_size) #(x, y, width, length)

# Set up the drawing window
screen = pygame.display.set_mode([700, 700])

drawing_surface = pygame.Surface((700, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ERASER = (188, 143, 143)
WHITE = (255, 255, 255)
colour_selected = (255, 255, 255)

class Colour_option:
    def __init__(self, coordinate, colour, radius):
        self.coordinate = coordinate
        self.colour = colour
        self.radius = radius
        
    def draw_paint_option(self):
        pygame.draw.circle(drawing_surface, self.colour, self.coordinate, self.radius, 0) 
        
    def check_if_clicked(self, mouse_pos):
        global colour_selected
        colour_selected = screen.get_at(mouse_pos)[:3]
        if colour_selected == ERASER:
                    colour_selected = WHITE
        
        return colour_selected

paint_options = []

red_coord = (650, 100)
red_option = Colour_option(red_coord, RED, 20)
paint_options.append(red_option)


blue_coord = (650, 200)
blue_option = Colour_option(blue_coord, BLUE, 20)
paint_options.append(blue_option)


green_coord = (650, 300)
green_option = Colour_option(green_coord, GREEN, 20)
paint_options.append(green_option)


eraser_coord = (650, 400)
eraser_option = Colour_option(eraser_coord, ERASER, 20)
paint_options.append(eraser_option)


#Run until the user asks to quit
running = True

# Fill the background with white initially
screen.fill((255, 255, 255))
drawing_surface.fill((255, 255, 255))


pygame.draw.rect(drawing_surface, palette_colour, palette_coordinates)
    
for paint in paint_options:
    paint.draw_paint_option()
    
pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.type)
            pen_pos = pygame.mouse.get_pos()
            
            if pen_pos[0] > 600:
                for paint in paint_options:
                    paint.check_if_clicked(pen_pos)
                       
            if pen_pos[0] < 600:
                pygame.draw.circle(drawing_surface, colour_selected, pen_pos, 5, 0)
        

                
    # draw the drawing surface onto the screen
    screen.blit(drawing_surface, (0, 0))
    
    # update the display
    pygame.display.flip()
 
            

# Done! Time to quit.
pygame.quit()


