import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop

mylist = ()
n=int(input("Enter four numbers:"))
for i in range(0,n):
  ele = int(input())
print(mylist)
    
  
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

class Snake:
  """Directs snake up, down, left, right, and controls color, speed, growth, actions
  """
  def __init__(self, x, y, filename):
    self.x = x
    self.y = y
    self.image = str(filename)

class Apples:
  """Positions apples and keeps track of score
  """
  def innit(self, x, y, filename, score):
    self.x = x
    self.y = y
    self.image = str(filename)
    se.f.score = 
    
class Background:
  """Displays user score, creates snake's boundaries, displays snake, displays fruit
  """
  def __init__(self, filename):
    self.image = str(filename)

  
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
