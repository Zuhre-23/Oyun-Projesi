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
        self.font = pygame.font.SysFont("Courier New" ,50, bold=True)

        self.arkaplan = pygame.image.load("Background.png")
        self.arkaplan_boyut = pygame.transform.scale(self.arkaplan,size=(GENİSLİK,YUKSEKLİK))

        self.arkaplan_2 = pygame.image.load("Background_2.png")
        self.arkaplan_2_boyut = pygame.transform.scale(self.arkaplan_2,size=(GENİSLİK,YUKSEKLİK))
        
        self.karakter_resmi = pygame.image.load("karakter.png")
        self.karakter_resmi = pygame.transform.scale(self.karakter_resmi,(280,280))

        self.level=Level()
        self.player = Player(50, 600, self.level)
        self.menu_acik = True

    def menu_loop(self):
        secenekler = ["Oyunu Başlat","Çıkış"]
        secili_index =0
        while self.menu_acik :
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        secili_index = (secili_index-1)%len(secenekler)
                    elif event.key == pygame.K_DOWN:
                        secili_index = (secili_index+1)%len(secenekler)
                    elif event.key == pygame.K_RETURN:
                        if secili_index ==0:
                            self.menu_acik = False
                        elif secili_index ==1:
                            pygame.quit()
                            exit()
            self.pencere.blit(self.arkaplan_boyut,(0,0))
            self.pencere.blit(self.karakter_resmi,(GENİSLİK//2 - self.karakter_resmi.get_width()//2, 150))

            baslik_metni = "2D Platform Oyunu"
            baslik= self.font.render(baslik_metni,True,(55,55,55))
            golge = self.font.render(baslik_metni,True,(0,0,0))
            self.pencere.blit(golge,((GENİSLİK//2 - baslik.get_width()//2)+2, 60+2))
            self.pencere.blit(baslik,((GENİSLİK//2 - baslik.get_width()//2), 60))

            for i, secenek in enumerate(secenekler):
                if i == secili_index:
                    renk = (255, 255, 0)
                else:
                    renk = (200, 200, 200)
                yazi= self.font.render(secenek,True,renk)
                shadow = self.font.render(secenek,True,(0,0,0))
                x = GENİSLİK//2 - yazi.get_width()//2
                y = 430+ i*80
                self.pencere.blit(shadow,(x+2, y+2))
                self.pencere.blit(yazi,(x,y))

                if i== secili_index:
                    imlec = self.font.render("-->",True,renk)
                    self.pencere.blit(imlec, (x-50, y))
            pygame.display.update()


    def run(self):
        while True:
            self.menu_acik = True
            self.menu_loop()
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
        
        self.player.draw(self.pencere)
        self.level.draw(self.pencere)
        pygame.display.update()