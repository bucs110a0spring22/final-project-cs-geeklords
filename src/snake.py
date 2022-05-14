import pygame

class Snake:
  
  def __init__(self):
    self.length = 3
    self.list_snake = []
    
  def draw_snake(self,screen):
    #Color the snake
    purple = (104,34,139)
    
    #Draw the snake
    for x in self.list_snake:
      pygame.draw.rect(screen, purple, [x[0], x[1], 20, 20])
