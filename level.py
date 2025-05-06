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

        self.platform_resmi = pygame.image.load("Platform.PNG")

        self.door = pygame.Rect(900,550,150,300)
        self.door_frames = load_images("animations//door","portal1_frame",6)
        self.door_current_frame = 0
        self.door_frame_timer = 0

    def update_door_animation(self): #kapı animasyonun sürekli ççalışmasını sağlar
            self.door_frame_timer += 1
            if self.door_frame_timer >= 10:
                self.door_current_frame = (self.door_current_frame+1)% len(self.door_frames)
                self.door_frame_timer = 0



    def draw (self, surface ):
        for rect in self.platforms:
            surface.blit(self.platform_resmi, rect.topleft)

        if self.door_frames:
            current_frame = self.door_frames[self.door_current_frame]
            surface.blit(current_frame,self.door.topleft)