import pygame
import os

def load_images(dosya_yolu, resim_adi, resim_sayisi):
    images = []
    for i in range(1, resim_sayisi + 1):
        filename = f"{resim_adi}_{i}.png"
        path = os.path.join(dosya_yolu, filename)
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            images.append(img)
    return images
