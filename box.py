import pygame

class Box:

    def __init__(self, x, y, box_type):
        self.box_type = box_type
        self.x = x
        self.y = y
        self.set_image()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def uncover_box(self):
        self.box_type -= 1
      #  if self.box_type < 0:
      #      self.box_type = 1
        self.set_image()

    def set_image(self):
        if self.box_type == 0:
            self.image = pygame.image.load("yellow-block.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .035, self.image_size[1] * .035)
            self.image = pygame.transform.scale(self.image, scale_size)
            self.image_size = self.image.get_size()
        else:
            self.image = pygame.image.load("orangeblock.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .21, self.image_size[1] * .21)
            self.image = pygame.transform.scale(self.image, scale_size)
            self.image_size = self.image.get_size()
