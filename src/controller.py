
      
import pygame
import time
import random
from src.snake import Snake
from src.apple import Apple
 
pygame.init()
 
#size of screen
screen_width = 600
screen_height = 400

#create screen 
screen = pygame.display.set_mode((screen_width, screen_height))
 
#create the clock
clock = pygame.time.Clock()
 
 
def gameLoop():
    game_over = False
 
    #start in the middle
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

    while not game_over:
        
        #display the background
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
        clock.tick(10)
 
    pygame.quit()
    quit()
 
 
gameLoop()








