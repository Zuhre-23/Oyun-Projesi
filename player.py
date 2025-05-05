import pygame
from animation_loader import load_images

class Player:
    def __innit__(self, x, y, level):
        self.rect =pygame.Rect(x, y, 50, 80)
        self.level =level
        self.current_frame =0
        self.frame_timer =0
        self.jump_velocity =0
        self.gravity =1.4
       
        

        folder = "animations//PNG"
        self.animations = {
            'idle': load_images(f"{folder}/idle", "idle", 12),
            'run': load_images(f"{folder}/run", "run", 10),
            'jump': load_images(f"{folder}/jump_full", "jump", 22),
            'roll': load_images(f"{folder}/roll", "roll", 8),
            'death': load_images(f"{folder}/death", "death", 19),

        }











            }
        }
