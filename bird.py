import pygame
import random


class Bird:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["bird_up.png", "bird_down.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.up = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_bird(self):
        if self.x != 1200:
            self.x = self.x + self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        else:
            self.x = 0
            return True


    def switch_image(self):
        image_number = 0
        if not self.up:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.up = not self.up