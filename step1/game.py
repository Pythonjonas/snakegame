import pygame

pygame.init()

#dis is for display
dis = pygame.display.set_mode((400,300))
pygame.display.update()

#Give display screen a title
pygame.display.set_caption('Snake game by Keano')

#Set game over to false (This is because the game has not started yet)
game_over = False

#Game has not been exited yet, so it is able to start
while not game_over:

    #starting the game
    for event in pygame.event.get():
        
        #if player has quit the game using any of the buttons, change the game over to TRUE
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()