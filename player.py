import pygame
from animation_loader import load_images

class Player:
    def __init__(self,x,y,level):
        self.rect=pygame.Rect(x,y,50,80)
        self.level=level
        self.current_frame=0
        self.frame_timer=0
        self.jump_velocity=0
        self.gravity=1.4
        self.on_ground = True
        self.looking_left= False

        self.is_running =False
        self.is_jumping=False
        self.is_rolling =False
        self.is_dead=False
       
        folder ="animations//PNG"
        self.animations = {
            'idle' : load_images(f"{folder}/idle","idle",12),
            'run' : load_images(f"{folder}/run", "run" ,10),
            'jump' : load_images(f"{folder}/jump_full", "jump" ,22),
            'roll' : load_images(f"{folder}/roll", "roll",8),
            'death' :load_images(f"{folder}/death" , "death", 19),

                    }

    def move_and_check_collisions(self,keys):
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -5
            self.looking_left_True

        elif keys[pygame.K_RIGHT]:
            dx = 5
            self.looking_left = False

        if keys[pygame.K_DOWN] and self.on_ground and not self.is_jumping:
            self.is_rolling = True
            self.current_frame = 0
        
        if keys[pygame.K_UP] and self.on_ground:
            self.jump_velocity = -17
            self.on_ground = False
            self.is_jumping = True
        
        dy += self.jump_velocity
        if not self.on_ground:
            self.jump_velocity += self.gravity


    def update_animation(self):
        self.frame_timer += 1
        if self.frame_timer >= 6:
            anim = self.get_animation_state()
            self.current_frame += 1
            if anim in ['roll', 'death'] and self.current_frame >= len(self.animations[anim]):
                self.current_frame =0


                if anim == 'roll':
                    self.is_rolling = False
                if anim == 'death':
                    self.is_dead = True
        
        else:
            self.current_frame %= len(self.animations[anim])
        self.frame_timer = 0

    def draw(self, surface):
        anim = 'death' if self.is_dead else self.get_animation_state()

        frame = self.animations[anim][self.current_frame % len(self.animations[anim])]

        if self.looking_left:
            frame = pygame.transform.flip(frame, True, False)
        
        pos = (self.rect.centerx - frame.get_width() // 2, self.rect.bottom - frame.get_height())
        surface.blit(frame, pos)


    def get_animation_state(self):
        if self.is_rolling:
            return 'roll'
        if self.is_jumping:
            return 'jump'
        if self.is_running:
            return 'run'
        if self.is_dead:
            return 'death'
        
        return 'idle'
    
    def die(self):
        if not self.is_dead:
            self.is_dead = True
            self.current_frame = 0
            self.frame_timer = 0


class Enemy:
    def __init__(self, x, y, sprite_path, frame_width, frame_height, num_frames, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.current_frame = 0
        self.frame_timer = 0
        self.direction = -1
        self.flip = False

        self.sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
        self.frames = self.load_frames(frame_width, frame_height, num_frames)
        self.rect = pygame.Rect(self.x , self.y, frame_width, frame_height)

    def load_frames(self, width, height, num_frames):
        frames = []
        for i in range(num_frames):
            frame = self.sprite_sheet.subsurface(pygame.Rect(i * width, 0, width, height ))
            frames.append(frame)
        return frames

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= 5:
            self.current_frame = (self.current_frame + 1)% len(self.frames)
            self.frame_timer = 0
        
        self.x += self.speed * self.direction

        if self.x <=0:
             self.direction = 1
             self.flip = False
        elif self.x + self.rect.width >= 1000:
            self.direction = -1
            self.flip = True

        self.rect.topleft = (self.x, self.y)
    
    def draw(self, surface):
        frame = self.frames[self.current_frame]
        if self.flip:
            frame = pygame.transform.flip(frame, True , False)
        surface.blit(frame, (self.x, self.y))    























     

                    













         
