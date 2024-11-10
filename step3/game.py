import pygame 

pygame.init()

#color of the background (white)
white = (255, 255, 255)

#color of the snake (black)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Keano')

game_over = False

#sets the position of the snake (starting position)
x1 = 300
y1 = 300

#controlls the movement of the snake
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        #Controlls the movement via keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    #Updates the movement of the snake, once the user enteres up, down, left or right
    x1 += x1_change
    y1 += y1_change

    #creates the white background for the game
    dis.fill(white)

    #the snake will be black
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()