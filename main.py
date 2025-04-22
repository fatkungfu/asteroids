import sys
import pygame
import csv
from datetime import datetime
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def save_score(score):
    filename = "highscores.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create file with headers if it doesn't exist
    try:
        with open(filename, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Score"])
    except FileExistsError:
        pass

    # Append the new score
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, score])


def main():
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize the score
    score = 0
    score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

    # add groping to the player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(score)
                return

        # update the player
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print(f"Game over! Final score: {score}")
                save_score(score)
                sys.exit()
            # check for collisions between shots and asteroids
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 10

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        for obj in drawable:
            # draw the player
            obj.draw(screen)

        # draw the score
        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limit to 60 frames per second
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
