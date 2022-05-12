:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Snake Game
## CS 110 Final Project
### Spring 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[Snake Game Presentation Repl](https://replit.com/@Brianna-OO/final-project-cs-geeklords#main.py) \
[Snake Game Presentation Demo](https://docs.google.com/presentation/d/1KRhsGmiyhKvFk8tZsDDbPL1Xe0GopRUtqusd4xfNnnM/edit#slide=id.g11bf020bd32_0_0)

### Team: Geeklords
#### Erica Rodrigues, Julia Steckler, Brianna Sexton

***

## Project Description *(Software Lead)*

We decided to replicate the classic snake game as our final project. The basic idea of the snake game is a snake moves around a box trying to eat apple. Once the snake eats an apple, it grows in size, and a new apple is spawned for the snake to eat. The game is more complicated because if the snake bites itself (runs into its body) or runs into the boundaries of the box, the game is over. The user controls the direction of the snake's head (up, down, left, or right), and the snake's body follows.

***    

## User Interface Design *(Front End Specialist)*

* << Welcome and Game Over Screen: https://docs.google.com/document/d/1PU83rbIjToGl7bUlHPRCLUX5jQfMAl0z6P-sFnBjYNQ/edit?usp=sharing >>
  
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*
 
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes 
  * Controller: Runs the main loop for starting the game, playing the game, and exits when the snake collides into the wall or itself
  * Snake: Holds the position of the snake, size of snake, adds length to the snake when it eats an apple, holds conditions where the snake dies
  * Apples: Holds the position for the apples, spawns new apples at random locations, allows snake to collide with apples


## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src: \
  snake.py \
  apples.py \
  controller.py \
  utility.py
  
    
  
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*

   * You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Brianna Sexton

Worked as integration specialist by making sure that programming by front and back end specialist flows efficiently and clearly. Test game constantly to make sure all actions are working.

### Front End Specialist - Julia Steckler

Front-end lead conducted significant research on the layout and design of game. Organized use of computer buttons for user to control their player. Creates efficient internal linking and user-friendly navigation of game and menus.

### Back End Specialist - Erica Rodrigues

The back end specialist specifically programs outcomes of actions taken from user. Programs what happens and how a user wins/loses game. Uses classes to organize actions.

## Testing *(Software Lead)*

* Constanyly testing the game focusing on isolated features
    * << Example >>

## ATP
|Step|Procedure|Expected Results|Actual Results| 
|-------|:-------------:| -----------------:| -------------- |
|1|Press Run Button|Display of Main Menu Screen|
|2| Press Play to Begin Game|Menu screen disappears and game screen displays. On the game screen there is a snake and apple.|  |
|3| Press Left arrow key | Snake character moves left| |
|4| Press Right arrow key| Snake character moves right| |
|5| Press up arrow key| Snake character moves up| |
|6| Press down arrow key| Snake character moves down| | 
|7| Move snake to eat apple| Snake grows in length, current apple is eaten and new apple spwans| | 
|8| Move snake to hit boundaries| Game over screen| |
|9| Have snake bite itself| Game over screen| | 

REFERENCES:
https://riptutorial.com/pygame/example/18046/event-loop