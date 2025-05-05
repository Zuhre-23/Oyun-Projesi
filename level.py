import pygame

class Level:
    def __init__(self):
        self.platforms=[
            pygame.Rect(100,500,100,100),
            pygame.Rect(180,500,100,100),
            pygame.Rect(260,500,100,100),
            pygame.Rect(340,300,100,100),
            pygame.Rect(420,300,100,100),
        ]

        self.platform_resmi = pygame.image.load("Platform.PNG")


    def draw (self, surface ):
        for rect in self.platforms:
            surface.blit(self.platform_resmi, rect.topleft)