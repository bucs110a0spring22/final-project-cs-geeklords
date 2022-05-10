import pygame
orange = pygame.Color(255,165,0)
yellow = pygame.Color(255,255,0)
screen_width = 180 
screen_height = 180 
#initializing variables of the snake 
def __init__(self):
  #color of snake 
  self_head_color = orange
  self_body_color = yellow
  #location of snake 
  self_x = 0
  self_y = screen_height /2
  # size of snake (1st block)
  self_height = 12
  self_width = 12
  #snake doesn't move until player starts the game
  self_direction = 'stop'
  # speed of snake 
  self_speed = 5
  self_body = []
  self_length = 1

#drawing the snake 
  def draw_snake(self, surface):
        self_body = []
        pygame.draw.rect(surface, self.head.color, self.head)
        self.head = pygame.Rect(self.x, self.y, self.width, self.height)
  for unit in self.body:
        segment = pygame.Rect(unit[0], unit[1], self.width, self.height)
        pygame.draw.rect(surface, self.body_color, segment)
        self.seg.append(segment)

## Adding block when snake eats ####
  head=[]
head.append(self.x)
head.append(self.y)
self_body.append(head)
if len(self_body)>self_length:
  del self_list[0]

### Snake colliding into wall ###
  if self_body[0] < 0 or self_body[0] > screen_width:
      game_over()
  if self_body[1] < 0 or self_body[1] > screen_height:
        game_over()

### Snake colliding into itself ###
    for block in self_body[1:]: 
      if self_body[0] == block[0] and self_body[1] == block[1]:
            game_over()

        
#direction snake moves 
def snake_direction(direction, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return "LEFT"
        elif event.key == pygame.K_RIGHT:
            return "RIGHT"
        elif event.key == pygame.K_UP:
            return "UP"
        elif event.key == pygame.K_DOWN:
            return "DOWN"
    return direction

  

