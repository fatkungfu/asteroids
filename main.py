import pygame
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update the player
        player.update(dt)
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        player.draw(screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limit to 60 frames per second
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
