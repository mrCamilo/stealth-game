import sys
import pygame

#main function
def main():
    
    #Initialize game
    pygame.init()
    pygame.display.set_caption("hey it me")
    screen = pygame.display.set_mode((480,360))
    red = (255, 64, 64)
    screen.fill((red))

    #Loading image
    ball = pygame.image.load("images/ball.gif")
    ballrect = ball.get_rect()

    running = True

    #game's main while loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(ball,(0,0))
        pygame.display.flip()

if __name__=="__main__":
    main()
