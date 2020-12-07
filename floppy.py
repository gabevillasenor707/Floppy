import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen =  pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Define game variables
ground_scroll = 0
scroll_speed = 4

# Load images
bg = pygame.image.load('/Users/gabe/Desktop/bg.png')
ground_img = pygame.image.load('/Users/gabe/Desktop/ground.png')

class Bird(pygame.sprite.Sprite):
    def __int__(self, x, y):
        pygame.sprite.Sprite.__int__(self)
        self.image = pygame.image.load('/Users/gabe/Desktop/bird1.png')
        self.rect = self.image.get_rect()
        self.rest.center = [x, y]


bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)



run = True
while run:

    clock.tick(fps)

    # Draw background
    screen.blit(bg, (0,0))

    # Draw bird group
    bird_group.draw(screen)

    # Draw and scroll the ground
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()