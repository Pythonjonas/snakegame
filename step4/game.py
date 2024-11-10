import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

#Game over color
red = (255, 0, 0)
brown = (153, 102, 51)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Keano')

game_over = False

x1 = dis_width / 2
y1 = dis_height / 2

#Size of snake
snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

#snake speed will be 20 to begin (can change)
snake_speed = 20

#Font and size of the game over message
font_style = pygame.font.SysFont(None, 50)

#Create a message function to tell the user game over
def message(msg, color):
    mesg = font_style.render(msg, True, color)

    #Displays message back to user
    dis.blit(mesg, [dis_width / 2, dis_height / 2])

while not game_over:
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

    #if snake hits display boundaries, game over will be true, displaying the message above
    #Any one of these conditions need to be true for game over
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

    pygame.display.update()

    #setting speed of snake in pixels
    clock.tick(snake_speed)

#Displayed once game ends
message("You lost!", brown)
pygame.display.update()

#time taken before it shuts automatically
time.sleep(2)   #in seconds

#quits the game automatically (after game over is displayed)
pygame.quit()
quit()