import pygame
import time
import random      #We use this to randomly create a food block

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#color for the food object
blue = (0, 0, 255)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Keano')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 20

font_style = pygame.font.SysFont(None, 30)

def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])

#Creates the function that will close or replay the game,after game over
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0
    
    #Creates a food block randomly on the screen
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    
    #while not game over, the game resumes
    while not game_over:
        
        #We prompt the user to either play again or close the game
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q (to QUIT) or C (to PLAY AGAIN)", red)
            pygame.display.update()
            
            #Closes game is Q is pressed
            #set game over to true
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    #Restarts the game if the user presses the (C) button
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        #We draw the food block on the sreen
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        #We draw the snake block onto the screen
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        #Print message in terminal if snake eats food block
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()
    
#Run the game loop
#This will ask the user to play again or quit
gameLoop()

