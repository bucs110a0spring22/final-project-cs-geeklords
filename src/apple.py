
import pygame
import random

class Apple:
    applex = 0
    appley = 0
 
    def __init__(self):
        #create random coordinates between 0 and width but ensure it is a multiple of 20
        self.applex = random.randint(0,12) * 20

        #create random coordinates between 0 and height but ensure it is a multiple of 20
        self.appley = random.randint(0,12) * 20

    def draw_apple(self, screen):
        #color of apple
        red = (213, 50, 80)
        
        #draw the apple to the screen
        pygame.draw.rect(screen, red, [self.applex, self.appley, 20, 20])

#bg = pygame.image.load("background.png")
 #     bg = pygame.transform.scale(bg, (600, 400))
