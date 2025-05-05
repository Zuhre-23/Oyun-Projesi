import pygame

pygame.init()

window=pygame.display.set_mode((800,600))
flag=True

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False 

