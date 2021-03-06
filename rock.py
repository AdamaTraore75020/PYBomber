import square
import pygame


class Rock(pygame.sprite.Sprite):

    def __init__(self, x, y, window):
        super(Rock, self).__init__()
        self.x = x
        self.y = y
        self.background = pygame.image.load("./resources/rock.png").convert()
        self.rect = pygame.Rect(x, y, 40, 40)
        window.blit(self.background, (x, y))
