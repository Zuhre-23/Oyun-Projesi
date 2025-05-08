import pygame
from animation_loader import load_images

class Level:
    def __init__(self):
        self.evren1=[
            pygame.Rect(100,500,100,100),
            pygame.Rect(180,500,100,100),
            pygame.Rect(260,500,100,100),
           
        ]
        self.evren2=[
            pygame.Rect(340,300,100,100),
            pygame.Rect(420,300,100,100),
        ]
        self.gems = [
            pygame.Rect(100,500,32,32),
            pygame.Rect(100,600,32,32)
        ]

        self.platform_1 = pygame.image.load("Platform.PNG")
        self.platform_2 = pygame.image.load("Platform_2.PNG")
        self.active_evren = 1

        self.yatay_hareketli_platform =pygame.Rect(500, 550, 120, 20)
        self.yatay_hareket_yönü = 1
        self.hareketli_platform_karakter =False
        self.dikey_hareketli_platform = pygame.Rect(80,50,50,50) 
        self.dikey_hareket_yönü = 1     


        self.door = pygame.Rect(800,450,150,300)
        self.door_frames = load_images("animations//door","portal1_frame",6)
        self.door_current_frame = 0
        self.door_frame_timer = 0

        self.gem = pygame.image.load("gem.PNG")
        

    def evren_degistir(self):
        if self.active_evren == 1:
            self.active_evren = 2
        else :
            self.active_evren = 1
    
    def get_active_platforms(self):
        if self.active_evren == 1:
            aktifler = self.evren1
        else:
            aktifler = self.evren2
        return aktifler
    
    def get_passive_platforms(self):
        if self.active_evren == 1:
            return self.evren2
        else:
            return self.evren1

    def update_door_animation(self): #kapı animasyonun sürekli ççalışmasını sağlar
            self.door_frame_timer += 1
            if self.door_frame_timer >= 10:
                self.door_current_frame = (self.door_current_frame+1)% len(self.door_frames)
                self.door_frame_timer = 0

    def update(self,player):
        #YATAY HAREKETLİ
        self.yatay_hareketli_platform.x += 2 * self.yatay_hareket_yönü
        if self.yatay_hareketli_platform.left <= 100 or self.yatay_hareketli_platform.right >= 700:
            self.yatay_hareket_yönü *= -1

        if self.hareketli_platform_karakter:
           player.rect.x += 2 * self.yatay_hareket_yönü 

        #DİKEY HAREKETLİ
        self.dikey_hareketli_platform.y += 2 * self.dikey_hareket_yönü
        if self.dikey_hareketli_platform.top <= 50 or self.dikey_hareketli_platform.bottom >= 450:
            self.dikey_hareket_yönü *= -1


    def draw (self, surface ):

        saydam_surface=pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        saydam_surface.set_alpha(100)

        for rect in self.get_passive_platforms():
            if self.active_evren == 1:
                platform_resmi_boyut=pygame.transform.scale(self.platform_2, (rect.width, rect.height))

            else:
                platform_resmi_boyut=pygame.transform.scale(self.platform_1, (rect.width, rect.height))
            saydam_surface.blit(platform_resmi_boyut, rect.topleft)

        surface.blit(saydam_surface, (0, 0))

        for rect in self.get_active_platforms():
            if self.active_evren == 1:
                platform_resmi_boyut = pygame.transform.scale(self.platform_1, (rect.width ,rect.height))
            else:
                 platform_resmi_boyut = pygame.transform.scale(self.platform_2, (rect.width ,rect.height)) 
            surface.blit(platform_resmi_boyut, rect.topleft)

        if self.active_evren == 1:
            hareketli_platform_resmi=self.platform_1
        else:
            hareketli_platform_resmi=self.platform_2

        hareketli_platform_resmi_boyut=pygame.transform.scale(hareketli_platform_resmi, (self.yatay_hareketli_platform.width, self.yatay_hareketli_platform.height))
        surface.blit(hareketli_platform_resmi_boyut, self.yatay_hareketli_platform.topleft)
        
        if self.active_evren == 1:
            platform_image = self.platform_1
        else:
            platform_image = self.platform_2

        scaled_vertical = pygame.transform.scale(platform_image, (self.dikey_hareketli_platform.width, self.dikey_hareketli_platform.height))
        surface.blit(scaled_vertical, self.dikey_hareketli_platform.topleft)

        
        if self.door_frames:
            current_frame = self.door_frames[self.door_current_frame]
            surface.blit(current_frame,self.door.topleft)

        for gem in self.gems:
            surface.blit(self.gem,gem.topleft)
        