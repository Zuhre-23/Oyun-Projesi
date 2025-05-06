import pygame
from level import Level
from player import Player
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
        self.player = Player(50, 600, self.level)

    def run(self):
        oyun_acik = True
        while oyun_acik :
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    oyun_acik = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.level.evren_degistir()
                    elif event.key == pygame.K_ESCAPE:
                        oyun_acik=False
                    
            self.pencere.blit(self.arkaplan_boyut,(0,0))
            self.level.update_door_animation()

            self.level.update(self.player)

            self.draw()
    
    def draw(self):
        if self.level.active_evren == 1:
            self.pencere.blit(self.arkaplan_boyut, (0, 0))
        else:
            self.pencere.blit(self.arkaplan_2_boyut, (0, 0))
        
        self.level.draw(self.pencere)
        pygame.display.update()