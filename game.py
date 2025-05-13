import pygame
import math
import random
from level import Level
from player import Player
from player import Enemy
GENISLIK , YUKSEKLIK = 1000,700
FPS=60

class Game:
    def __init__(self):
        self.pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
        pygame.display.set_caption("Game")
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
        self.enemy = Enemy(1000, 200, "flight.png", 150, 150, 8 , 3)

        self.menu_acik = True
        self.game_over = True
        self.death_timer = 0

    def menu_loop(self):
        secenekler = ["Start","Exit"]
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

            baslik_metni = "FLIPSIDE"
            baslik_font = pygame.font.SysFont("Courier New",70, bold= True)
            baslik_renk = (255,215,0)
            baslik = baslik_font.render(baslik_metni,True,(255,255,0))
            gölge = baslik_font.render(baslik_metni, True,(0,0,0))

            dalga_y = 60+ math.sin(pygame.time.get_ticks()*0.005)*10
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
            self.game_over = False

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
                
                if self.level.won:
                    panel = pygame.Surface((500,120))
                    panel.set_alpha(100)
                    panel.fill((0,0,0))
                    self.pencere.blit(panel,(GENISLIK//2 - 250, YUKSEKLIK//2 - 60,500, 120))
                    pygame.draw.rect(self.pencere, (255, 215, 0), (GENISLIK // 2 - 250, YUKSEKLIK // 2 - 60, 500, 120),5)

                    win_text = "YOU WIN!"
                    font = pygame.font.SysFont("Courier New",80, bold=True)
                    golge = font.render(win_text,True,(0,0,0))
                    self.pencere.blit(golge, (GENISLIK // 2 - golge.get_width() // 2 + 4, YUKSEKLIK // 2 - 36 + 4))
                    text = font.render(win_text, True, (255, 215, 0)) 
                    self.pencere.blit(text, (GENISLIK // 2 - text.get_width() // 2, YUKSEKLIK // 2 - 36))

                    for i in range(100):
                        x = random.randint(0, GENISLIK)
                        y = random.randint(0, YUKSEKLIK)
                        pygame.draw.circle(self.pencere, (255, 255, 0), (x, y), 2)

                    pygame.display.update()
                    pygame.time.wait(5000)
                    break
                
                if self.level.game_over or self.player.rect.top >= YUKSEKLIK:
                    self.player.is_dead = True

                if self.player.is_dead:
                    self.player.update(pygame.key.get_pressed())
                    self.level.update_door_animation()
                    self.draw()
                    self.death_timer += 1

                    karartma = pygame.Surface((GENISLIK, YUKSEKLIK))
                    karartma.set_alpha(180)
                    karartma.fill((0, 0, 0))
                    self.pencere.blit(karartma, (0, 0))

                    panel_x = GENISLIK // 2 - 250
                    panel_y = YUKSEKLIK // 2 - 60
                    pygame.draw.rect(self.pencere, (0, 0, 0), (panel_x, panel_y, 500, 120))
                    pygame.draw.rect(self.pencere, (255, 0, 0), (panel_x, panel_y, 500, 120), 5)

                    yazi = self.font.render("He is dead", True, (255, 0, 0))
                    gölge = self.font.render("He is dead", True, (0, 0, 0))
                    x = GENISLIK // 2 - yazi.get_width() // 2
                    y = YUKSEKLIK // 2 - yazi.get_height() // 2
                    self.pencere.blit(gölge, (x + 3, y + 3))
                    self.pencere.blit(yazi, (x, y))
                    pygame.display.update()
                    if self.death_timer > FPS * 2:
                        break
                    continue

                        
                self.pencere.blit(self.arkaplan_boyut,(0,0))
                self.level.update_door_animation()
                keys = pygame.key.get_pressed()
                
                self.player.update(keys)
                if self.player.rect.left < 0:
                    self.player.rect.left = 0
                if self.player.rect.right > GENISLIK:
                    self.player.rect.right = GENISLIK

                if self.level.hareketli_platform_karakter and self.player.on_ground:
                    self.player.rect.x += 2* self.level.yatay_hareket_yönü
                
                self.level.update(self.player)
                self.level.temas_kontrolu(self.player)

                player_center = pygame.Vector2(self.player.rect.center)
                enemy_center = pygame.Vector2(self.enemy.rect.center)
                mesafe = player_center.distance_to(enemy_center)

                if mesafe < 60 and not self.player.is_dead:
                    self.player.die()

                self.enemy.update()
                self.draw()
    
    def draw(self):
        if self.level.active_evren == 1:
            self.pencere.blit(self.arkaplan_boyut, (0, 0))
        else:
            self.pencere.blit(self.arkaplan_2_boyut, (0, 0))
            
        self.enemy.draw(self.pencere)
        self.player.draw(self.pencere)
        self.level.draw(self.pencere)
        
        pygame.display.update()