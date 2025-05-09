import pygame
import math
from level import Level
from player import Player
GENISLIK , YUKSEKLIK = 1000,700
FPS=60

class Game:
    def __init__(self):
        self.pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
        pygame.display.set_caption("OYUN")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Courier New" ,50, bold=True)

        self.arkaplan = pygame.image.load("Background.png")
        self.arkaplan_boyut = pygame.transform.scale(self.arkaplan,size=(GENISLIK,YUKSEKLIK))

        self.arkaplan_2 = pygame.image.load("Background_2.png")
        self.arkaplan_2_boyut = pygame.transform.scale(self.arkaplan_2,size=(GENISLIK,YUKSEKLIK))
        
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
            self.pencere.blit(self.karakter_resmi,(GENISLIK//2 - self.karakter_resmi.get_width()//2, 150))

            baslik_metni = "2D Platform Oyunu"
            baslik_font = pygame.font.SysFont("Courier New",70, bold= True)
            baslik_renk = (255,215,0)
            baslik = baslik_font.render(baslik_metni,True,(255,255,0))
            gölge = baslik_font.render(baslik_metni, True,(0,0,0))

            dalga_y = 60+ math.sin(pygame.time.get_ticks()*0.002)*10
            x = GENISLIK//2 - baslik.get_width()//2
            y = int(dalga_y)

            panel = pygame.Surface((baslik.get_width()+40 , baslik.get_height() + 20))
            panel.set_alpha(150)
            panel.fill((0,0,0))
            self.pencere.blit(panel,(x - 20, y - 10))

            self.pencere.blit(gölge, (x + 4, y + 4))
            self.pencere.blit(baslik, (x, y))

            for i, secenek in enumerate(secenekler):
                if i == secili_index:
                    renk = (255, 255, 0)
                else:
                    renk = (200, 200, 200)
                yazi= self.font.render(secenek,True,renk)
                golge = self.font.render(secenek,True,(0,0,0))
                x = GENISLIK//2 - yazi.get_width()//2
                y = 480+ i*80

                if i== secili_index:
                    kutu_genislik = yazi.get_width() + 20
                    kutu_yukseklik = yazi.get_height() + 20
                    kutu_x = GENISLIK // 2 - kutu_genislik // 2
                    kutu_y = y - 20 // 2
                    #pygame.draw.rect(self.pencere, (0, 0, 0), (kutu_x, kutu_y, kutu_genislik, kutu_yukseklik), border_radius=10)
                    pygame.draw.rect(self.pencere, (255, 255, 0), (kutu_x, kutu_y, kutu_genislik, kutu_yukseklik), 3, border_radius=10)


                self.pencere.blit(golge,(x+2,y+2))
                self.pencere.blit(yazi,(x,y))
            pygame.display.update()


    def run(self):
        while True:
            self.menu_acik = True
            self.menu_loop()
            self.level=Level()
            self.player = Player(350,350,self.level) 
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
                keys = pygame.key.get_pressed()
                
                self.player.update(keys)
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