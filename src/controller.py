      
import pygame
import sys
from src.snake import Snake
from src.apple import Apple
import time

pygame.font.init()
 
#create the clock
clock = pygame.time.Clock()
class Controller:
  def __init__(self, screen_width=600, screen_height=400):
    pygame.init()
    #size of screen
    screen_width = 600
    screen_height = 400

    #create screen 
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = pygame.image.load("background.png")
    screen.blit(bg, (0, 0))
    #create the clock
    #clock = pygame.time.Clock()
    
  def mainLoop(self):
      #self.state = "START"
      self.state = "Game"
      print("This is mainloop")
      while True:
          if(self.state == "START"):
            print("start loop has been called")
            self.startLoop()
          elif(self.state == "GAME"):
            self.gameloop()
            print("game loop has been called")
          elif(self.state == "GAME OVER"):
            print("game over loop has been called")
            self.gameoverloop()

  def startLoop(self):
        pygame.display.set_caption("Menu")
        while (self.state == "START"):
        
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              self.state = "GAME OVER"
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                self.state = "GAME"
              if event.key == pygame.K_q:
                pygame.quit()
                quit()

  def startScreen():
    myfont = pygame.font.SysFont('times new roman', 30)
    text_1 = myfont.render('Snake Game', True, (141,238,238))
    text_2 = myfont.render('The Game is About to Begin', True, (193,255,193))
    bg = pygame.image.load("background.png")
    bg = pygame.transform.scale(bg, (600, 400))
    screen_width = 600
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.blit(bg, (screen_width, screen_height))
    screen.blit(text_1, (200,200))
    screen.blit(text_2,(100, 160))
    pygame.display.flip()
    print("This is where startScreen is called")
    time.sleep(3)

  startScreen()


  def gameLoop():
      game_over = False
      print("Game Loop")
      #start in the middle
      screen_width = 600
      screen_height = 400
      x = screen_width / 2
      y = screen_height / 2
 
      new_x = 0
      new_y = 0
      #create a snake
      snake = Snake()
 
      #create an apple
      apple = Apple()
 
      #load the background image
      bg = pygame.image.load("background.png")
      bg = pygame.transform.scale(bg, (600, 400))
      while not game_over:
        
          #display the background
          screen = pygame.display.set_mode((screen_width, screen_height))
          screen.blit(bg, (0, 0))
 
          for event in pygame.event.get():
            
              #game over
              if event.type == pygame.QUIT:
                  game_over = True
            
              #presses a key
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                      new_x = -10
                      new_y = 0
                  elif event.key == pygame.K_RIGHT:
                      new_x = 10
                      new_y = 0
                  elif event.key == pygame.K_UP:
                      new_y = -10
                      new_x = 0
                  elif event.key == pygame.K_DOWN:
                      new_y = 10
                      new_x = 0
 
          # If you run off the map
          if x >= screen_width or x < 0 or y >= screen_height or y < 0:
              game_over = True

          #replace new coordinates
          x += new_x
          y += new_y
       
          #drap an apple
          Apple.draw_apple(apple, screen)

          #add the new position to the snake (will draw in background)
          addition = []
          addition.append(x)
          addition.append(y)
          snake.list_snake.append(addition)
        
          #if the snake did not actually eat anything, only display the current length of the snake
          if len(snake.list_snake) > snake.length:
            #don't show additional pieces of the snake unless the length has increased
              del snake.list_snake[0]
 
          #draw the snake over the background
          Snake.draw_snake(snake, screen)
 
          #update the display
          pygame.display.update()
 
          #check to see if the snake ate the apple
          if x == apple.applex and y == apple.appley:
              #create a new apple
              apple = Apple()
            
              #inccrease the length of the snake
              snake.length += 1
        
          #tick the clock
          clock = pygame.time.Clock()
          clock.tick(10)
      #pygame.quit()
      #quit()
 
 
  gameLoop()

  def endScreen():
    screen_width = 600
    screen_height = 400
    myfont = pygame.font.SysFont('times new roman',   45)
    #text_1 = myfont.render('Snake Game', True, (141,238,238))
    text_2 = myfont.render('The Game is Over!!!', True, (193,255,193))
    bg = pygame.image.load("assets/images.png")
    bg = pygame.transform.scale(bg, (600, 400))
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.blit(bg, (0, 0))
    #screen.blit(bg, (screen_width, screen_height))
    #screen.blit(text_1, (200,200))
    screen.blit(text_2,(100, 160))
    pygame.display.flip()
    print("This is where endScreen is called")
    time.sleep(3)

  endScreen()



 





