
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Mid point  ellipse algoritm")

# Colors
WHITE = (50, 250, 255)
BLACK = (0,0, 0)

# Function to draw a line using DDA algorithm
def draw_line(xc,yc,rx,ry):
    x=0
    y=ry
    dx=2*ry*ry*x
    dy=2*rx**2*y
    p1=ry**2-rx**2*ry+0.25*rx**2
    while(2*ry*ry*x<=2*rx**2*y):
        screen.set_at((round(x+xc), round(y+yc)), WHITE) 
        screen.set_at((round(x+xc), round(-y+yc)), WHITE) 
        screen.set_at((round(-x+xc), round(y+yc)), WHITE) 
        screen.set_at((round(-x+xc), round(-y+yc)), WHITE) 

        if (p1<0):
            x=x+1
            y=y
            p1=p1+2*ry**2*x+ry**2
        else:
            x=x+1
            y=y-1
            p1=p1+2*ry**2*x-2*rx**2*y+ry**2
        
    p2=ry**2*(x+0.5)**2+rx**2*(y-1)**2-rx**2*ry**2
    while y!=0:
        screen.set_at((round(x+xc), round(y+yc)), WHITE) 
        screen.set_at((round(x+xc), round(-y+yc)), WHITE) 
        screen.set_at((round(-x+xc), round(y+yc)), WHITE) 
        screen.set_at((round(-x+xc), round(-y+yc)), WHITE)

        if (p2>0):
            x=x
            y=y-1
            p2=p2-2*rx**2*y+rx**2
        else:
            x=x+1
            y=y-1
            p2=p2+2*ry**2*x-2*rx**2*y+rx**2
         
      
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
        draw_line(370,250,150,60)
        draw_line(370,250,250,140)
        draw_line(370,250,350,220)
        draw_line(370,250,40,40)
        draw_line(350,100,20,20)
        draw_line(250,200,20,20)
        draw_line(40,250,60,60)
        draw_line(350,100,60,12)
        
        
         # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
