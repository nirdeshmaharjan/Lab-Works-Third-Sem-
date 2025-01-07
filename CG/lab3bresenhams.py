
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (50, 250, 255)
BLACK = (50,20,50)

# Function to draw a line using DDA algorithm
def draw_line_dda(x1, y1, x2, y2):
    dx=abs(int(x2-x1))
    dy=abs(int(y2-y1))
    x=x1
    y=y1
    if x2>x1:
        lx=1
    else:
        lx=-1
    if y2>y1:
        ly=1
    else:    
        ly=-1
    if dx>dy:
        p=2*dy-dx
        while(not(x==x2)):
            if p<0:
                x=x+lx
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
            screen.set_at((round(x), round(y)), BLACK) 
    else:
        p=2*dy-dx
        while(not(y==y2)):
            if p<0:
                x=x+lx
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((round(x), round(y)), WHITE) 


       
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw_line_dda(20,20 ,100, 100)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
   