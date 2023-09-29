import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

#declare global constants

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = 9
SEPARATION = 10 #separation between two pixels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1 , "DOWN":2, "LEFT":3, "RIGHT":4}

#initialize screen
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH),pygame.HWSURFACE)
#hw surface stands for hardware surface memory on video card for scoring 
#draws as opposed to main memory

#resources
score_front = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_front.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_front.size("Score")
background_color = pygame.Color(0,0,0)
black = pygame.Color(0,0,0)

#clock at left corner
gameClock = pygame.time.Clock()

def checkCollision(posA,As ,posB,Bs): #As is the size of a and Bs is the size of b
    if(posA.x < posB.x + Bs and posA.x + As > posB.x and posA.y < posB.y + Bs and posA.y > posB.y):
        return True
    return False
# This checks the boudaries limiting boundaries of the screen
def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x < 0): #checks if the snake is breaks the limit of the screen
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if(snake.y < 0):
        snake.y - SCREEN_HEIGHT - SNAKE_SIZE

#food for the snake
class snakeFood:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("Orange") #Color of the Food

    def draw(self,screen):
             pygame.draw.rect(screen,self.color(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)

#define keys

def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            return KEY["UP"]
        elif event.key == pygame.K_DOWN:
            return KEY["DOWN"]
        elif event.key == pygame.K_LEFT:
            return KEY["LEFT"]
        elif event.key == pygame.K_RIGHT:
            return KEY["RIGHT"]
        #exit
        elif event.key == pygame.K_ESCAPE:
            return "exit"
        #Continue and play again if you want
        elif event.key == pygame.K_y:
            return "yes"
        #if you don't want too
        elif event.key == pygame.K_n:
            return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame():
    message = game_over_font.render("Game Over",1,pygame.Color("white"))
    message_play_again = play_again_font.render("Play again ? (Y/N)",1,pygame.color("green"))
    # This line says "Draw messege onto the screen at the center"
    screen.blit,(message,(328,240))
    screen.blit(message_play_again,(320+12,240+40))

    #Update the full display Surface to the screen
    #Update portions of the screen for software displays
    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        #It will compute how many . milliseconds have passed since the previous call.
        #means that for every second at most #?frames should pass.
        gameClock.tick
    sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg,(SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb,(SCREEN_WIDTH - 45,14))

def drawGameTime(gameTime):
    gameTime = score_front.render("Time:" , 1, pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("white"))
    screen.blit(gameTime,(30,10))
    screen.blit(game_time_numb,(105,14))

def exitScreen():
    pass

def main():
    score = 0
