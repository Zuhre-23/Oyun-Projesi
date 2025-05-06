import pygame
from animation_loader import load_images

class Level:
    def __init__(self):
        self.platforms=[
            pygame.Rect(100,500,100,100),
            pygame.Rect(180,500,100,100),
            pygame.Rect(260,500,100,100),
            pygame.Rect(340,300,100,100),
            pygame.Rect(420,300,100,100),
        ]

        self.platform_1 = pygame.image.load("Platform.PNG")
        self.active_evren = 1
        self.yatay_hareketli_platform =pygame.Rect(500, 550, 120, 20)
        self.yatay_hareket_yönü = 1
        self.hareketli_platform_karakter =False

        self.door = pygame.Rect(900,550,150,300)
        self.door_frames = load_images("animations//door","portal1_frame",6)
        self.door_current_frame = 0
        self.door_frame_timer = 0
        


    def evren_degistir(self):
        if self.active_evren == 1:
            self.active_evren = 2
        else :
            self.active_evren = 1

    def update_door_animation(self): #kapı animasyonun sürekli ççalışmasını sağlar
            self.door_frame_timer += 1
            if self.door_frame_timer >= 10:
                self.door_current_frame = (self.door_current_frame+1)% len(self.door_frames)
                self.door_frame_timer = 0

    def update(self,player):
        self.yatay_hareketli_platform.x += 2 * self.yatay_hareket_yönü
        if self.yatay_hareketli_platform.left <= 100 or self.yatay_hareketli_platform.right >= 700:
            self.yatay_hareket_yönü *= -1

        if self.hareketli_platform_karakter:
           player.rect.x += 2 * self.yatay_hareket_yönü 

    def draw (self, surface ):
        for rect in self.platforms:
            surface.blit(self.platform_1, rect.topleft)

        platform_resmi=self.platform_1
        platform_resmi_boyut=pygame.transform.scale(platform_resmi, (self.yatay_hareketli_platform.width, self.yatay_hareketli_platform.height))
        surface.blit(platform_resmi_boyut, self.yatay_hareketli_platform.topleft)
        
        if self.door_frames:
            current_frame = self.door_frames[self.door_current_frame]
            surface.blit(current_frame,self.door.topleft)

        