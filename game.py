import pygame
from level import Level
GENİSLİK , YUKSEKLİK = 1000,700
FPS=60

class Game:
    def __init__(self):
        self.pencere = pygame.display.set_mode((GENİSLİK, YUKSEKLİK))
        pygame.display.set_caption("OYUN")
        self.clock = pygame.time.Clock()

        self.arkaplan = pygame.image.load("Background.png")
        self.arkaplan_boyut = pygame.transform.scale(self.arkaplan,size=(GENİSLİK,YUKSEKLİK))

        self.arkaplan_2 = pygame.image.load("Background_2.png")
        self.arkaplan_2_boyut = pygame.transform.scale(self.arkaplan_2,size=(GENİSLİK,YUKSEKLİK))
        self.level=Level()

    def run(self):
        oyun_acik = True
        while oyun_acik :
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    oyun_acik = False

            self.pencere.blit(self.arkaplan_boyut,(0,0))
            self.level.update_door_animation()

            self.draw()
    
    def draw(self):
        self.level.draw(self.pencere)
        pygame.display.update()