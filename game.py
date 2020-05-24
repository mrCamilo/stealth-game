import sys
import pygame

#main function
def main():

    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pyame.display.set_icon(logo)
    pygame.display.set_caption("hey it me")

    screen = pygame.display.set_mode((240,180))
    running = True

    #game's main while loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip

if __name__=="__main__":
    main()
