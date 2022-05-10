import random
import pygame
screen_width = 180
screen_height = 180 
red = pygame.Color(255, 0, 0)
class apples():
    # Initialization
    def __init__(self):
      #color of apple
      self.color = red
      #size of apple
      self.width = 12
      self.height = 12
     #location of apple
      self.x = 32
      self.y = 100
      
    # Makes the apple visible
    def draw_apple(self, surface):
       #creating rectangle with given size, and location 
      self.apples = pygame.Rect(self.width, self.height, self.x, self.y)
      pygame.draw.rect(surface, self.color, self.apples)
   
      # Is the food eaten?
    def eat_food(self, head):
        return self.food.colliderect(head)
   
      # Returns a new position for the food after it is eaten
    def new_location(self):
        self.x = random.randint(0, screen_width-1) * 12 
        self.y = random.randint(0, screen_height-1) * 12 
  
  
  
  