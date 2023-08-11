import pygame

widht = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, widht, height, color):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        self.color = color
        self.rect = (x, y, widht, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.keys.get_pressed()

        

def redrawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        redrawWindow()

main()