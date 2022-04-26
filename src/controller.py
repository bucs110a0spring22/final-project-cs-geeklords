import pygame
from src.utility import Utility

class Controller:
  def __init__(self, width=480, height=320):
    pygame.init()
    self.width = width
    self.height = height
    Utility.screen_height = height
    Utility.screen_width = width
    self.screen = pygame.display.set_mode( (self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size())

    self.background.fill( (250, 250, 250))
    ##white background
    pygame.key_set_repeat(1, 50)

    player = pleayer.Player(x=10, y=10, filenames)

    enemies = pygame.sprite.Group()
    num_enemies = 3
    for i in range(num_enemies):
      x = random.randrange(100, 400)
      y = random.randrange(100, 400)
      enemy = enemy.Enemy(x=x, y=y, enemy_filenames)
      enemies.add(enemy)

    models = (self.player,)+tuple(enemies)
    all_sprites = pygame.sprite.Group(models)

    self.state = "RUNNING"
    

    #draw() draws all sprites in the group on the screen
    #update() calls update on all sprites in the group
    #spritecollide() checks if any sprite in a group collided with a specific sprite
    


  def mainloop():
    while self.state == "RUNNING":
      #retrieve user events
      #respond to user events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.state = "DONE"
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            self.player.move("UP")
          elif event.key == pygame.K_DOWN:
            self.player.move("DOWN")
          elif event.key == pygame.K_LEFT:
            self.player.move("LEFT")
          elif event.key == pygame.K_RIGHT:
            self.player.move("RIGHT")
      #update all models
      self.all_sprites.update()

      #fights is a tuple of enemies that collided with the player
      fights = pygame.sprite.spritecollide(self.player, self.enemies)
      if fights:
        #looping through each enemy that collided with the player
        for enemy in fights:
          result = self.player.fight(enemy)
          if result:
            enemy.kill()
          else:
            self.player.health -= 1
      #redraw the screen
      self.screen.blit(background, (0,0))
      if self.player.health == 0:
        self.sate = "GAMEOVER"

      self.all_sprites.draw()

      pygame.display.flip()

  def gameoverloop(self):
    self.gobackground
    self.gobackground.fill(250, 0, 0)
    self
    pygame.display.flip()
    
    

  