import pygame

pygame.init()

dis = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake game by Keano')

purp = (128, 0, 128)
red = (255, 0, 0)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #draw function to create a rectangle (this will be the snake)
    pygame.draw.rect(dis, purp, [200, 150, 10, 10])

    #Update any changes made
    pygame.display.update()
pygame.quit()
quit()