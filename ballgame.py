import pygame
import os

size = width, height = 750, 422
screen = pygame.display.set_mode(size)

img_path = os.path.join(os.getcwd())
background_image = pygame.image.load('background.jpg').convert()
bg_image_rect = background_image.get_rect()
pygame.mixer.pre_init(44100, 16, 2, 4096)

pygame.display.set_caption("BallGame")

class Ball(object):
    def __init__(self):
        self.image = pygame.image.load("ball.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.x
        self.image_rect.y
        self.facing = 'LEFT'

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN] and self.image_rect.y < 321:
            self.facing = 'DOWN'
            self.image_rect.y += dist
        elif key[pygame.K_UP] and self.image_rect.y > 0:
            self.facing = 'UP'
            self.image_rect.y -= dist
        if key[pygame.K_RIGHT] and self.image_rect.x < 649:
            self.facing = 'RIGHT'
            self.image_rect.x += dist
        elif key[pygame.K_LEFT] and self.image_rect.x > 0:
            self.facing = 'LEFT'
            self.image_rect.x -= dist

    def draw(self, surface):
        if self.facing == "RIGHT":
            surface.blit(pygame.transform.flip(self.image, True, False),(self.image_rect.x,self.image_rect.y))
        elif self.facing == "DOWN":
            surface.blit(pygame.image.load("ball_down.png"),(self.image_rect.x,self.image_rect.y))
        if self.facing == "UP":
            surface.blit(pygame.image.load("ball_up.png"),(self.image_rect.x,self.image_rect.y))
        elif self.facing == "LEFT":
            surface.blit(self.image,(self.image_rect.x,self.image_rect.y))


pygame.init()
screen = pygame.display.set_mode((750, 422))

ball = Ball()
clock = pygame.time.Clock()

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play(-1, 0.0)

running = True
while running:
    esc_key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if esc_key[pygame.K_ESCAPE]:
            pygame.display.quit()
            pygame.quit()
            running = False

    ball.handle_keys()

    screen.blit(background_image, bg_image_rect)
    screen.blit(background_image, bg_image_rect.move(bg_image_rect.width, 0))
    bg_image_rect.move_ip(-2, 0)
    if bg_image_rect.right <= 0:
        bg_image_rect.x = 0


    ball.draw(screen)
    pygame.display.update()

    clock.tick(60)
