import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((694,388))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame/font/FFFFORWA.TTF', 50)

######################################################################

#Sprites

sky_surf = pygame.image.load('pygame/graphics/background.webp').convert()
ground_surf = pygame.image.load('pygame/graphics/ground.jpg').convert()

score_surf = test_font.render('My game',False, '#0b0c00')
score_rect = score_surf.get_rect(midbottom = (350,100))

snail_surf = pygame.image.load('pygame/graphics/snail.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('pygame/graphics/character1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

######################################################################

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

######################################################################

    #Controls
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
        player_gravity = -20

    if event.type == pygame.MOUSEBUTTONDOWN:
      if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
        player_gravity = -20
        
######################################################################
        
        #Objects 
  
  screen.blit(sky_surf,(0,0))
  screen.blit(ground_surf,(0,300))
  pygame.draw.rect(screen,'#b6cfd4',score_rect)
  pygame.draw.rect(screen,'#b6cfd4',score_rect,10)
  screen.blit(score_surf,score_rect)  

######################################################################  

  #Snail
  snail_rect.x -= 4
  if snail_rect.right <= 0: snail_rect.left = 800
  screen.blit(snail_surf,snail_rect)

######################################################################
  
  #Player
  player_gravity += 1
  player_rect.y += player_gravity
  if player_rect.bottom >= 300:
    player_rect.bottom = 300
  screen.blit(player_surf,player_rect)

######################################################################  

#Collision

if snail_rect.colliderect(player_rect):
  pygame.quit()
  exit()
  
######################################################################    
  pygame.display.update()
  clock.tick(60)