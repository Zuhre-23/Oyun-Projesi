import pygame
import os

def load_images(folder_path, prefix, count):
    images = []
    for i in range(1, count + 1):
        filename = f"{prefix}_{i}.png"
        path = os.path.join(folder_path, filename)
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            images.append(img)
        else:
            print(f"Uyarı: Dosya bulunamadı -> {path}")
    print(f"{prefix} animasyonu için {len(images)} kare yüklendi.")
    return images
