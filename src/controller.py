import pygame

class Controller:
  
  def __init__(self, width, height):
    """Takes two parameters width and height
    Sets up pygame data"""
    pygame.init()
    self.width = 500
    self.height = 500
    self.screen = pygame.display.set_mode((self.width, self.height)) 
    clock = pygame.time.Clock()
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.fill((255, 255, 255)) 
    
  def mainloop(self):
    """Select state loop"""
    running = True
    while True:
      if(self.state == "START"):
        self.gameLoop()
      elif(self.state == "GAMEOVER"):
        self.gameOver()
      
  def gameLoop(self):
      """Controls snake movement and checks for collison"""
    while self.state == "GAME":
      for event in pygame.event.get():
        if event.type == pygame.QUIT
        elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            self.snake.up(0, 1)
        elif event.key == pygame.K_LEFT:
            self.snake.left(-1, 0)
        elif event.key == pygame.K_DOWN:
            self.snake.down(0, -1)
        elif event.key == pygame.K_RIGHT:
            self.snake.right(1, 0)
    #controls snake movement
    pygame.sprite.spritecollide(self.player, self.enemies)
    if self_position[0] == block[0] and self_position[1] == block[1]:
      gameover()
    pygame.snake.update()
    #checks for collision

  def gameover(self):
      """Exits game when user presses quit button and ends game when snake touches its own body"""
      if event.type == pygame.QUIT:
        pygame.display.upate()
        quit()
        
      for block in self_body[1:]: 
        if self_position[0] == block[0] and self_position[1] == block[1]:
          screen = pygame.display.set_mode((500, 500)) 
          pygame.display.set_caption('GAME OVER')
          screen.fill(red)
          self.screen.blit(snake, apple)
          pygame.display.update():
          while True:
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()

    