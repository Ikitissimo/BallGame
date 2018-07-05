import pygame
import os

size = width, height = 750, 422
screen = pygame.display.set_mode(size)

img_path = os.path.join('/Users/riccardob/Desktop/Py/BallGame/', 'ball.png')
background_image = pygame.image.load('/Users/riccardob/Desktop/Py/BallGame/background.jpg').convert()

pygame.display.set_caption("BallGame")

class Ball(object):
    def __init__(self):
        self.image = pygame.image.load(img_path)
        self.image_rect = self.image.get_rect()
        self.image_rect.x
        self.image_rect.y

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.image_rect.y += dist
        elif key[pygame.K_UP]:
            self.image_rect.y -= dist
        if key[pygame.K_RIGHT]:
            self.image_rect.x += dist
        elif key[pygame.K_LEFT]:
            self.image_rect.x -= dist

    def draw(self, surface):
        surface.blit(self.image, (self.image_rect.x, self.image_rect.y))

pygame.init()
screen = pygame.display.set_mode((750, 422))

ball = Ball()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    ball.handle_keys()

    screen.blit(background_image, [0, 0])
    ball.draw(screen)
    pygame.display.update()

    clock.tick(40)