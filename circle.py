import pygame 
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill("white")
pygame.display.update()

class Circle():
    def __init__(self,color,position,radius):
        self.circle_surface = screen
        self.circle_color = color
        self.circle_positions = position
        self.circle_radius = radius
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_positions,self.circle_radius)
    def grow(self,r):
        self.circle_radius = self.circle_radius + r
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_positions,self.circle_radius)


blue_circle = Circle("blue",(300,300),20)

run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    

        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            blue_circle.draw()
        elif i.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            blue_circle.grow(20)
            pygame.display.update()

        

    
    pygame.display.update()

